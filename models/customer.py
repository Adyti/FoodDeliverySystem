class Customer:
    total_created = 0

    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        Customer.total_created += 1

    def get_type(self):
        return "NORMAL"

    @classmethod
    def total_customers_created(cls):
        return cls.total_created

    def __str__(self):
        return f"{self.name} - {self.phone} - {self.get_type()}"


class PremiumCustomer(Customer):
    def get_type(self):
        return "PREMIUM"