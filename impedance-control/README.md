# Impedance Control Example

This folder contains an example URScript implementation of a joint-space impedance (PD torque) controller with dynamics compensation for Universal Robots e-Series robots.

The script demonstrates how to control the robot to follow a circular trajectory in Cartesian space using an impedance controller. The targets are converted from Cartesian space to joint space, before the impedance controller is computing the control input.  The controller compensates for the robot's dynamics and clamps the commanded torques.

The impedance control is, at the commit time, depending on a beta version of the Universal Robots software. Sign up for the beta at https://ur.centercode.com/key/PolyScope5Beta

## Background

Impedance control is a control strategy that regulates the dynamic relationship between force and motion at the robot's end-effector. In joint-space impedance control, the robot's joints are controlled to behave like a virtual mass-spring-damper system, allowing compliant interaction with the environment or precise trajectory tracking.

This example uses a PD (proportional-derivative) controller with feedforward dynamics compensation (mass matrix and Coriolis/centrifugal terms) to achieve accurate and compliant motion.

## Note
Position singularities is not handled as well as it is a PD controller make rapid motions depending on the gains and targets. The script is currently only tested with a ur3e, ur5e ur10e. 