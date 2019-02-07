#Ex18. Write a Python program to calculate the sum of three given numbers, 
#if the values are equal then return thrice of their sum
import math

val_list = []
print("Please enter three integers: ")
val_1 = int(input("Enter int for num1: "))
val_2 = int(input("Enter int for num2: "))
val_3 = int(input("Enter int for num3: "))
val_list.append(val_1)
val_list.append(val_2)
val_list.append(val_3)
print(val_list)
if val_1 == val_2 == val_3:
	print("tripling the sum of three since equal val...")
	print(sum(val_list)*3)
else:
	sum_three=sum(val_list)
	print("The sum of three numbers are: {}".format(sum_three))