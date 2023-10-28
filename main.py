from online_store.models.product import Product
from online_store.models.electronics import Electronics
from online_store.models.clothing import Clothing
from online_store.models.customer import Customer
from online_store.models.order import Order
from online_store.models.inventory import Inventory
from online_store.services.payment_gateway import PaymentGateway
from online_store.services.delivery_service import DeliveryService
import datetime


class OnlineStore:
    def __init__(self):
        self.inventory = Inventory()
        self.customers = []
        self.orders = []
        self.payment_gateway = PaymentGateway()
        self.delivery_service = DeliveryService()

    def add_product(self, product, quantity):
        self.inventory.add_product(product, quantity)

    def remove_product(self, product, quantity):
        self.inventory.remove_product(product, quantity)

    def create_customer(self, name, email, address):
        customer = Customer(name, email, address)
        self.customers.append(customer)
        return customer

    def place_order(self, customer, products):
        for product in products:
            self.inventory.remove_product(product, 1)
        order = Order(customer, products, "Pending", datetime.datetime.now())
        self.orders.append(order)
        self.process_payment(order)
        self.delivery_service.schedule_delivery(order)
        return order

    def process_payment(self, order):
        total_amount = order.calculate_total()
        self.payment_gateway.process_payment(total_amount)
        order.status = "Paid"

    def mark_order_delivered(self, order):
        self.delivery_service.mark_delivered(order)

    def display_inventory(self):
        print("Inventory:")
        for product, quantity in self.inventory.stock.items():
            print(f"- {product.name}: {quantity} in stock")

    def display_customers(self):
        print("Customers:")
        for customer in self.customers:
            print(f"- {customer.name} ({customer.email})")

    def display_orders(self):
        print("Orders:")
        for order in self.orders:
            print(
                f"- Order ID: {id(order)}, Customer: {order.customer.name}, Status: {order.status}, Order Date: {order.order_date}")
            if order.status == "Delivered":
                print(f"   Delivery Date: {order.delivery_date}")


def main():
    store = OnlineStore()

    # Add products to inventory
    product1 = Electronics("Laptop", 1500, "Dell")
    product2 = Clothing("T-Shirt", 20, "M")
    store.add_product(product1, 10)
    store.add_product(product2, 50)

   # Create customers
    customer1 = store.create_customer(
        "Alice", "alice@example.com", "123 Main St")
    customer2 = store.create_customer("Bob", "bob@example.com", "456 Park Ave")

    # Place orders
    order1 = store.place_order(customer1, [product1, product2])
    order2 = store.place_order(customer2, [product2])

    # Mark an order as delivered
    store.mark_order_delivered(order1)

    # Display inventory, customers, and orders
    store.display_inventory()
    store.display_customers()
    store.display_orders()


if __name__ == "__main__":
    main()
