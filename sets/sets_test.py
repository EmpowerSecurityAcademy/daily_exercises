import unittest
from sets import * 

class TestSets(unittest.TestCase):

	def test_create_set_from_sentence(self):

		result = create_set_from_sentence("driving in the District can be a struggle driving in new york and driving in san francisco can be a struggle as well")
		self.assertEqual(result, set(['a', 'be', 'and', 'francisco', 'driving', 'District', 'struggle', 'well', 'as', 'new', 'york', 'can', 'in', 'san', 'the']))

	def test_intersection_two_sets(self):

		list_a = ["a", "b", "a", "c", "d", "j", "k", "m", "a", "b", "c"]
		list_b = ["a", "f", "l", "z", "j", "w", "w", "y"]

		result = intersection_two_sets(list_a, list_b)

		self.assertEqual(result, ["a", "j"])

	def test_exist_only_in_first_set(self):

		


if __name__ == '__main__':
	unittest.main()