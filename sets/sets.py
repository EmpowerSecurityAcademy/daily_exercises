# create a set
# set("my name is Eric and Eric is my name".split())

# use .split(" ") to split the input, and return it as a set
def create_set_from_sentence(sentence):
	split_sentence = sentence.split(" ")
	return set(split_sentence)

# find the interection of two sets
# a.intersection(b)

# find elements that are unique to one of the lists
# a.symmetric_difference(b)

# find all elements unique to a set
# a.difference(b)

# return one of each elements
# a.union(b)