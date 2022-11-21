#!/bin/bash

docker build workspace -t mdsplus-example

xhost +local:docker
xhost +local:root

docker run --rm -it \
    --network=bridge \
    --volume=$PWD/workspace:/workspace \
    --env=DISPLAY \
    --env=QT_X11_NO_MITSHM=1 \
    --volume=/tmp/.X11-unix:/tmp/.X11-unix:rw \
    --volume="$HOME/.Xauthority:/root/.Xauthority:rw" \
    mdsplus-example