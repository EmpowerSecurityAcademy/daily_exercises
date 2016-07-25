# the menu of bill's taco shack is going to start changing rapidly
# therefore the code associated with it needs to be refactored to accomodate a rapidly changing menu
# also prices are going to start being changed on a daily basis, and because of that, we want to pass
#prices when we initialize the customer object


class CustomerRefactored(object):

	def __init__(self, name, cash_available, prices, food={}):
		self.name = name
		# assign cash_available to a variable of customer called cash_available
		# assign number_of_tacos to a variable of customer called number_of_tacos
		# assign number_of_burritos to a variable of custmer called number_of_burritos
		self.cash_available = cash_available
		self.prices = prices
		self.food = {}

	def calculate_purchase_amount(self, order):
		#the order object is a dictionary, with food types and amounts
		# {
		# 	"burritos": 1,
		# 	"tacos": 3,
		# 	"enchiladas" 1
		# }
		# this function uses self.prices to calculate the cost of all the food in an order
		# and then returns that amount
		bill_amount = 0 

		for food_type, amount in order:
			bill_amount += self.prices["food_type"] * amount

		return bill_amount

	def purchase_food(self, order):
		self.cash_available -= self.calculate_purchase_amount(order)
		for food_type, amount in order:
			self.food["food_type"] += amount


	def eat_food(self, food_eaten):
		for food_type, amount in food_eaten:
			self.food["food_type"] -= amount