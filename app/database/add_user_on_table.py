from app.database.connection import new_connection
import sqlite3


def add_user_on_table(name, score):

    with new_connection() as connect:

        try:

            cursor = connect.cursor()
            cursor.execute("""
                INSERT INTO users
                    (name, score)
                VALUES
                    (?, ?)""", (name, score))
            connect.commit()

        except sqlite3.OperationalError as err:
            print(f'\n {err}')
