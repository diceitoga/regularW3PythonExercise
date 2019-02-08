'''
29. Write a Python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2. Go to the editor
Test Data :
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
Expected Output :
{'Black', 'White'}
''' 

from operator import sub


def print_color(somelist1, somelist2):
	agg_list=somelist1|somelist2     ##this is union
	print(agg_list)
	return agg_list


color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
#color_list_1 = ["White", "Black", "Red"]
#color_list_2 = ["Red", "Green"]

agg_listf = print_color(color_list_2, color_list_1)
print(agg_listf.difference(color_list_2))

#print_color(color_list_1, color_list_2)
