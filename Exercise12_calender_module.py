#Exercise 12: Write a Python program to print the calendar of a given month and year.
#Note : Use 'calendar' module.
#Utilized this video from youtube as a good reference (about 1:08): https://www.youtube.com/watch?v=e0Pys7H-sjM

import calendar
print("test")

year = int(input("Please type in a year: "))
month = int(input("Please type in a month: "))

#now use the built in function and pass these paramenters to get the value

value = calendar.month(year,month)
print(value)