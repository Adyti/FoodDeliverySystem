from repositories.interfaces import CustomerRepositoryInterface


class SQLiteCustomerRepository(CustomerRepositoryInterface):
    def __init__(self, database):
        self.database = database

    def save(self, customer):
        conn = self.database.connect()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO customers(name, phone, customer_type) VALUES (?, ?, ?)",
            (customer.name, customer.phone, customer.get_type())
        )
        conn.commit()
        conn.close()

    def get_all(self):
        conn = self.database.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, phone, customer_type FROM customers")
        customers = cursor.fetchall()
        conn.close()
        return customers

    def get_by_id(self, customer_id):
        conn = self.database.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, phone, customer_type FROM customers WHERE id = ?", (customer_id,))
        customer = cursor.fetchone()
        conn.close()
        return customer