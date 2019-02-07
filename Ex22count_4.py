#ex 22: Write a Python program to count the number 4 in a given list.

def count_4(some_list):
	count=0
	for element in some_list:
		if element==4:
			count+=1
	return count

value_1 = count_4([5,4,3,2,6,7,4])
print(value_1)
value_2 = count_4([2,2,5,4,6,8,8,20,4,3,2,4])
print(value_2)
