#Ex16. Write a Python program to get the difference between a given number and 17, 
#if the number is greater than 17 return double the 
#absolute difference.

print("I will give you the difference in the number you input and 17, if the number is greater than 17, return double the absolute difference")
num_input = int(input("Please enter a number: " ))

absolute_diff = abs(num_input -17)


if absolute_diff>17:
	print("doubled absolute diff due to being over 17")
	double_diff = 2*absolute_diff
	print(double_diff)
else: 
	print("Here is the absolute difference between {} and 17".format(num_input))
	print(absolute_diff)
