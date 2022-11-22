#!/bin/bash

# Open the tree model
# Increment the current shot number, or set it to 1 if there is none
# Create a copy of the model, identified by the current shot number
# Show the current shot number
# Open the newly created shot
# Run the SineWave device
mdstcl <<EOF
set tree test /shot=-1
set current test /inc
create pulse 0
show current test
set tree test /shot=0
do /method sine init
EOF

# Run post-shot analysis code
python3 analyze.py
