import unittest
from string_manipulation import *

class TestStringManipulation(unittest.TestCase):

	def test_character_counts(self):

		result = character_counts("all of the things are different and yet all of the same")
		self.assertEqual(result, {'a': 5, ' ': 11, 'e': 7, 'd': 2, 'g': 1, 'f': 4, 'i': 2, 'h': 3, 'm': 1, 'l': 4, 'm': 1, 'n': 3, 'o': 2, 'r': 2, 's': 2, 't': 5, 'y':1})

		result = character_counts("this string will result in a different dictionary when passed into charachter counts")
		self.assertEqual(result, {'a': 5, ' ': 12, 'c': 4, 'e': 6, 'd': 3, 'g': 1, 'f': 2, 'i': 8, 'h': 4, 'l': 3, 'o': 3, 'n': 7, 'p': 1, 's': 6, 'r': 6, 'u': 2, 't': 8, 'w': 2, 'y': 1})

	def test_combine_strings(self):

		string_list = ["I think ", "that I will have a good time ", "writing code today ", "I will learn a lot"]

		result = combine_strings(string_list)
		self.assertEqual(result, "I think that I will have a good time writing code today I will learn a lot")

if __name__ == '__main__':
	unittest.main()