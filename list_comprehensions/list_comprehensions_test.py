import unittest
from list_comprehensions import even_numbers, start_with_a

class TestNumbers(unittest.TestCase):

	def test_even_numbers(self):
		result = even_numbers([1, 2, 4, 5, 7, 8])
		self.assertEqual(result, [2, 4, 8])

	def test_start_with_a(self):
		result = start_with_a(["apple", "orange", "carrot"])
		self.assertEqual(result, ["apple"])

if __name__ == '__main__':
	unittest.main()