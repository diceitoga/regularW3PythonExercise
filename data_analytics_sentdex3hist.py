#Video 3 of data analytics with Sentdex using histogram and bar charts. 
'''
histogram is meant to show distribution

'''

import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

'''
simple histogram plot....you will be using pyplot to show distribution, such is the case w histogram. 
import matplotlib.pyplot as plt is always the convention
'''
#plt.plot(x,y)   when you plot, you plot [x,y] where both x =[] and y=[] with list of elements in each x and y to plot as coordinates. 
#you have to make the color different so that x and x2, y and y2 are different and visible
#histogram has concept of 'bins'

population_ages = [1,3,12,68,37,24,24,13,3,98,87,64,12,5,6,29,34,56,63,30,32,29,100,44,45,50,39,11,3,5,21,24,3,7,101,77,60,80,3,5,4,7,100]
#ids = [x for x in range(len(population_ages))]
bins = [0,10,20,30,40,50,60,70,80,90,100,110]    #elements that are broken up in buckes 
plt.hist(population_ages, bins, histtype='bar', rwidth=0.8)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting graph')
#plt.legend()
plt.show()    ##the plot funciton will allow for plotting but will be running in the background. so you have to plt.show() to put it to display

########################
'''
when you are plotting you should have label, Legends and titles for graph
'''