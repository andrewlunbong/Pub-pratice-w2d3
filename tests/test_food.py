import unittest
from src.pub import Pub
from src.customer import Customer
from src.drink import Drink
from src.food import Food

class TestFood(unittest.TestCase):
    def setUp(self):
        self.food = Food("sushi", 15, 2)

    def test_food_has_name(self):
        self.assertEqual("sushi", self.food.name)

    def test_food_has_price(self):
        self.assertEqual(15, self.food.price)