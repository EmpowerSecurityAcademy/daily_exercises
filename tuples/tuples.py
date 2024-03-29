# create a set

# return the last three values in the tuple input
def access_tuple_values(tup_input):
	length = len(tup_input)
	return tup_input[(length - 3):(length)]


def add_value_to_tuple(tup_input, value):
	return tup_input + (value, )

# write a function that iterates through a list
# checks whether the element exists in a tuple
# put the result of the check into an array
# return that array
def boolean_exists(tup_input, list_input):

	return_array = []

	for element in list_input:
		response = element in tup_input
		return_array.append(response)

	return return_array