from abc import ABC, abstractmethod
class Item(ABC):
    @abstractmethod
    def calculate_cost(self):
        pass
    
    def get_description(self):
        pass


class Pizza(Item):

    BASE_PRICES = {'Small': 8, 'Medium': 10, 'Large': 12}
    TOPPING_PRICES = {
        'Pepperoni': {'Small': 1, 'Medium': 1.5, 'Large': 2},
        'Olives': {'Small': 0.5, 'Medium': 1, 'Large': 1.5},
        'Mushrooms': {'Small': 0.8, 'Medium': 1.2, 'Large': 1.8}
    }
    CRUST_PREMIUMS = {'Gluten Free': 2, 'Stuffed': 3}

    def __init__(self, size, crust, toppings, sauces):
        self.size = size
        self.crust = crust
        self.toppings = toppings
        self.sauces = sauces
    
    def calculate_cost(self):
        cost = self.BASE_PRICES[self.size]
        cost += sum(self.TOPPING_PRICES[topping][self.size] for topping in self.toppings)
        if self.crust in self.CRUST_PREMIUMS:
            cost += self.CRUST_PREMIUMS[self.crust]
        return cost
    
    def get_description(self):
        return f"{self.size} {self.crust} crust pizza with {', '.join(self.toppings) or 'no toppings'} and {', '.join(self.sauces) or 'no sauce'}"

class Drink(Item):

    BASE_PRICES = {'Small': 2, 'Medium': 2.5, 'Large': 3}

    def __init__(self, size, name):
        self.size = size
        self.name = name

    def calculate_cost(self):
        return self.BASE_PRICES[self.size]
    
    def get_description(self):
        return f"{self.size} {self.name}"

    
class PizzaBuilder:

    def __init__(self):
        self.size = 'Medium'
        self.crust = 'Normal'
        self.toppings = []
        self.sauces = []
    
    def set_size(self, size):
        self.size = size
        return self
    
    def set_crust(self, crust):
        self.crust = crust
        return self
    
    def add_topping(self, topping):
        self.toppings.append(topping)
        return self
    
    def add_sauce(self, sauce):
        self.sauces.append(sauce)
        return self
    
    def build(self):
        return Pizza(self.size, self.crust, self.toppings, self.sauces)
    
class Cart:
    def __init__(self):
        self.items = []
    
    def add_item(self, item):
        self.items.append(item)
    
    def checkout(self):
        total_cost = sum(item.calculate_cost() for item in self.items)
        print("Order Summary:")
        for i, item in enumerate(self.items):
            print(f"{i+1}. {item.get_description()} -> ${item.calculate_cost()}")
        print(f"Total Cost: {total_cost}")

cart = Cart()
pizza_1 = PizzaBuilder().set_size('Large').set_crust('Pan').add_topping('Mushrooms').add_sauce('Marinara').build()
cart.add_item(pizza_1)
cart.checkout()
pizza_2 = PizzaBuilder().set_size('Small').set_crust('Gluten Free').add_topping('Mushrooms').add_topping('Olives').add_sauce('Marinara').build()
cart.add_item(pizza_2)
drink_1 = Drink('Small', 'Coke')
cart.add_item(drink_1)
drink_2 = Drink('Large', 'Dr. Pepper')
cart.add_item(drink_2)
cart.checkout()

