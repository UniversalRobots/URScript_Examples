# Control WAGO 750 series Modbus IO bridge

Examples require [Universal-Robots software 5.14.0](https://www.universal-robots.com/articles/ur/release-notes/release-note-software-version-514xx/) or later.

Efficient control of inputs and outputs of I/O modules connected to Modbus bridge.

# Getting started

Copy read-digital.script to the robot. Create new program with a script node, and load copied script file.

# Hardware setup

Example system was assembled from following components:

|     | Part number | Description
| --- | ----------- | -----------
| 1   | 750-362     | Modbus coupler
| 2   | 750-1405    | 16 digital inputs
| 3   | 750-474     | 2 analog 4-20mA inputs
| 4   | 750-430     | 8 digital inputs

# Bridge, and I/O modules configuration

IP address should be configured, and Modbus protocol enabled.
Configuring WAGO coupler and modules is beyond the scope of this example.