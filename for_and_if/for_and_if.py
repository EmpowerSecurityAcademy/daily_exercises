

def if_divisable_by_three(lst):

	return_array = []

	for element in lst:
		if element % 3 == 0:
			return_array.append(element)

	return return_array

def if_element_length_is_7_or_more(lst):

	return_array = []

	for element in lst:
		if len(element) >= 7:
			return_array.append(element)

	return return_array




