# the menu of bill's taco shack is going to start changing rapidly
# therefore the code associated with it needs to be refactored to accomodate a rapidly changing menu
# also prices are going to start being changed on a daily basis, and because of that, we want to pass
#prices when we initialize the customer object


class CustomerRefactored(object):

	def __init__(self, name, cash_available, prices, food={}):
		self.name = name
		self.cash_available = cash_available
		self.prices = prices
		self.food = {}
		# assign cash_available to a variable of customer called cash_available
		# assign prices to a variable of customer named prices
		# assign food to a variable of custmer named food


	def calculate_purchase_amount(self, order):
	#the order object is a dictionary, with food types and amounts
	# order = {
	# 	"burritos": 1,
	# 	"tacos": 3,
	# 	"enchiladas": 1}
	# this function uses self.prices to calculate the cost of all the food in an order
	# and then returns that amount
		purchase_amount = 0
		for food_item, amount in order.items():
			purchase_amount += self.prices[food_item] * amount

		return purchase_amount


	def purchase_food(self, order):
	# use calculate_purchase_amount to calculate the cost of food
	# remove the purchase price of food from self.cash_available
	# add food ordered to the self.food variable
		self.cash_available -= self.calculate_purchase_amount(order)
		for food_item, amount in order.items():
			if food_item in self.food:
				self.food[food_item] += amount
			else:
				self.food[food_item] = amount


	def eat_food(self, food_eaten):
	#remove from self.food the food in the food_eaten object
		for food_item, amount in food_eaten.items():
			if food_item in self.food:
				self.food[food_item] -= food_eaten[food_item]
				# del self.food[food_items]
			
