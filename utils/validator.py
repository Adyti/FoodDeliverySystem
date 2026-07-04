class Validator:
    @staticmethod
    def valid_phone(phone):
        return phone.isdigit() and len(phone) == 10

    @staticmethod
    def valid_amount(amount):
        return amount > 0    