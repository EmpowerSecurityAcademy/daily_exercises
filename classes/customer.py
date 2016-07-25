

class Customer(object):

	def __init__(self, name, cash_available, number_of_tacos=0, number_of_burritos=0):
		self.name = name
		# assign cash_available to a variable of customer called cash_available
		# assign number_of_tacos to a variable of customer called number_of_tacos
		# assign number_of_burritos to a variable of custmer called number_of_burritos
		self.cash_available = cash_available
		self.number_of_tacos = number_of_tacos
		self.number_of_burritos = number_of_burritos


	def purchase_tacos(self, number_tacos_purchased):
		#in this function increase number_of_tacos by the amount
		#decrease available cash by 1.5 * amount
		self.number_of_tacos += number_tacos_purchased
		self.cash_available -= (1.5 * number_tacos_purchased)

	def eat_tacos(self, number_tacos_eaten):
		#subtract the number of tacos eaten from self.number_of_tacos
		self.number_of_tacos -= number_tacos_eaten

	def purchase_burritos(self, number_burritos_purchased):
		#in this function increase number_of_burritos by the amount
		#decrease available cash by 7 * amount		
		self.number_of_burritos += number_burritos_purchased
		self.cash_available -= (7 * number_burritos_purchased)

	def eat_burritos(self, number_burritos_eaten):
		#subtract the number of tacos eaten from self.number_of_tacos
		self.number_of_burritos -= number_burritos_eaten




