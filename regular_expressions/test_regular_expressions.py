import unittest
import re
from regular_expressions import identify_match, identify_dates

class TestRegularExpressions(unittest.TestCase):

	def test_find_match(self):
		result = identify_match("cats like to wear hats", "hats")
		self.assertEqual(result, True)

		result = identify_match("cats like to wear hats", "fish")
		self.assertEqual(result, False)

	def test_identify_dates(self):
		result = identify_dates("On August 11 I will ride to Arlington, on November 15 I will write a poem")
		self.assertEqual(result, ['August 11', 'November 15'])

	

if __name__ == '__main__':
	unittest.main()