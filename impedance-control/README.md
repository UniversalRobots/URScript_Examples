# Impedance Control Example

This folder contains an example URScript implementation of a joint-space impedance (PD torque) controller with dynamics compensation for Universal Robots e-Series robots.

The script demonstrates how to control the robot to follow a circular trajectory in Cartesian space using an impedance controller. The targets are converted from Cartesian space to joint space and thereafter used as target for the joint based impedance controller. The controller compensates for the robot's dynamics and clamps the commanded torques.

The direct torque control is supported by all e-Series and UR-Series robots from Polyscope 5 software version 5.23 and PolyscopeX software version 10.10.

## Background

Impedance control is a control strategy that regulates the dynamic relationship between force and motion at the robot's end-effector. In joint-space impedance control, the robot's joints are controlled to behave like a virtual mass-spring-damper system, allowing compliant interaction with the environment.

This example uses a PD (proportional-derivative) controller with feedforward dynamics compensation (mass matrix and Coriolis/centrifugal terms) to achieve accurate and compliant motion.

## Note
Position singularities are not handled as well as rapid motions can happen with a PD controller depending on the gains and distance to the target. The script is currently only tested with a ur3e, ur5e, ur10e.
