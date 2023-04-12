import unittest
from src.pub import Pub
from src.customer import Customer
from src.drink import Drink
from src.food import Food

class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink = Drink("Sex on the beach", 10, 3)

    def test_drink_has_name(self):
        self.assertEqual("Sex on the beach", self.drink.name)

    def test_drink_has_price(self):
        self.assertEqual(10, self.drink.price)

    def test_drink_has_alcohol_level(self):
        self.assertEqual(3, self.drink.alcohol_level)
