import unittest
from dictionaries import * 

class TestDictionaries(unittest.TestCase):

	def test_construct_dictionary(self):
		dictionary_list = [
							{"name": "Rick Garcia"},
							{"nickname": "Rickopotomus"},
							{"favorite_snack": "Thai food"},
						  ]
		result = construct_dictionary(dictionary_list)
		self.assertEqual(result, {"name": "Rick Garcia", "nickname": "Rickopotomus", "favorite_snack": "Thai food"})

	def test_unpack_dictionary(self):
		packed_dictionary = {
								"name": "Steve Van Woerkom",
								"nickname": "Steezey Steve",
								"favorite_snack": "burrito"
							}
		result = unpack_dictionary(packed_dictionary)
		self.assertEqual(result, [{'nickname': 'Steezey Steve'}, {'name': 'Steve Van Woerkom'}, {'favorite_snack': 'burrito'}])


if __name__ == '__main__':
	unittest.main()