# Control Festo CMMT-AS series servo

Examples require Universal-Robots software 5.14.0 or later.

Example is exchanging data using telegram 111.
Basic error handling routines are implemented.

# Getting started

There are two components:
- festo_servo_library.script - library of utility script functions
- cmmt_servo1.urp - example program that uses library to move between two fixed positions

Both files should be uploaded to the robot.

# Known issues

Referencing method using end switch may not work. Workarounds are to use Festo Automation Studio for referencing, or moving servo to desired position using jogging commands, and using "set home to current position" method.

# Servo configuration

Configuring servo drives is beyond the scope of this example. Drive, motor, gearbox, and rail should be configured
beforehands.