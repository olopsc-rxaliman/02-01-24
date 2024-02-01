# ROVIC XAVIER A. ALIMAN
# BSCS-2
# FEBRUARY 1, 2024

# Python program to demonstrate the 'map' function and decorators


# DECORATOR
def include_only_alphabet_characters_then_lowercase(func):

	def wrapper(*args):

		strings = func(*args)

		return ''.join(map(lambda s: s.lower() if s.isalpha() or s.isdigit() else '', strings))

	return wrapper


# REVERSE THE STRING W/ DECORATOR APPLIED
@include_only_alphabet_characters_then_lowercase
def reverse_string(string):

	return string[::-1]


# RETURN STRING W/ DECORATOR APPLIED
@include_only_alphabet_characters_then_lowercase
def return_string_with_no_spaces(string):

	return string


# CHECKS IF STRING IS THE SAME FOR REVERSE AND ORIGINAL
def is_palindrome(string):

	modified_string = reverse_string(string)

	if modified_string == return_string_with_no_spaces(string):
		return True

	else:
		return False


# GET USER INPUT
string = input('Enter a palindrome: ')


# DETERMINE IF STRING IS PALINDROME OR NOT
if is_palindrome(string):
	print(f'"{string}" is a palindrome!')

else:
	print(f'"{string}" is not a palindrome...')


input('\nPress ENTER key to exit this program')