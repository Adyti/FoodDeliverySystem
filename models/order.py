from datetime import datetime

class Order:
    def __init__(self, customer_id, restaurant_id, amount, discount, 
                 delivery_charge, final_amount, delivery_type):
        self.customer_id = customer_id
        self.restaurant_id = restaurant_id
        self.amount = amount
        self.discount = discount
        self.delivery_charge = delivery_charge
        self.final_amount = final_amount
        self.delivery_type = delivery_type
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        return f"Amount: Rs.{self.amount}, Final Amount: Rs.{self.final_amount}"