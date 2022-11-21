#!/bin/bash

export MDS_PYDEVICE_PATH=/workspace/pydevices

mdstcl <<EOF
edit test /new
add node sine /model=sinewave
write
close
EOF