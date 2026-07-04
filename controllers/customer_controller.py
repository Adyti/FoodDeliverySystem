class CustomerController:
    def __init__(self, customer_service):
        self.customer_service = customer_service

    def add_customer(self):
        name = input("Enter customer name: ")
        phone = input("Enter phone number: ")
        customer_type = input("Enter customer type normal/premium: ").lower()

        try:
            customer = self.customer_service.create_customer(name, phone, customer_type)
            print("Customer added successfully")
            print(customer)
        except ValueError as error:
            print(error)

    def view_customers(self):
        customers = self.customer_service.list_customers()

        if not customers:
            print("No customers found")
            return

        for customer in customers:
            print(f"ID: {customer[0]}, Name: {customer[1]}, Phone: {customer[2]}, Type: {customer[3]}")        