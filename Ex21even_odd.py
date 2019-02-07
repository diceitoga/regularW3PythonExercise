#Ex21. Write a Python program to find whether a given number (accept from the user) is even or odd, 
#print out an appropriate message to the user.

def even_odd(num):
	even_odd = ''
	if num%2==0:
		even_odd = 'even'
	else:
		even_odd = 'odd'
	return even_odd

what_isit =even_odd(int(input("Please enter an integer between 1-100 and I will tell you if even or odd: ")))
print(what_isit)
