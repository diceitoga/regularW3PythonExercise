#Exercise 6 Python List to tuple using tuple(list)  via type casting

userinput_tuple =[]

while True: 
	data_provided =  input("Please enter a value/integer to be added to a Truple: ")
	userinput_tuple.append(data_provided)
	yes_no = input("do you have anymore to add type 'y' for yes and 'n' for no(y/n): ")
	if yes_no =='n':
		break
	else:
		continue

print("list: {}".format(userinput_tuple))
print(type(userinput_tuple))
userinput_tuple=tuple(userinput_tuple)
print("truple: {}".format(userinput_tuple))
print(type(userinput_tuple))

