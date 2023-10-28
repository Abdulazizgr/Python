class Order:
    def __init__(self, customer, products, status, order_date, delivery_date=None):
        self.customer = customer
        self.products = products
        self.status = status
        self.order_date = order_date
        self.delivery_date = delivery_date

    def calculate_total(self):
        return sum(product.price for product in self.products)

    def display_invoice(self):
        print("Invoice:")
        print(f"Customer: {self.customer.name}")
        print("Order details:")
        for product in self.products:
            print(f"- {product.name}: ${product.price}")
        print(f"Total: ${self.calculate_total()}")
        print(f"Status: {self.status}")
        print(f"Order Date: {self.order_date}")
        if self.status == "Delivered":
            print(f"Delivery Date: {self.delivery_date}")
