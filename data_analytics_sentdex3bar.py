#Video 3 of data analytics with Sentdex using histogram and bar charts. 
'''
histogram is meant to show distribution

'''

import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

'''
simple line plot....you will be using pyplot all of the time. 
import matplotlib.pyplot as plt is always the convention
'''
#plt.plot(x,y)   when you plot, you plot [x,y] where both x =[] and y=[] with list of elements in each x and y to plot as coordinates. 
#you have to make the color different so that x and x2, y and y2 are different and visible
x = [2,4,6,8,10]
y = [6,7,8,2,4]
x2 = [1,3,5,7,9]
y2 = [7,8,2,4,2]


plt.bar(x,y, label='Bars1', color='c')   ##this is for bar chart by plot.bar()
plt.bar(x2,y2, label='Bars2', color='b')
plt.title('Interesting graph')
plt.legend()
plt.show()    ##the plot funciton will allow for plotting but will be running in the background. so you have to plt.show() to put it to display

########################
'''
when you are plotting you should have label, Legends and titles for graph
'''