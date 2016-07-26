# filter, map and reduce are built in python functions
# filter enables you to extract all elements of a list that pass a truth test
# map applies a function to every element of a list
# reduce applies a function to a list, returning a specific value

def multiply_by_two(value):
	return value * 2

#write a function that uses map, and multiply_by_two to double all numbers in a list
def doubled_list(numbers):
	return map(multiply_by_two, numbers)

