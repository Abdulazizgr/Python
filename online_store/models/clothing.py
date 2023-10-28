

class Clothing:
    def __init__(self, name, price, size):
        self.name = name
        self.price = price
        self.size = size

    def display_details(self):
        print(f"Name: {self.name}, Price: {self.price}, Size: {self.size}")
