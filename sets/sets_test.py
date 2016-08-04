import unittest
from sets import * 

class TestSets(unittest.TestCase):

	def test_create_set_from_sentence(self):

		result = create_set_from_sentence("driving in the District can be a struggle driving in new york and driving in san francisco can be a struggle as well")
		self.assertEqual(result, set(['a', 'be', 'and', 'francisco', 'driving', 'District', 'struggle', 'well', 'as', 'new', 'york', 'can', 'in', 'san', 'the']))




if __name__ == '__main__':
	unittest.main()