This example is implementing simple plain socket communication from
Universal Robots controller to HMI implemented in python.

# Quick start using dockerized simulator
Start docker mapping 'programs' into URSim
```bash
# Windows
docker run --rm -dit -p 5900:5900 -p 6080:6080 -v "$(pwd)/programs:/ursim/programs.UR5" --name ursim universalrobots/ursim_e-series

# Linux
docker run --rm -dit -p 5900:5900 -p 6080:6080 -v ./programs:/ursim/programs.UR5 --name ursim universalrobots/ursim_e-series
```
Connect to URSim using VNC (it's recommended to use VNC client application like remmina or ultravnc)
Load socket_hmi_example program in Polyscope. 
Power on simulated robot arm.
Update ip address in socket_open() script node.

Start python HMI
```bash
python hmi-example.py
```

Play program

# Quick start with real robot
Upload socket_hmi_example to robot
Update ip address in socket_open() script node.

Start python HMI
```bash
python hmi-example.py
```

Play program
