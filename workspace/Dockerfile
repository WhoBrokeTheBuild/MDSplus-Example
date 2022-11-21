FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

RUN \
    apt update \
    && apt-get -y install curl gnupg \
    && curl -fsSL http://www.mdsplus.org/dist/mdsplus.gpg.key | apt-key add - \
    && echo 'deb http://www.mdsplus.org/dist/Ubuntu20/repo MDSplus alpha' > /etc/apt/sources.list.d/mdsplus.list \
    && apt update \
    && apt install -y \
        libxml2 \
        libpython3.8 \
        python3-pip \
        python3-tk \
        default-jre \
        libmotif-common \
        libmotif-dev \
    && apt install -y \
        mdsplus-alpha-kernel \
        mdsplus-alpha-python \
        mdsplus-alpha-motif \
        mdsplus-alpha-java \
    && python3 -m pip install \
        matplotlib \
    && echo '/usr/local/mdsplus/python' > /usr/local/lib/python3.8/dist-packages/mdsplus.pth \
    && ldconfig

VOLUME /workspace
WORKDIR /workspace

ENV test_path=/workspace/trees
ENV PyLib=/usr/lib/x86_64-linux-gnu/libpython3.8.so.1

ENTRYPOINT /bin/bash -c 'source /usr/local/mdsplus/setup.sh; bash'