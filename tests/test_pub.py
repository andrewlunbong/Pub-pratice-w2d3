import unittest
from src.pub import Pub
from src.customer import Customer
from src.drink import Drink
from src.food import Food

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("The Chanter", 300)
        self.drink = Drink("Sex on the beach", 10, 3)
        self.customer = Customer("Bob", 60, 30)
        self.customer2 = Customer("John", 150, 15)
        self.food = Food("sushi", 15, 2)
        self.pub.drinks.append(self.drink) 

    def test_pub_has_name(self):
        self.assertEqual("The Chanter", self.pub.name)

        
    def test_pub_has_a_till(self):
        self.assertEqual(300, self.pub.till)

    def test_pub_has_drinks(self):
        self.assertEqual(1, len(self.pub.drinks))

    def test_customer_can_buy_drink(self):
        self.pub.sell_drink(self.drink, self.customer)
        self.assertEqual(50, self.customer.wallet)
        self.assertEqual(310, self.pub.till)
        self.assertEqual(3, self.customer.drunkenness)

    def test_customer_cannot_buy_drink(self):
        self.pub.sell_drink(self.drink, self.customer2)
        self.assertEqual(150, self.customer2.wallet)
        self.assertEqual(300, self.pub.till)
        self.assertEqual(0, self.customer2.drunkenness)

    def test_customer_can_buy_food(self):
        self.pub.sell_food(self.food, self.customer)
        self.assertEqual(45, self.customer.wallet)
        self.assertEqual(315, self.pub.till)
        self.assertEqual(-2, self.customer.drunkenness)

    def test_customer_is_too_drunk_to_serve(self):
        self.pub.sell_drink(self.drink, self.customer)
        self.pub.sell_drink(self.drink, self.customer)
        self.pub.sell_drink(self.drink, self.customer)
        self.pub.sell_drink(self.drink, self.customer)
        self.pub.sell_drink(self.drink, self.customer)
        self.assertEqual(20, self.customer.wallet)
        self.assertEqual(340, self.pub.till)
        self.assertEqual(12, self.customer.drunkenness)

    def test_customer_has_sobered_up(self):
        self.pub.sell_drink(self.drink, self.customer)
        self.pub.sell_drink(self.drink, self.customer)
        self.pub.sell_drink(self.drink, self.customer)
        self.pub.sell_drink(self.drink, self.customer)
        self.pub.sell_food(self.food, self.customer)
        self.pub.sell_drink(self.drink, self.customer)
        self.assertEqual(-5, self.customer.wallet)
        self.assertEqual(365, self.pub.till)
        self.assertEqual(13, self.customer.drunkenness)

    
