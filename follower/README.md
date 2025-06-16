# Robot Follower Example

This example demonstrates how to create a follower robot that tracks the position of a leader robot using Modbus communication in real-time. By default, the follower robot replicates the joint angles of the leader robot directly using servoj. An optional mirror mode is available for symmetrical movements.

This setup has several practical applications:

- Remote Control: One robot can be used as a leader to directly control another robot, enabling leader-follower robot setup. One leader robot can have multiple followers
- Data Collection: The follower setup can be used to collect synchronized movement data from both robots for machine learning and performance analysis
- Training: An expert operator can demonstrate movements on the leader robot while trainees observe the synchronized motion on the follower robot
- Performance Art: Two or more robots can be choreographed to perform synchronized or mirrored movements for demonstrations and artistic installations


This is achieved by:
- Reading the leader robot's joint angles through Modbus communication
- Directly replicating these joint angles on the follower robot
- Optionally supporting a mirror mode for symmetrical movements. Useful for making the two robots dance towards each other.

## Features

- Real-time joint angle replication from leader robot
- Modbus-based communication directly between the robot for reliable data exchange
- Smooth motion interpolation for natural following behavior using servoj
- Optional mirror mode for symmetrical movements

## Leader

Depending on the use case, a Leader program could be the Admittance controller, a dance program or maybe just the robot's Freedrive.
To get the Admittance controller example, please see this repo's [admittance-control](https://github.com/UniversalRobots/URScript_Examples/tree/main/admittance-control) folder

## Getting Started

1. Upload the followerUR10e.urp and followerUR10e.installation to the follower robot
2. Open the followerUR10e.urp and ensure that it also opens the followerUR10e.installation. If you are using it on another robot or software version, you might need to adapt the safety settings to the robot type.
3. Update the Installation -> Fieldbus -> Modbus settings with the leader robot's IP address. On this page, please also verify that there is a connection established and that everything is green. 
4. Enable the Modbus service on the Leader robot by Settings -> Security -> Services
5. Adjust the safety settings to the needs and risk assessment
6. Start the program on Follower robot before the Leader.

## Hardware Requirements

- At least two Universal Robots with software 5.19 or newer (A Leader and one or more Followers)
- Working network connection between the robots
