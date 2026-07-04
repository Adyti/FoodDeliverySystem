from factories.discount_factory import DiscountFactory
from factories.delivery_factory import DeliveryFactory


class OrderController:
    def __init__(self, order_service, customer_controller, restaurant_controller):
        self.order_service = order_service
        self.customer_controller = customer_controller
        self.restaurant_controller = restaurant_controller

    def create_order(self):
        self.customer_controller.view_customers()
        customer_id = int(input("Enter customer ID: "))

        self.restaurant_controller.view_restaurants()
        restaurant_id = int(input("Enter restaurant ID: "))

        amount = float(input("Enter order amount: "))
        distance = float(input("Enter delivery distance in KM: "))

        discount_type = input("Discount type none/premium/festival: ").lower()
        delivery_type = input("Delivery type bike/car: ").lower()

        discount_strategy = DiscountFactory.create(discount_type)
        delivery_strategy = DeliveryFactory.create(delivery_type)

        try:
            order = self.order_service.create_order(
                customer_id,
                restaurant_id,
                amount,
                distance,
                discount_strategy,
                delivery_strategy
            )

            print("Order created successfully")
            print(order)

        except ValueError as error:
            print(error)

    def view_orders(self):
        orders = self.order_service.list_orders()

        if not orders:
            print("No orders found")
            return

        for order in orders:
            print("-" * 60)
            print(f"Order ID: {order[0]}")
            print(f"Customer: {order[1]}")
            print(f"Restaurant: {order[2]}")
            print(f"Amount: Rs.{order[3]}")
            print(f"Discount: Rs.{order[4]}")
            print(f"Delivery Charge: Rs.{order[5]}")
            print(f"Final Amount: Rs.{order[6]}")
            print(f"Delivery Type: {order[7]}")
            print(f"Created At: {order[8]}")  