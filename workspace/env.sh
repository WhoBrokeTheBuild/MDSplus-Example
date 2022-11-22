
source /usr/local/mdsplus/setup.sh

WORKSPACE=$(realpath $(dirname "${BASH_SOURCE[0]}"))

# Configure MDSplus to look for / store our `test` tree files here
export test_path=$WORKSPACE/trees

# Configure MDSplus to look for our new python device here
export MDS_PYDEVICE_PATH=$WORKSPACE/pydevices
