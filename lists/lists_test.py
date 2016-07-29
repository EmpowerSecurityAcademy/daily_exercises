import unittest
from lists import *

class TestLists(unittest.TestCase):

	def test_remove_more_than_two(self):
		result = even_numbers([1, 2, 4, 5, 7, 8])
		self.assertEqual(result, [2, 4, 8])

	def test_palindrome_checker(self):
		result = start_with_a(["apple", "orange", "carrot"])
		self.assertEqual(result, ["apple"])

	def test_flatten_list(self):
		result = multiply_by_11_numbers_divisable_by_three([1, 2, 4, 9, 7, 12])
		self.assertEqual(result, [99, 132])

if __name__ == '__main__':
	unittest.main()