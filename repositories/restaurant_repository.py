from repositories.interfaces import RestaurantRepositoryInterface


class SQLiteRestaurantRepository(RestaurantRepositoryInterface):
    def __init__(self, database):
        self.database = database

    def save(self, restaurant):
        conn = self.database.connect()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO restaurants(name, city) VALUES (?, ?)",
            (restaurant.name, restaurant.city)
        )
        conn.commit()
        conn.close()

    def get_all(self):
        conn = self.database.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, city FROM restaurants")
        restaurants = cursor.fetchall()
        conn.close()
        return restaurants

    def get_by_id(self, restaurant_id):
        conn = self.database.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, city FROM restaurants WHERE id = ?", (restaurant_id,))
        restaurant = cursor.fetchone()
        conn.close()
        return restaurant