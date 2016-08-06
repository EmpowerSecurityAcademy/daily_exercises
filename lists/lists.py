import types


# return elements of a list
# if there are more than one of that element in the list
def return_non_unique(list_characters):
	counts = {}
	for character in list_characters:
		if character in counts:
			counts[character] += 1
		else:
			counts[character] = 1
	non_unique_keys = []
	for key, value in counts.items():
		if value != 1:
			non_unique_keys.append(key)
	return non_unique_keys


	
def return_non_unique(list_charachters):







# return True if the list is a palindrome ex. ["x", "a", "m", "a", "x"]
# return False if the list is not a palindrome ex. ["x", "a", "m", "a", "x", "b"]
def palindrome_checker(possible_palindrome):








# take a nested array, and flatten into one array
# [a, [b, [c, d], e]]
# [a, b, c, d, e]
# use recursion
def flatten_list(nested_array):





