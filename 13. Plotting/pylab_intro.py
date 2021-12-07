#!/usr/local/bin python3

# Edited by ozervesh on Tue 7 Dec, 2:19pm. 
# I'm combining everything that's learnt across chapter 13 into this one file.

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

plt.figure("lin")
plt.title("Linear")
plt.xlabel("Sample points")
plt.ylabel("Linear function")
# format for graph plotting -> 
# plt.plot(x values, y values, "colourAndStyle:str", label="labelName:str", linewidth = "number:float")
plt.plot(mySamples, myLinear, "b-", label = "linear", linewidth = 4.0) # "b-" -> blue line
# indicate where the label legend should be shown in the graph
plt.legend(loc = "lower right")

# we do the same for the quadratic plot

plt.figure("quad")
plt.title("Quadratic")
plt.xlabel("Sample points")
plt.ylabel("Quadratic function")
plt.plot(mySamples, myQuadratic, "g^", label = "quadratic") # "g^" -> green triangle
# if no arguments are given for plt.legend(), pyplot will just decide
# which position is best for the legend on its own
plt.legend()

# the cubic and exponential graphs' shapes can still be observed
# accurately when overlapping with one another as they grow at closer rates
# (numerically speaking)

plt.figure("cub vs exp")
plt.title("Cubic vs. Exponential")
plt.xlabel("Sample points")
plt.ylabel("Cubic and exponential functions")
plt.plot(mySamples, myCubic, label = "cubic") # here, "colourAndStyle" is not indicated so it defaults
plt.plot(mySamples, myExponential, label = "exponential")
plt.legend(loc = "lower right")

# we can change the scale for graph axes. in this case, we'll change 
# the cubic vs exp graph such that it shows a log scale on the y axis
plt.figure("cub vs exp log")
plt.title("Cubic vs. Exponential (log scale)")
plt.xlabel("Sample points")
plt.ylabel("Cubic and exponential functions")
plt.plot(mySamples, myCubic, label = "cubic") # here, "colourAndStyle" is not indicated so it defaults
plt.plot(mySamples, myExponential, label = "exponential")
plt.yscale("log")
plt.legend(loc = "upper left")


# this is how it'd look like if we put all the graphs on the same axes.
# notice how the linear and quadratic graphs look really flat in this
# particular window.

plt.figure("bad graph")
plt.title("Bad Graph")
plt.xlabel("Sample points")
plt.ylabel("All functions")
plt.plot(mySamples, myLinear, "b-", label = "linear", linewidth = 2.0) # "b-" -> blue line
plt.plot(mySamples, myQuadratic, "g^", label = "quadratic", linewidth = 2.5) # "g^" -> green triangle
plt.plot(mySamples, myCubic, "ko", label = "cubic",linewidth = 3.0) # "ko" -> black circle
plt.plot(mySamples, myExponential, "r--", label = "exponential", linewidth = 3.5) # "r--" -> red dotted lines
plt.legend(loc = "upper left")

# we can also clear the figure, producing a clean window
# plt.clf()


# let's try to set much smaller limits on the axes on a copy of the
# bad graph. you'll notice that if you set a domain of x:[0,40] and
# y:[0,40], the shape of the linear graph will be apparent. the same can't
# be said for the other graphs, however.

plt.figure("bad graph 2")

plt.title("Bad Graph 2")
plt.plot(mySamples, myLinear)

plt.xlabel("Sample points")
plt.ylabel("All functions")
plt.xlim(0,40)
plt.ylim(0,40)
plt.plot(mySamples, myQuadratic)
plt.plot(mySamples, myCubic)
plt.plot(mySamples, myExponential)

# notice that legend doesn't work if you don't provide each
# graph plot with a label
plt.legend(loc = "upper left")

# let's try a copy of bad graph 2 but with a working legend and some subplots now

plt.figure("bad graph 3")
# don't put the figure title here otherwise it'll get overlapped by the
# subplots which will be generated later on
# plt.title("Bad Graph 3")


# Subplot 1: linear graph
plt.subplot(211) # plt.subplot(no. of rows and columns -> int)
plt.xlabel("Sample points")
plt.ylabel("Linear function")
plt.plot(mySamples, myLinear, label = "linear")

# Subplot 2: quadratic, cubic, and exponential graphs
plt.subplot(212) # args of diff subplots must be diff for the subplots to generate
plt.xlabel("Sample points")
plt.ylabel("Quad, cubic, and exp functions")
plt.plot(mySamples, myQuadratic, label = "quadratic")
plt.plot(mySamples, myCubic, label = "cubic")
plt.plot(mySamples, myExponential, label = "exponential")

# insert title after subplot generation, otherwise the title will get lost
plt.title("Bad Graph 3")


# display all figures
plt.show()
