#Ex 19: Write a Python program to get a new string from a given string where "Is" has been added to the front.
#If the given string already begins with "Is" then return the string unchanged

print("test")

sentence_string = input("Please enter a short sentence and I will add something: ")
first_l = sentence_string.split(' ')
if first_l[0] == 'Is':
	print(sentence_string)
else: 
	print("Is " + sentence_string)
