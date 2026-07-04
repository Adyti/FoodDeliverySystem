from models.customer import Customer, PremiumCustomer
from utils.validator import Validator


class CustomerService:
    def __init__(self, customer_repository):
        self.customer_repository = customer_repository

    def create_customer(self, name, phone, customer_type):
        if not Validator.valid_phone(phone):
            raise ValueError("Invalid phone number")

        if customer_type == "premium":
            customer = PremiumCustomer(name, phone)
        else:
            customer = Customer(name, phone)

        self.customer_repository.save(customer)
        return customer

    def list_customers(self):
        return self.customer_repository.get_all()

    def get_customer(self, customer_id):
        return self.customer_repository.get_by_id(customer_id)