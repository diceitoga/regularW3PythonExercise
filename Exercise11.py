#Exercise 11: Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).
#Example: abs()

value_example = int(input("Input any number from 1 ~ 10 and I will print the absolute value: "))

print(abs(value_example))

print("Input any two values (where first is larger than second) and I will mod it")
first_value = int(input("input first value: "))
second_value = int(input("input second value: "))
ans = first_value%second_value
print(ans)