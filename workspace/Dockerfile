FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

RUN \
    apt update \
    # Packages needed to add the MDSplus repository key
    && apt-get -y install curl gnupg \
    # Add the MDSplus repository key
    && curl -fsSL http://www.mdsplus.org/dist/mdsplus.gpg.key | apt-key add - \
    # Add the MDSplus repository
    && echo 'deb http://www.mdsplus.org/dist/Ubuntu20/repo MDSplus alpha' > /etc/apt/sources.list.d/mdsplus.list \
    && apt update \
    # Install dependencies for MDSplus
    && apt install -y \
        libxml2 \
        libpython3.8 \
        python3-pip \
        python3-tk \
        default-jre \
        libmotif-common \
        libmotif-dev \
    # Install MDSplus
    && apt install -y \
        mdsplus-alpha-kernel \
        mdsplus-alpha-python \
        mdsplus-alpha-motif \
        mdsplus-alpha-java \
    && python3 -m pip install \
        matplotlib \
    # Fix MDSplus python installation
    && echo '/usr/local/mdsplus/python' > /usr/local/lib/python3.8/dist-packages/mdsplus.pth \
    && ldconfig

VOLUME /workspace
WORKDIR /workspace

# Configure MDSplus to load this version of python
ENV PyLib=/usr/lib/x86_64-linux-gnu/libpython3.8.so.1

ENTRYPOINT /bin/bash -c 'source /workspace/env.sh; bash'