# Install Ubuntu 24.04.2 LTS Noble Numbat
FROM ubuntu:24.04

# Delete any existing user with UID 1000 (e.g., 'ubuntu')
RUN userdel -r ubuntu || true

# Get the user name, user id and group id from the host (if passed, when building the docker image)
# Their default values are "user", "1000:1000"
ARG USER=user
ARG USER_ID=1000
ARG GROUP_ID=1000

# Define USER and HOME environment variables to match the non-root user context.
# This ensures that any tools or scripts relying on $USER or $HOME 
# use the intended paths (/home/$USER), preventing unexpected fallback to /home/ubuntu.
ENV USER=${USER}
ENV HOME=/home/${USER}

# Set the non-interactive debian frontend
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections

# Update, upgrade and install apt packages
RUN apt update && apt upgrade -y && apt autoremove -y
RUN apt install -y \
    --no-install-recommends \
    sudo \
    cmake \
    g++ \
    python3-pip \
    build-essential \
    apt-utils \
    curl \
    bash-completion \
    lsb-release \
    gnupg2 \
    iputils-ping \
    net-tools \
    nano \
    dbus-x11 \
    gedit \
    htop \
    wget \
    git \
    libeigen3-dev \
    libgtest-dev \
    mesa-utils

# Add a user and a group, based on their id
RUN groupadd -g $GROUP_ID -o $USER \
    && useradd --no-log-init -m -u $USER_ID -g $GROUP_ID -o -s /bin/bash $USER \
    && usermod -aG sudo $USER \
    && echo "%sudo ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

### ROS2 Jazzy Jalisco steps ###

# Set locale
RUN apt update && sudo apt install locales
RUN locale-gen en_US en_US.UTF-8
RUN update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
RUN export LANG=en_US.UTF-8

# Enable required repositories
RUN apt install -y software-properties-common
RUN add-apt-repository universe -y

RUN set -e; \
    export ROS_APT_SOURCE_VERSION=$(curl -s https://api.github.com/repos/ros-infrastructure/ros-apt-source/releases/latest | grep -F "tag_name" | awk -F\" '{print $4}'); \
    curl -L -o /tmp/ros2-apt-source.deb "https://github.com/ros-infrastructure/ros-apt-source/releases/download/${ROS_APT_SOURCE_VERSION}/ros2-apt-source_${ROS_APT_SOURCE_VERSION}.$(. /etc/os-release && echo $VERSION_CODENAME)_all.deb"; \
    dpkg -i /tmp/ros2-apt-source.deb && rm /tmp/ros2-apt-source.deb

# Install development tools
RUN apt update && sudo apt install -y ros-dev-tools

# Install ROS2 Jazzy Jalisco
RUN apt update && apt upgrade
RUN apt install -y ros-jazzy-desktop

USER $USER
WORKDIR $HOME