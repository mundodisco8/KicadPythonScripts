FROM ubuntu:18.04
MAINTAINER Sascha Schade (strongly-typed) <stronglytyp3d@gmail.com>
LABEL Description="Image for building and debugging arm-embedded projects from git"
WORKDIR /work

ADD . /work

ENV DEBIAN_FRONTEND noninteractive

# Install any needed packages specified in requirements.txt
RUN apt update && \
    apt upgrade -y && \
    apt install -y \
# Development files
      build-essential \
      git \
      bzip2 \
      libqt5widgets5 \
      unzip \
      wget \
      jq \
      awscli && \
      nano && \
      gcc-multilib && \
    apt clean && \
    wget https://launchpad.net/gcc-arm-embedded/4.9/4.9-2015-q3-update/+download/gcc-arm-none-eabi-4_9-2015q3-20150921-linux.tar.bz2 -O cortex_m.tar.bz2 && \
    tar -xjf cortex_m.tar.bz2 && \
    rm cortex_m.tar.bz2