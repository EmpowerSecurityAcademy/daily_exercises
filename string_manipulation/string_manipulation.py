#

# return a dictionary where the keys are each letter in the past in string
# and the values are the number of times the keys exists in the string
def character_counts(string):

	return_dict = {}

	for element in string:
		return_dict[element] = 0

	for key in return_dict:
		return_dict[key] = string.count(key)

	return return_dict

# this function will take a list of strings
# and will return one string that is made up
# of adding all of the other strings together
def combine_strings(strings):

	start = ""

	for element in strings:
		start += element

	return start

def break_into_sentence(string):

	