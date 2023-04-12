class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = []

    def sell_drink(self, drink, customer):
        if customer.age >= 18 and customer.drunkenness < 12:
            customer.buy_drink(drink)
            self.till += drink.price 
            customer.drunkenness += drink.alcohol_level  

    def sell_food(self, food, customer):
        customer.buy_food(food)
        self.till += food.price
        customer.drunkenness -= food.rejuvenation_level