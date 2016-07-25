# the menu of bill's taco shack is going to start changing rapidly
# therefore the code associated with it needs to be refactored to accomodate a rapidly changing menu
# also prices are going to start being changed on a daily basis, and because of that, we want to pass
#prices when we initialize the customer object


import unittest
from customer_refactored import CustomerRefactored

class TestCustomerRefactored(unittest.TestCase):

	prices = {
		"taco": 2,
		"burrito": 8,
		"enchilladas": 6
	}

	def test_init(self):
		test_customer = CustomerRefactored("bill shelton", 15, prices)

		self.assertEqual(test_customer.cash_available, 15)
		self.assertEqual(test_customer.prices, prices)
		self.assertEqual(test_customer.food, {})

	


if __name__ == '__main__':
	unittest.main()