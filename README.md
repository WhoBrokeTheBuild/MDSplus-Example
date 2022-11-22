
# MDSplus Example

A simple MDSplus data collection example, using a device class that generates a simple sine wave.

## 0. Clone this repo

Clone the repo and change into the directory.

## 1. Install MDSplus

### Option A: Using Docker (Recommended)

Docker is not an important part of the job, but it was an easy way to get an example up and running to see MDSplus in action.

Step #1 must be run on a linux system with docker installed. If you don't have a linux system, I recommend creating a virtual machine. If you don't have docker installed, you can follow these instructions: https://docs.docker.com/engine/install/

If you were interested, you could run all of the commands found in `workspace/Dockerfile` on an Ubuntu 20.04 system, and you would get a working MDSplus installation.

I encourage you to read any and all code snippits in this repo and save your questions to ask during the interview. However, I wouldn't focus too much on the `Dockerfile` or `shell.sh`, those are just to get an environment running.

This will build and start a docker container that will allow you to try out MDSplus without installing anything on your system.

```
$ ./shell.sh
```

The `workspace/` directory in this repo will be mounted as `/workspace/` in the container, and all scripts and data will be accessible in both your host system and the container.

*Note:* Tree files created from docker will be owned by root.

### Option B: Using a standard installation

If you want to run MDSplus the standard way, you will need to install it on your system. You can find the instructions here: https://mdsplus.org/index.php/Downloads
*Note:* This example is not compatible with Windows, if you have a Windows system I recommend making a Linux Virtual Machine.

Once you have MDSplus installed, navigate to the `workspace/` folder within this repo and run:
*Note:* You may have to adjust PyLib to point at your python version.

```
$ source env.sh
$ export PyLib=python3.8
```

This will configure that terminal with the right environment variables to run the other scripts and try out MDSplus.

## 2. Create the tree model.

*Note:* Running this again will delete the existing tree and all modifications to it.

In order to run this and all following steps, you will need to have done Step #0.

This will generate a model for our tree, which is used as the template for each "shot" as described below.

A SineWave device will be added to the tree, which will generate our data to play with.

```
root@abcd1234:/workspace# ./build-tree.sh
```

## 3. Run a "shot" to collect some data.

A "shot" is how we refer to a single data capture. Each shot gets a number to refer to it. The special number -1 refers to the "model shot", which is the template used when creating new shots. The special number 0 refers to the "current shot".

This script will generate a new shot number, assign it as the "current shot", and run a data capture using the SineWave device. The SineWave device will use the settings stored in the model, and then record a copy of the settings used alongside the data.

Additionally, this script will call `workspace/analyze.py` after each data capture which calculates an average of the data and stores it in the `AVERAGE` node in the tree.

Shot files will be located in `workspace/trees/` and can be accessed using the tools described below.

```
root@abcd1234:/workspace# ./run-shot.sh
```

## 4. Analyze the data.

This can be done using any of the MDSplus tools, here are some examples:

**python**

This example has a python script `workspace/analyze.py` that gets called by `run-shot.sh` after every data capture. You can use this as a testbed to play with the data.

**jScope**

MDSplus comes with built-in scope tools that know how to read data from shots. There is an example scope configuration file in `workspace/scopes/`.

```
root@abcd1234:/workspace# jScope -def scopes/test.jscp &
```

**matplotlib**

With the MDsplus python API and matplotlib, you can easily work with and view the data.

```
root@abcd1234:/workspace# python3 plot.py
```

## 4. Experiment!

Edit the values `FREQUENCY`, `AMPLITUDE`, `LENGTH` and `SAMPLE_RATE`, then run a new shot and see the effects on the data.

**jTraverser**
MDSplus comes with additional graphical tools to help with viewing / modifying the tree files. jTraverser allows you to view the 
tree as a proper hierarchy, and view/modify values. You can use this to edit the values mentioned above.

```
root@abcd1234:/workspace# jTraverser test -1 &
```

Once you've edited a value in the model, go back to Step #3 and collect more data.
