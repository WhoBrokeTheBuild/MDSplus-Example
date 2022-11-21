
import MDSplus
from matplotlib import pyplot

tree = MDSplus.Tree('test', 0)
data = tree.SINE.DATA.data()
times = tree.SINE.DATA.dim_of()

pyplot.plot(times, data)
pyplot.show()