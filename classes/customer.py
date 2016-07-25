

class Customer(object):

	def __init__(self, name, cash_available, number_of_tacos=0):
		self.name = name
		# assign cash_available to a variable of customer called cash_available
		# assign number_of_tacos to a variable of customer called number_of_tacos
		self.cash_available = cash_available
		self.number_of_tacos = number_of_tacos


	def purchase_tacos(self, amount):
		#in this function increase number_of_tacos by the amount
		#decrease available cash by 1.5 * amount
		self.number_of_tacos += amount
		self.cash_available -= (1.5 * amount)


