from models.order import Order
from utils.validator import Validator


class OrderService:
    def __init__(self, order_repository, customer_service, restaurant_service):
        self.order_repository = order_repository
        self.customer_service = customer_service
        self.restaurant_service = restaurant_service

    def create_order(self, customer_id, restaurant_id, amount, distance, 
                     discount_strategy, delivery_strategy):
        customer = self.customer_service.get_customer(customer_id)
        restaurant = self.restaurant_service.get_restaurant(restaurant_id)

        if not customer:
            raise ValueError("Customer not found")

        if not restaurant:
            raise ValueError("Restaurant not found")

        if not Validator.valid_amount(amount):
            raise ValueError("Amount should be positive")

        discount = discount_strategy.apply(amount)
        delivery_charge = delivery_strategy.calculate_charge(distance)
        final_amount = amount - discount + delivery_charge

        order = Order(
            customer_id,
            restaurant_id,
            amount,
            discount,
            delivery_charge,
            final_amount,
            delivery_strategy.get_type()
        )

        self.order_repository.save(order)
        return order

    def list_orders(self):
        return self.order_repository.get_all()