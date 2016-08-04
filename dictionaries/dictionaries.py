# dictionaries are a powerful and flexible python data structure



# this function will take a list of dictionaries
# each of these dictionaries will have one key value pair
# instantiate a dictionary that will be returned from the function
# copy each key value pair from the list of dictionaries to the newly instantiated dictionary
# input: [{"name": "billy"}, {"hometown", "Salt Lake City"}, {"eye_color", "blue"}]
# output: {"name": "billy", "hometown": "Salt Lake City", "eye_color": "blue"}
def construct_dictionary(dictionary_list):
	return_value = {}

	for element in dictionary_list:
		print(element)
		for key, value in element.items():
			return_value[key] = value

	return return_value

# this function is the opposite of the above function
# we will take in a dictionary, and unpack it into a list
# of key value pairs
def unpack_dictionary(packed_dictionary):
	return_value = []

	for key, value in packed_dictionary.items():
		dict_element = {}
		dict_element[key] = value
		return_value.append(dict_element)

	return return_value
