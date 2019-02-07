#Exercise 17 Write a Python program to test whether a number is within 100 of 1000 or 2000.

var1 = 1000
var2 = 2000
close_v1 = False
close_v2 = False
#############################################################################
input_data = int(input("Please enter a positive integer: "))

if abs(var1-input_data)<100:
	close_v1 = True
if abs(var2-input_data)<100:
	close_v2 = True
if close_v1 ==True or close_v2 == True:
	print("The value is with in 100 of the two values tested")
else: 
	print("The valus is out of the 100 range.")
	print("actual value: {}".format(input_data))
