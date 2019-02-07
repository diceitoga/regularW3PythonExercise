#Ex 27: Write a Python program to concatenate all elements in a list into a string and return it.

def concat_tostring(some_list):
	mod_string = ''
	print(some_list)
	for element in some_list:
		mod_string +=element

	return mod_string



sample_list = ['Here ', 'is ', 'a ', 'sentence ', 'for ', 'ya ']

string_value = concat_tostring(sample_list)
print(string_value)