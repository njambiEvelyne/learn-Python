#Single inheritance
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Product: {self.name}, Price: {self.price}"

class Clothing(Product):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size
    def __str__(self):
        return f"Clothing: {self.name}, {self.price}, {self.size}"

class Utensils(Product):
    def __init__(self, name, price, quantity):
        self.quantity = quantity
        super().__init__(name, price)
    def __str__(self):
        return f"Utensil: {self.name}, Quantity: {self.quantity}"

# class Total(Product, Utensils):
#     def __init__(self, name, price, quantity):
#         super().__init__(name, price, quantity)
#     def __str__(self):
#         total_cost = self.price * self.quantity
#         return f"The total cost is {total_cost}"
#

shirt = Clothing("T-shirt", 20, "M")
print(shirt)

cup = Utensils("Mug", 40, 12)
print(cup)