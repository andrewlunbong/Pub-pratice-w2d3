import unittest
from src.pub import Pub
from src.customer import Customer
from src.drink import Drink
from src.food import Food

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Bob", 60, 30)
        self.customer2 = Customer("John", 150, 15)
        self.drink = Drink("Sex on the beach", 10, 3)
        self.food = Food("sushi", 15, 2)

    def test_customer_has_name(self):
        self.assertEqual("Bob", self.customer.name)

    def test_customer_has_wallet(self):
        self.assertEqual(60, self.customer.wallet)

    def test_customer_can_buy_drink(self):
        self.customer.buy_drink(self.drink)
        self.assertEqual(50, self.customer.wallet)

    def test_customer_has_drunkenness(self):
        self.assertEqual(0, self.customer.drunkenness)

    def test_customer_can_buy_food(self):
        self.customer.buy_food(self.food)
        self.assertEqual(45, self.customer.wallet)

    