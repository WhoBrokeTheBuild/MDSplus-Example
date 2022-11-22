#!/bin/bash

# Create a new tree named `test`
# Add a node named SINE that is a SineWave device
# Add a node named AVERAGE that will store a number
# Write the tree to disk
# Close the tree
mdstcl <<EOF
edit test /new
add node SINE /model=SineWave
add node AVERAGE /usage=numeric
write
close
EOF

# Open our new tree
# Print a listing of nodes
# Print a listing of open trees / shot numbers
mdstcl <<EOF
set tree test
dir
show db
EOF