# create a set

# return the last three values in the tuple input
def access_tuple_values(tup_input):
	length = len(tup_input)
	return tup_input[(length - 3):(length)]


def add_value_to_tuple(tup_input, value):
	return tup_input + (value, )

