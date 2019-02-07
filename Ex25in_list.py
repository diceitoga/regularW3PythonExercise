#Ex25: Write a Python program to check whether a specified value is contained in a group of values.
#in 

def value_in_list(some_value):
	bool_value = False
	list_values = [3,4,5,6,9,10,11]
	if some_value in list_values:
		bool_value = True

	return bool_value

bool_val1 = value_in_list(6)
print(bool_val1)
bool_val2 = value_in_list(8)
print(bool_val2)
