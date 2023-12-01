# Admittance Control Example 

This is an URScript example of an admittance control loop utilize the force torque sensor in the tool flange of the Universal Robots E-series robots.
It script is designed to run on UR5e robot, but can be adjusted, through parameters, to work on other e-series robots.

## Background
Admittance control is a type of control algorithm for robots that physically interact with the environment or objects. It transforms the forces and torques applied by the external contact into the desired position and orientation of the robot’s end-effector.\
Admittance control can make the robot behave like a programmable spring-mass-damper system, where the stiffness, damping, and inertia parameters can be adjusted according to the desired dynamic behavior. Admittance control can be used for applications such as human-robot interaction, precision assembly, medical surgery, and finishing processes.


## Note
Position singularities is not handled and can therefore give rapid motions.