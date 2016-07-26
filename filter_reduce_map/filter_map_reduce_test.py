# filter, map and reduce are built in python functions
# filter enables you to extract all elements of a list that pass a truth test
# map applies a function to every element of a list
# reduce applies a function to a list, returning a specific value


import unittest
from filter_reduce_map import doubled_list

class TestNumbers(unittest.TestCase):

	def test_doubled_list(self):
		result = doubled_list([1, 2, 4, 5, 7, 8])
		self.assertEqual(result, [2, 4, 8, 10, 14, 16])

if __name__ == '__main__':
	unittest.main()
