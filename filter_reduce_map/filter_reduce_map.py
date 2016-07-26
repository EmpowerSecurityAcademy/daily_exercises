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
	return word.replace("a", "")

#write a function that splits a sentence into words
#remove all letter "a" from word
# do this using map and strip_a_from_word
def split_sentence_remove_a(sentence):
	split_sentence = sentence.split(" ")
	return map(split_sentence, strip_a_from_word)
