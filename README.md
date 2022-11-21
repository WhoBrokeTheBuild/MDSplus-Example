
# MDSplus Example

A simple MDSplus data collection example, using a device class that generates a simple sine wave.

## 1. Start the docker shell to use the MDSplus tools.

This will mount the `workspace/` directory as `/workspace/`, and all scripts and data will live in that directory.

```
$ ./shell.sh
```

## 2. Once there, you need to create the tree files.

*Note:* Running this again will delete the existing tree and all modifications to it.

This will add a SineWave device to the tree, which will generate our data to play with.

```
root@abcd1234:/workspace# ./build-tree.sh
```

## 3. Run a "shot" to collect some data.

A "shot" is how we refer to a single data capture. Each shot gets a number to refer to it. The special number -1 refers to the "model shot", which is the template used when creating new shots. The special number 0 refers to the "current shot".

This script will generate a new shot number, assign it as the "current shot", and run a data capture using the SineWave device. The SineWave device will use the settings stored in the model, and then record a copy of the settings used alongside the data.

Shot files will be located in `/workspace/trees/` and can be accessed using the tools described below.

```
root@abcd1234:/workspace# ./run-shot.sh
```

## 4. Analyze the data.

This can be done using any of the MDSplus tools, here are some examples:

**jScope**
MDSplus comes with built-in scope tools that know how to read data from shots. There is an example scope configuration file in `/workspace/scopes/`.

```
root@abcd1234:/workspace# jScope -def scopes/test.jscp &
```

**matplotlib**
With the MDsplus python API and matplotlib, you can easily work with and view the datra.
```
root@abcd1234:/workspace# python3 plot.py
```

## 5. Experiment!

Edit the values `FREQUENCY`, `AMPLITUDE`, `LENGTH` and `SAMPLE_RATE`, then run a new shot and see the effects on the data.

**jTraverser**
MDSplus comes with additional graphical tools to help with viewing / modifying the tree files. jTraverser allows you to view the 
tree as a proper hierarchy, and view/modify values. You can use this to edit the values mentioned above.

```
root@abcd1234:/workspace# jTraverser test -1 &
```

Once you've editied a value in the model, go back to Step #3 and collect more data.