import unittest
from lists import *

class TestLists(unittest.TestCase):

	def test_return_non_unique(self):
		result = return_non_unique(["a", "b", "c", "d", "a", "b", "e"])
		self.assertEqual(result, ["a", "b"])

	def test_palindrome_checker(self):
		result = palindrome_checker(["z", "a", "w", "a", "z"])
		self.assertEqual(result, True)

		result = palindrome_checker(["z", "g", "w", "a", "z"])
		self.assertEqual(result, False)

	def test_flatten_list(self):
		result = multiply_by_11_numbers_divisable_by_three([1, 2, 4, 9, 7, 12])
		self.assertEqual(result, [99, 132])

if __name__ == '__main__':
	unittest.main()