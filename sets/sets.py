# create a set
# set("my name is Eric and Eric is my name".split())

# use .split(" ") to split the input, and return it as a set
def create_set_from_sentence(sentence):
	split_sentence = sentence.split(" ")
	return set(split_sentence)

# find the unique elements of two lists that exist in both lists
# convert them to sets and then use the set intersection function
# return elements as a list
def intersection_two_sets(list_a, list_b):

	set_a = set(list_a)
	set_b = set(list_b)
	return list(set_a.intersection(set_b))

# find elements that are unique to one of the lists
# a.symmetric_difference(b)

# find all elements unique to a set
# a.difference(b)

# return one of each elements
# a.union(b)