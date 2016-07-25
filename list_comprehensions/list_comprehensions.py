# list comprehensions follow the format
# [dosomething(num) for num in array if some_condition_is_true]


# use a list comprehension to return only even numbers
def even_numbers(array_numbers):
	return [num for num in array_numbers if num % 2 == 0]

# use list comprehension to return words starting with the letter "a"
def start_with_a(array_strings):
	return [s_str for s_str in array_strings if s_str[0] == 'a']

def multiply_by_11_numbers_divisable_by_three(array_numbers):
	return [num*11 for num in array_numbers if num % 3 == 0]

