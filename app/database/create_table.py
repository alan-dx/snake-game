import sqlite3
from app.database.connection import new_connection


def create_table():
    with new_connection() as connect:
        try:
            cursor = connect.cursor()

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name VARCHAR(40) NOT NULL,
                    score VARCHAR(10) NOT NULL
                );
            """)
        except sqlite3.OperationalError as err:
            print(f'\n {err}')
