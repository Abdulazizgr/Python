

class Inventory:
    def __init__(self):
        self.stock = {}

    def add_product(self, product, quantity):
        if product in self.stock:
            self.stock[product] += quantity
        else:
            self.stock[product] = quantity

    def remove_product(self, product, quantity):
        if product in self.stock:
            if self.stock[product] >= quantity:
                self.stock[product] -= quantity
                if self.stock[product] == 0:
                    del self.stock[product]
            else:
                print("Insufficient stock.")
        else:
            print("Product not found.")
