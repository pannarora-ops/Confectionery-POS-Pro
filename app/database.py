import sqlite3
from app.config import DATABASE_DIR, DATABASE_FILE


class Database:

    def __init__(self):
        DATABASE_DIR.mkdir(parents=True, exist_ok=True)

        self.connection = sqlite3.connect(DATABASE_FILE)
        self.cursor = self.connection.cursor()

    def create_tables(self):

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            role TEXT NOT NULL
        )
        """)

        self.cursor.execute("""
        INSERT OR IGNORE INTO users
        (id, username, password, role)

        VALUES
        (1,'admin','admin123','Administrator')
        """)

        self.connection.commit()

    def close(self):
        self.connection.close()