import unittest
from tuples import * 

class TestTuples(unittest.TestCase):

	def test_access_tuple_values(self):

		tup_1 = ("spain", "germany", "argentina", "peru", "japan")
		result = access_tuple_values(tup_1)
		self.assertEqual(result, ("argentina", "peru", "japan"))

		tup_2 = ("paris", "buenos aires", "tokyo", "frieburg", "huaraz", "new york", "chicago")
		result = access_tuple_values(tup_2)
		self.assertEqual(result, ("huaraz", "new york", "chicago"))



if __name__ == '__main__':
	unittest.main()