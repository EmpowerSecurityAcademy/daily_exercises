import types


# return elements of a list
# if there are more than one of that element in the list
def return_non_unique(list_charachters):
	counts = {}
	for charachter in list_charachters:
		if charachter in counts:
			counts[charachter] += 1
		else:
			counts[charachter] = 1
	non_unique_keys = []
	for key, value in counts.items():
		if value != 1:
			non_unique_keys.append(key)
	return non_unique_keys


# return True if the list is a palindrome ex. ["x", "a", "m", "a", "x"]
# return False if the list is not a palindrome ex. ["x", "a", "m", "a", "x", "b"]
def palindrome_checker(possible_palindrome):
	string_length = len(possible_palindrome)
	for i, charachter in enumerate(possible_palindrome):
		if possible_palindrome[(string_length - i - 1)] != charachter:
			return False

	return True



# take a nested array, and flatten into one array
# [a, [b, [c, d], e]]
# [a, b, c, d, e]
# use recursion
def flatten_list(nested_array):
	value = [val for sublist in nested_array for val in sublist]
	return value




