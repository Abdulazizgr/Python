from abc import ABC, abstractmethod


class Product(ABC):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @abstractmethod
    def display_details(self):
        pass
