import unittest
import re
from regular_expressions import identify_match

class TestRegularExpressions(unittest.TestCase):

	def test_find_match(self):
		result = identify_match("cats like to wear hats", "hats")
		self.assertEqual(result, True)

		result = identify_match("cats like to wear hats", "fish")
		self.assertEqual(result, False)

	


if __name__ == '__main__':
	unittest.main()