'''
prompt the user to enter an integer that the computer return in a reverse form and print
prompt the computer to return true if the number is a palindrome and save
prompt the user to input the reverse function to implement ispalindrome and save.
print the result and save
'''

def is_palindrome(number):

 number = 0

 user_input = int(input("Enter a number:"))

 return "it's a palindrome" if str(number) == str(number)[::-1] else "print it's not a palindrome"

print(is_palindrome(4567))


def reverse_string(word):
	reverse_word = ''
	for number in range(len(word)-1, -1, -1):
		reverse_word += word[number]

	return reverse_word


def palindrome(number):
	return str(number) == reverse_string(str(number))

print(palindrome("hannah"))