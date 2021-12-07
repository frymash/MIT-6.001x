#!/usr/local/bin python3

# Edited by ozervesh on Tue 7 Dec, 2:19pm

# it's actually regarded as bad practice to use pylab 
# (see https://matplotlib.org/stable/api/index.html).
# instead of import pylab as plt, use import matplotlib.pyplot as plt instead

import matplotlib.pyplot as plt
from icecream import ic
mySamples = []
myLinear = []
myQuadratic = []
myCubic = []
myExponential = []

for i in range(30):
    mySamples.append(i)
    myLinear.append(i)
    myQuadratic.append(i**2)
    myCubic.append(i**3)
    myExponential.append(1.5**i)

ic(
    mySamples,
    myLinear,
    myQuadratic,
    myCubic,
    myExponential
)

# some graphs will look like flat lines if they're plotted on the same axes
# as the cubic and exponential graphs due to the differences in their rates
# of growth.

# for instance, the linear graph grows at a significantly slower as compared
# to the quadratic, cubic, and exponential graphs. to observe the shape of the
# linear graph accurately, we need the axes to be on a smaller scale as
# compared to the other graphs.

# as such, we use plt.figure() to isolate the linear plot.
# the axes can be labelled with plt.xlabel() and plt.ylabel()

plt.figure("Linear")
plt.plot(mySamples, myLinear)

# we do the same for the quadratic plot

plt.figure("Quadratic")
plt.plot(mySamples, myQuadratic)

# the cubic and exponential graphs' shapes can still be observed
# accurately when overlapping with one another as they grow at closer rates
# (numerically speaking)

plt.figure("Cubic and Exponential")
plt.plot(mySamples, myCubic)
plt.plot(mySamples, myExponential)

# this is how it'd look like if we put all the graphs on the same axes.
# notice how the linear and quadratic graphs look really flat in this
# particular window.

plt.figure("Bad graph")
plt.plot(mySamples, myLinear)
plt.plot(mySamples, myQuadratic)
plt.plot(mySamples, myCubic)
plt.plot(mySamples, myExponential)

# display figures
plt.show()
