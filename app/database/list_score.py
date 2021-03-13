from app.database.connection import new_connection
from sqlite3 import OperationalError, Row


def list_score():
    with new_connection() as connect:
        try:
            connect.row_factory = Row
            cursor = connect.cursor()
            cursor.execute("SELECT * FROM users ORDER BY score desc")
            users = cursor.fetchall()
        except OperationalError as err:
            print(f'\n {err}')
        else:
            for user in users:
                print(
                    f'\n Player: {user["name"]} | Score: {user["score"]}'
                )
