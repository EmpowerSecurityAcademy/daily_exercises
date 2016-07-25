# the menu of bill's taco shack is going to start changing rapidly
# therefore the code associated with it needs to be refactored to accomodate a rapidly changing menu
# also prices are going to start being changed on a daily basis, and because of that, we want to pass
#prices when we initialize the customer object


class CustomerRefactored(object):

	def __init__(self, name, cash_available, food={}, prices):
		self.name = name
		# assign cash_available to a variable of customer called cash_available
		# assign number_of_tacos to a variable of customer called number_of_tacos
		# assign number_of_burritos to a variable of custmer called number_of_burritos
		self.cash_available = cash_available
		self.food = {}


	def purchase_food