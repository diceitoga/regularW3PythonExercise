#Exercise 10: Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn
#Expected input value: Sample value of n is 5
#Expected return value: Expected Result : 615

bt = int(input("Please enter a single digit integer: "))
transformed = bt*100+bt*10+bt+bt*10+bt+bt
print("Transformed data value: {}".format(transformed))