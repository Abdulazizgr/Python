
import datetime


class DeliveryService:
    def schedule_delivery(self, order):
        delivery_date = datetime.datetime.now() + datetime.timedelta(days=3)
        order.delivery_date = delivery_date
        order.status = "Scheduled"
        print(
            f"Delivery scheduled for Order ID: {id(order)}, Delivery Date: {delivery_date}")

    def mark_delivered(self, order):
        order.status = "Delivered"
        print(f"Order ID: {id(order)} marked as delivered")
