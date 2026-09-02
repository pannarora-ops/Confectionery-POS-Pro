"""
Confectionery POS Pro
Database Module
"""

import sqlite3
from pathlib import Path


# -------------------------------------------------
# Database Path
# -------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

DB_DIR = BASE_DIR / "database"
DB_DIR.mkdir(exist_ok=True)

DB_FILE = DB_DIR / "shop.db"


class Database:

    def __init__(self):
        self.connection = sqlite3.connect(DB_FILE)
        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()

    # ---------------------------------------------
    # Execute Query
    # ---------------------------------------------
    def execute(self, query, values=()):
        self.cursor.execute(query, values)
        self.connection.commit()

    # ---------------------------------------------
    # Fetch One
    # ---------------------------------------------
    def fetchone(self, query, values=()):
        self.cursor.execute(query, values)
        return self.cursor.fetchone()

    # ---------------------------------------------
    # Fetch All
    # ---------------------------------------------
    def fetchall(self, query, values=()):
        self.cursor.execute(query, values)
        return self.cursor.fetchall()

    # ---------------------------------------------
    # Close Connection
    # ---------------------------------------------
    def close(self):
        self.connection.close()

    # ---------------------------------------------
    # Create Tables
    # ---------------------------------------------
    def create_tables(self):

        # ---------------- Users ----------------

        self.execute("""
        CREATE TABLE IF NOT EXISTS users(

            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT,
            fullname TEXT,
            role TEXT,
            active INTEGER DEFAULT 1

        )
        """)

        # ---------------- Categories ----------------

        self.execute("""
        CREATE TABLE IF NOT EXISTS categories(

            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category_name TEXT UNIQUE

        )
        """)

        # ---------------- Products ----------------

        self.execute("""
        CREATE TABLE IF NOT EXISTS products(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            barcode TEXT UNIQUE NOT NULL,

            product_name TEXT NOT NULL,

            category TEXT,

            brand TEXT,

            unit TEXT,

            hsn TEXT,

            gst REAL DEFAULT 0,

            purchase_price REAL DEFAULT 0,

            selling_price REAL DEFAULT 0,

            mrp REAL DEFAULT 0,

            stock REAL DEFAULT 0,

            minimum_stock REAL DEFAULT 0,

            active INTEGER DEFAULT 1,

            created_at TEXT DEFAULT CURRENT_TIMESTAMP,

            updated_at TEXT DEFAULT CURRENT_TIMESTAMP

        )
        """)

        # ---------------- Customers ----------------

        self.execute("""
        CREATE TABLE IF NOT EXISTS customers(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            customer_name TEXT,

            mobile TEXT,

            gstin TEXT,

            address TEXT

        )
        """)

        # ---------------- Suppliers ----------------

        self.execute("""
        CREATE TABLE IF NOT EXISTS suppliers(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            supplier_name TEXT,

            mobile TEXT,

            gstin TEXT,

            address TEXT

        )
        """)

        # ---------------- Sales ----------------

        self.execute("""
        CREATE TABLE IF NOT EXISTS sales(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            bill_no TEXT,

            bill_date TEXT,

            customer_id INTEGER,

            subtotal REAL,

            gst REAL,

            discount REAL,

            grand_total REAL,

            payment_mode TEXT

        )
        """)

        # ---------------- Sale Items ----------------

        self.execute("""
        CREATE TABLE IF NOT EXISTS sale_items(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            sale_id INTEGER,

            product_id INTEGER,

            qty REAL,

            rate REAL,

            gst REAL,

            amount REAL

        )
        """)

        print("Database Ready")


if __name__ == "__main__":

    db = Database()
    db.create_tables()
    db.close()

    print("Database Created Successfully")