class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Tax:
    def __init__(self, tax):
        self.tax= tax

    def apply_tax(self, price):
        return price * (1+ self.tax)

class FinalPrice(Product, Tax):
    #You can inherit using different ways. The first one is:
    def __init__(self, name, price, tax):
        super().__init__(name. price, tax)
    #The second method is:
    def __int__(self, name, price, tax):
        Product.__init__(self, name, price)
        Tax.__init__(self, tax)
    def calculate_product_price(self, price):
        return self.apply_tax(price)

    def __str__(self):
        final_price = self.calculate_product_price(self.price)
        return f"Product: {self.name}, Original Price: {self.price}, Tax: {self.tax * 100}%, Final Price: {final_price:.2}"

product = FinalPrice("Shirt", "9", 0.05)






