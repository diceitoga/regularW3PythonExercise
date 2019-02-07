#Exercise 7: 

filename = input("Please type in a filename, and make sure to include file extention followed by <filename>.extension. \n For example; example.txt: ")

filename = filename.split(".")
print("File type: {}".format(filename[1]))
