import unittest
from customer import Customer

class TestCustomer(unittest.TestCase):

	def test_init(self):
		test_customer = Customer("bill shelton", 5)

		self.assertEqual(test_customer.cash_available, 5)
		self.assertEqual(test_customer.number_of_tacos, 0)

	def test_purchase_tacos(self):
		test_customer = Customer("bill shelton", 5)
		test_customer.purchase_tacos(2)

		self.assertEqual(test_customer.cash_available, 2)
		self.assertEqual(test_customer.number_of_tacos, 2)


if __name__ == '__main__':
	unittest.main()