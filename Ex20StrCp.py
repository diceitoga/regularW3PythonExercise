#Ex 20: Write a Python program to get a string which is n (non-negative integer) copies of a given string


def string_times_n(some_string, n):
	print("You entered {} copies as desired value".format(n))
	print(some_string*3)

print("Enter a string")
string_entered = input("Here:")
num_copies = int(input("How many copies?: "))
string_times_n(string_entered, num_copies)

