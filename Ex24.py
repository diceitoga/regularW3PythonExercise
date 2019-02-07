#24 Vowel:  Write a Python program to test whether a passed letter is a vowel or not

def check_vowel(some_letter):
	vowel_list = ['a','i','u','e','o']

	if some_letter.lower() in vowel_list:
		return "vowel"
	else: 
		return "not vowel"

answer_vowel = check_vowel('a')
print(answer_vowel)
answer_vowel2 = check_vowel('x')
print(answer_vowel2)
answer_vowel3 = check_vowel('A')
print(answer_vowel3)