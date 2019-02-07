#ex23: Write a Python program to get the n (non-negative integer) copies of the first 2 
#characters of a given string. Return the n copies of the whole string if the length is less than 2.
#print('test')

def string_first2(some_string, copies):
	firstchar = some_string[0]
	secondchar = some_string[1]
	firstchar_xcopies = firstchar*copies
	secondchar_xcopies = secondchar*copies
	return_char = firstchar_xcopies + secondchar_xcopies
	return return_char
###################################################
return_value1 = string_first2("happiness", 4)
print(return_value1)
return_value2 = string_first2("enlightenment",5)
print(return_value2) 
