#!/bin/bash
set -e

echo "Build and source the ROS2 workspace"

# Resolve dependencies
sudo rosdep init
rosdep update
rosdep install -i --from-path src --rosdistro jazzy -y

# Build the workspace with colcon
colcon build

# Source ROS2 Jazzy Jalisco
source /opt/ros/jazzy/setup.bash
. install/setup.bash