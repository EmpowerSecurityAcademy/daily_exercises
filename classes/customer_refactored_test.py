# the menu of bill's taco shack is 


class Customer(object):

	def __init__(self, name, cash_available, food={}):
		self.name = name
		# assign cash_available to a variable of customer called cash_available
		# assign number_of_tacos to a variable of customer called number_of_tacos
		# assign number_of_burritos to a variable of custmer called number_of_burritos
		self.cash_available = cash_available
		self.food = {}


	def purchase_food