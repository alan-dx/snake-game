from app.database.connection import new_connection
from sqlite3 import OperationalError, Row


def add_user_on_table(name, score):

    with new_connection() as connect:

        try:

            connect.row_factory = Row
            cursor = connect.cursor()
            cursor.execute(f"SELECT * FROM users WHERE name = '{name}'")
            user = cursor.fetchall()

            if len(user) == 0:
                cursor.execute("""
                    INSERT INTO users
                        (name, score)
                    VALUES
                        (?, ?)""", (name, score))
                connect.commit()
            elif (user[0]['score'] < score):
                cursor.execute(f"""
                    UPDATE users
                    SET score = {score}
                    WHERE name = '{name}'
                """)
                connect.commit()

        except OperationalError as err:
            print(f'\n erro: {err}')
