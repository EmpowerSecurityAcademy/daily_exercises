# include items, range
# case statements
# break, continue

# this function takes two inputs, a begining value and an ending value
# use the range function to populate a list with the values in between 
# the begining and ending values
def create_list_of_range(begin, end):
	return_value = []

	for num in range(begin, end):
		return_value.append(num)

	return_value.append(end)

	return return_value

