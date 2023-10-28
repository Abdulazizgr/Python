

class Electronics:
    def __init__(self, name, price, brand):
        self.name = name
        self.price = price
        self.brand = brand

    def display_details(self):
        print(f"name{self.name}, price: {self.price}, Brand: {self.brand}")
