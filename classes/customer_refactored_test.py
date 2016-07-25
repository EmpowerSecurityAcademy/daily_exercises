# the menu of bill's taco shack is going to start changing rapidly
# therefore the code associated with it needs to be refactored to accomodate a rapidly changing menu
# also prices are going to start being changed on a daily basis, and because of that, we want to pass
#prices when we initialize the customer object


import unittest
from customer_refactored import CustomerRefactored

class TestCustomerRefactored(unittest.TestCase):

	def test_init(self):
		test_customer = Customer("bill shelton", 5)

		self.assertEqual(test_customer.cash_available, 5)
		self.assertEqual(test_customer.number_of_tacos, 0)

	def test_purchase_tacos(self):
		test_customer = Customer("bill shelton", 5)
		test_customer.purchase_tacos(2)

		self.assertEqual(test_customer.cash_available, 2)
		self.assertEqual(test_customer.number_of_tacos, 2)

	def test_eat_tacos(self):
		test_customer = Customer("bill shelton", 5)
		test_customer.purchase_tacos(2)
		test_customer.eat_tacos(1)
		self.assertEqual(test_customer.number_of_tacos, 1)

	def test_purchase_burritos(self):
		test_customer = Customer("bill shelton", 15)
		test_customer.purchase_burritos(1)

		self.assertEqual(test_customer.cash_available, 8)
		self.assertEqual(test_customer.number_of_burritos, 1)

	def eat_burrito(self):
		test_customer = Customer("bill shelton", 15)
		test_customer.purchase_burritos(1)

		self.assertEqual(test_customer.number_of_burritos, 1)

		test_customer.eat_burritos(1)
		self.assertEqual(test_customer.number_of_burritos, 0)


if __name__ == '__main__':
	unittest.main()