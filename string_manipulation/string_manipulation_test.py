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

	def test_break_into_sentence(self):

		sample_text = "Lorem ipsum dolor sit amet, nam nostro delicata percipitur ea, nonumes constituto te sit, sed ex maiorum lobortis consulatu. In vivendum legendos vis, dolor contentiones pro no. In pri esse laboramus, ex constituto intellegam voluptatibus est, debitis mandamus sea ei. Usu vitae intellegam te, ea usu causae menandri. Te esse libris quo, iracundia dissentiunt cu sit, purto perpetua partiendo in usu. Te fierent consulatu sea, qui quaeque nominati assentior te. Cum ut feugait interesset, ne sed semper ocurreret.  No sit putant percipit mediocritatem. Ius falli accusam ei. Ne vis persius fuisset. An explicari dissentiunt usu. Fierent erroribus assueverit mei id, ei utinam patrioque his.Iusto mundi scribentur quo an, an affert qualisque inciderint mea. Minimum eloquentiam cum an, hinc mentitum comprehensam pri eu. Nec exerci gubergren in, salutandi gloriatur usu an, habemus evertitur eu ius. Ne vel hendrerit elaboraret voluptatibus, ius oratio placerat ut.Paulo partem referrentur at vis, ut scaevola reprehendunt est. Duo cu nibh quas, usu id odio sententiae. Ea quem vidit solum mea. Sea case aeterno discere ut, tantas nominavi sea id, no per harum molestie. Ex novum affert mei. Everti bonorum nam id.  Quo semper labitur quaestio at. Audire persecuti adolescens no mea, his semper omnium commodo an. Lorem facilisi ea vis. Commodo discere nec te, at sale persius neglegentur pri. Quem exerci complectitur quo cu. Malis principes molestiae te sit. Dolorum sadipscing v"

if __name__ == '__main__':
	unittest.main()