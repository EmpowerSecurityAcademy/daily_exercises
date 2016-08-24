



def construct_zoo(dictionary_list):
	return_value = {}

	for element in dictionary_list:
		for key, value in element.items():
			return_value[key] = value

	return return_value

def extract_characters(list_strings):

	return_value = []

	for word in list_strings:
		for character in word:
			return_value.append(character)

	return return_value


def is_int_or_string(mystery):
	if isinstance(mystery, int):
		return "int"
	else:
		return "string"


# use a list comprehension!!!
def even_numbers(array_numbers):
	return [num for num in array_numbers if num % 2 == 0]




