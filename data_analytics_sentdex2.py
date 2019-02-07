#sentdex data analytics. 

import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

'''
simple line plot....you will be using pyplot all of the time. 
import matplotlib.pyplot as plt is always the convention
'''
#plt.plot(x,y)   when you plot, you plot [x,y] where both x =[] and y=[] with list of elements in each x and y to plot as coordinates. 

x = [1,2,3]
y = [5,7,4]
x2 = [1,2,3]        ##when you have more than 1 liniar graph as is this example, Leends become useful.
y2 = [10,14,12]
plt.plot(x,y, label="FirstLine")     #line plot, such that (1,5), (2,7), (3,4) should be the coordinates when plotted. 

plt.plot(x2,y2, label="SecondLine")
plt.xlabel('plot number')
plt.ylabel('y-axis')
plt.title('Interesting graph')
plt.legend()
plt.show()    ##the plot funciton will allow for plotting but will be running in the background. so you have to plt.show() to put it to display

########################
'''
when you are plotting you should have label, Legends and titles for graph
'''