#sentdex data analytics. 

import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

'''
simple line plot....you will be using pyplot all of the time. 
import matplotlib.pyplot as plt is always the convention
'''
#plt.plot(x,y)   when you plot, you plot [x,y] where both x =[] and y=[] with list of elements in each x and y to plot as coordinates. 

plt.plot([1,2,3],[5,7,4])
plt.show()    ##the plot funciton will allow for plotting but will be running in the background. so you have to plt.show() to put it to display

########################
'''
when you are plotting you should have label, Legends and titles for graph