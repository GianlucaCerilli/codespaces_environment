# codespaces_environment

The repository allows to work through a Docker image based on:

* Ubuntu 24.04.2 LTS Noble Numbat
* ROS2 Jazzy Jalisco

The `ros2_ws` folder represents the ROS2 workspace and can be built and sourced running:
```
cd ros2_ws
./configure_workspace.sh
```

You can then source from another terminal by running:
```
cd ros2_ws
. install/setup.bash
```

The `ros2_ws` contains two folders:

* *ros2_codespaces_cpp*
* *ros2_codespaces_py*

used to locate ROS2 files in cpp and python.

The repository contains two additional folders:

* *cpp*
* *python*

used to locate cpp and python files, independent from the ROS2 environment.