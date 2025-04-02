# Modbus
Example programs, and URScript snippets. 

Script code is intended to be used in URCap plugins for Universal-Robots, as well as in end applications.
New modbus client functionality is not available through Polyscope GUI yet.

Refer to release notes and script manual for more detailed description.

# Examples

Examples showing efficient communication with modbus leveraging URScript improvements in 5.14.0 and later.
- [Festo CMMT-AS servo drive control](festo-cmmt-as)
- [Festo CPX Modbus bridge](festo-cpx)
- [Wago 750-series Modbus bridge](wago-750)

# Getting started using robot simulator
Examples can be easily tried out without real UR robot.

Universal-Robots provides [dockerized simulator images](https://hub.docker.com/r/universalrobots/ursim_e-series).
Simulator includes modbus client functionality. Follow instructions on dockerhub to download simulator image.

**NOTE:** It's recommended to use UltraVNC Viewer (Windows) or Remmina (Linux) to interact with Polyscope GUI instead of using http VNC interface.

By default when simulator is started no external files can be accessed. Following command starts URSim mapping current folder into subfolder to programs in URSim:

```bash
# Linux
docker run -dit --rm -p 5900:5900 -v ./:/ursim/programs/modbus --name ursim universalrobots/ursim_e-series

# Windows
docker run -dit --rm -p 5900:5900 -v "$(PWD):/ursim/programs/modbus" --name ursim universalrobots/ursim_e-series
```

# Contributing

If there is any example that was tested then create a pull request

If you're a company that can  provide modbus device for testing then create an issue, and Universal-Robots R&D team will contact you.