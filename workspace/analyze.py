
import MDSplus
import numpy as np
from matplotlib import pyplot

tree = MDSplus.Tree('test', 0)

# Read the data from the tree
data = tree.SINE.DATA.data()

# Compute something
average = np.mean(data)

# Store it back in the tree
tree.AVERAGE.record = average

print('AVERAGE =', tree.AVERAGE.data())