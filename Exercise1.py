
import pandas
import numpy

'''
Input:  a text read in
Expected output:
Twinkle, twinkle, little star,
	How I wonder what you are!
		Up above the world so high,
		Like a diamond in the sky.
Twinkle, twinkle, little star,
	How I wonder what you are
'''

twinkle_obj = open("Twinkle1.txt", "r+")
#print(twinkle_obj.read())
special_char=(',','!','.')

twinkle_obj_list = twinkle_obj.read().split(' ')
#print(twinkle_obj_list)
empty_list = []
for element in twinkle_obj_list: 
	#print(element)		#new character line
	if element[0].isupper():
		if element == "I":
			#print(element)
			empty_list.append(element)
		else:
			#print("\n")
			empty_list.append("\n")
			#print(element)
			empty_list.append(element)
	else:
		#print(element)
		empty_list.append(element)

print(empty_list)

twinkle_obj.close()





