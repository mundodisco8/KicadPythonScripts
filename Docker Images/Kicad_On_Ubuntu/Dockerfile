# Kicad on Ubuntu for scripting
FROM ubuntu:19.10
LABEL maintainer="jsantosrico@gmail.com"

# Update the image to the latest packages
ARG DEBIAN_FRONTEND=noninteractive
# RUN apt-get update && apt-get upgrade -y
# Install Kicad (basic package) and nano...
RUN apt-get update && apt-get install -y software-properties-common \
    && rm -rf /var/lib/apt/lists/*
RUN apt-get update && add-apt-repository --yes ppa:js-reynaud/kicad-5.1
RUN apt-get update && apt-get install -y \
    kicad --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*
# Install pip and the dependencies that will be needed for the plugins
RUN apt-get update && apt-get install -y \
    nano \
    git \
    python3-venv \
    python3-pip \
    python3-setuptools \
    ssh \
    --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*
RUN pip3 install wheel pillow openPyXL
# Clone Kiplot...
RUN git clone --single-branch --branch Support_more_than_2_layers https://github.com/mundodisco8/kiplot.git /kiplot
RUN git clone --single-branch --branch Fix_+_variants https://github.com/mundodisco8/KiBoM.git /KiBoM
# Make scripts callable without having to add the path
RUN ln -s /KiBoM/KiBOM_CLI.py /usr/bin/KiBOM_CLI.py && \
    chmod +x //usr/bin/KiBOM_CLI.py
# ... and create a virtualenv and install it on it
RUN cd kiplot && pip3 install -e .