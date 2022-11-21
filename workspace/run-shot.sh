#!/bin/bash

export MDS_PYDEVICE_PATH=/workspace/pydevices

mdstcl <<EOF
set tree test /shot=-1
set current test /inc
create pulse 0
show current test
set tree test /shot=0
do /method sine init
EOF