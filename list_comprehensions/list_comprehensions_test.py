import unittest
from numbers import 

class TestNumbers(unittest.TestCase):

	def test_map(self):
		def multiply_2(num):
			return num * 2

		input_array = [3, 4, 5, 6, 7]
		res = _map(input_array, multiply_2)

		self.assertEqual(res, [6, 8, 10, 12, 14])

if __name__ == '__main__':
	unittest.main()