# filter, map and reduce are built in python functions
# filter enables you to extract all elements of a list that pass a truth test
# map applies a function to every element of a list
# reduce applies a function to a list, returning a specific value

def multiply_by_two(value):
	return value * 2

#write a function that uses map, and multiply_by_two to double all numbers in a list
def doubled_list(numbers):
	return map(multiply_by_two, numbers)




#write a function that removes all letter "a" from a word
def strip_a_from_word(word):
	return word.replace("a","")



#write a function that splits a sentence into words
#remove all letter "a" from word
# do this using map and strip_a_from_word
def split_sentence_remove_a(sentence):
	split_words = sentence.split(" ")
	sample = map(strip_a_from_word, split_words)
	return sample


def divisable_by_5(number):
	if number % 5 == 0:
		return True
	else:
		return False

# use the filter function and divisable_by_5
# to return numbers in the list that are divisable by 5
def filter_divisable_by_five(numbers):
	return filter(divisable_by_5, numbers)


# write a function that returns True if a word contains "ing"
# the function should return False if it does not
def contains_ing(word):
	if "ing" in word:
		return True
	else:
		return False


# write a function that uses filter and contains_ing
# to return all words in a sentence that contain ing
# they should be returned as an array of strings
def filter_contains_ing(sentence):
	splitter = sentence.split(" ")
	return filter(contains_ing, splitter)
	







