import unittest
from numbers import *

class TestNumbers(unittest.TestCase):

	def test_sum_3_5_multiples(self):
		result = sum_3_5_multiples(155)
		self.assertEqual(result, 11110)


	def test_sum_fibonacci_numbers_below_1000000(self):
		result = sum_fibonacci_numbers_below_1000000()
		self.assertEqual(result, 2692537)



	# def test_largest_palindrome_of_thee_digit_numbers(self):
		



if __name__ == '__main__':
	unittest.main()