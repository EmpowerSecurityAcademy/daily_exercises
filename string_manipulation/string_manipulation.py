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


def combine_strings(strings):