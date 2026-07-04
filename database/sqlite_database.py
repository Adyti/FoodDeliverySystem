import sqlite3
from abc import ABC, abstractmethod


class DatabaseInterface(ABC):
    @abstractmethod
    def connect(self):
        pass


class SQLiteDatabase(DatabaseInterface):
    def __init__(self, db_name="food_delivery.db"):
        self.db_name = db_name
        self.create_tables()

    def connect(self):
        return sqlite3.connect(self.db_name)

    def create_tables(self):
        conn = self.connect()
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT NOT NULL,
            customer_type TEXT NOT NULL
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS restaurants (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            city TEXT NOT NULL
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER NOT NULL,
            restaurant_id INTEGER NOT NULL,
            amount REAL NOT NULL,
            discount REAL NOT NULL,
            delivery_charge REAL NOT NULL,
            final_amount REAL NOT NULL,
            delivery_type TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
        """)

        conn.commit()
        conn.close()