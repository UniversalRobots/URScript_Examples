#!/usr/bin/env python3
# Copyright (c) 2020-2023, Universal Robots A/S,
# All rights reserved.
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#    * Redistributions of source code must retain the above copyright
#      notice, this list of conditions and the following disclaimer.
#    * Redistributions in binary form must reproduce the above copyright
#      notice, this list of conditions and the following disclaimer in the
#      documentation and/or other materials provided with the distribution.
#    * Neither the name of the Universal Robots A/S nor the names of its
#      contributors may be used to endorse or promote products derived
#      from this software without specific prior written permission.
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL UNIVERSAL ROBOTS A/S BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import logging
import argparse
import struct
import socket
import threading
import tkinter as tk
from tkinter import font

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--fullscreen', action='store_true', help='run in fullscreen mode')
    parser.add_argument('-p', '--port', type=int, default=60000, help='server port')
    parser.add_argument('-d', '--debug', action='store_true')
    return parser.parse_args()

class CommandsWindow(tk.Tk):
    def __init__(self, fullscreen=False):
        super().__init__()
        self.log = logging.getLogger("CommandsWindow")
        if fullscreen:
            self.geometry(f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}+0+0")
        
        # set variables for widgets state
        self.analog_var = tk.IntVar()
        self.button1_var = tk.IntVar()
        self.button2_var = tk.IntVar()
        
        # add 3 action widgets, and one text label for status
        self.analog_slider = tk.Scale(self, orient=tk.HORIZONTAL, label="Analog value", width=30, length=300, variable = self.analog_var)
        self.analog_slider.pack(side=tk.TOP)
        
        self.button1 = tk.Checkbutton(self, text="Button 1", height=3, variable=self.button1_var)
        self.button1.pack(side=tk.TOP)

        self.button2 = tk.Checkbutton(self, text="Button 2", height=3, variable=self.button2_var)
        self.button2.pack(side=tk.TOP)
        
        self.status = tk.Label(self, text='no connection', fg='red', font=font.Font(size=30))
        self.status.pack(side=tk.BOTTOM)

class SocketServerThread(threading.Thread):
    # Class encapsulating server
    def __init__(self, **kwargs):
        super().__init__(name="SocketServer", target=self.__run)
        # listen on all network interfaces
        self.__host = kwargs.get("host", "0.0.0.0")
        self.__port = kwargs.get("port")
        self.__keep_running = True
        # reference to window class
        self._gui = kwargs.get("gui")

        self._log = logging.getLogger(__class__.__name__)
        self.daemon = True
        
    def stop(self):
        self.__keep_running = False
        if self.__socket:
            self._log.info("Closing socket")
            self.__socket.shutdown(socket.SHUT_RDWR)
            self.__socket.close()
            self._log.info("Closed")
    
    def _process(self, received):
        # Function expects string in input message from program
        self._log.info(f"Received status: {received.decode('utf-8')}")
        self._gui.status.config(text=received.decode('utf-8'), fg='green')

        # return array of 3 values. Each value is INT32 encoded in network byte order
        return struct.pack("!iii", self._gui.analog_var.get(), self._gui.button1_var.get(), self._gui.button2_var.get())
    
    def __run(self):
        self._log.info("Starting server thread")
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            self.__socket = s
            s.bind((self.__host, self.__port))
            s.listen()
            while self.__keep_running:
                # wait for socket connection from controller
                conn, remote = s.accept()
                with conn:
                    self._log.info(f"Connected from {remote}")
                    try:
                        while True:
                            # expect to receive one data packet, and send response afterwards
                            # NOTE: this is naive implementation of protocol. Data packets can be fragmented, or
                            #       joined if bigger data is sent from controller.
                            data = conn.recv(1024)
                            if not data:
                                break;
                            # send response
                            data = self._process(data)
                            self._log.info(f"Sending {data.hex()}")
                            conn.sendall(data)
                    except Exception as e:
                        self._log.warning(f"Socket exception: {e}")
                    self._log.info(f"Connection from {remote} closed")
        self._log.info(f"Thread stopped")
        
if(__name__ == "__main__"):
    logging.basicConfig(level = logging.INFO)
    log = logging.getLogger()
    
    args = parse_args()
    if args.debug:
        log.setLevel(logging.DEBUG)
    log.debug(args)
    
    # create window user interaction
    window = CommandsWindow(fullscreen=args.fullscreen)
    
    # start background thread that opens server socket
    # and processes connections from controller
    server = SocketServerThread(port = args.port, gui=window)
    server.start()
    
    # window main loop is blocked
    try:
        window.mainloop()
    except KeyboardInterrupt:
        window.destroy()
    except Exception as e:
        log.error(e)
    
    log.info("Stopping server")
    server.stop()
    server.join()
    log.info("Stopped")
    