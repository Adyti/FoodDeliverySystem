from repositories.interfaces import OrderRepositoryInterface


class SQLiteOrderRepository(OrderRepositoryInterface):
    def __init__(self, database):
        self.database = database

    def save(self, order):
        conn = self.database.connect()
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO orders(
            customer_id,
            restaurant_id,
            amount,
            discount,
            delivery_charge,
            final_amount,
            delivery_type,
            created_at
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            order.customer_id,
            order.restaurant_id,
            order.amount,
            order.discount,
            order.delivery_charge,
            order.final_amount,
            order.delivery_type,
            order.created_at
        ))
        conn.commit()
        conn.close()

    def get_all(self):
        conn = self.database.connect()
        cursor = conn.cursor()
        cursor.execute("""
        SELECT 
            orders.id,
            customers.name,
            restaurants.name,
            orders.amount,
            orders.discount,
            orders.delivery_charge,
            orders.final_amount,
            orders.delivery_type,
            orders.created_at
        FROM orders
        JOIN customers ON orders.customer_id = customers.id
        JOIN restaurants ON orders.restaurant_id = restaurants.id
        ORDER BY orders.id DESC
        """)
        orders = cursor.fetchall()
        conn.close()
        return orders   