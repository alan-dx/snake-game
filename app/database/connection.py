import sqlite3
from contextlib import contextmanager


@contextmanager
def new_connection():
    connection = sqlite3.connect('users.db')

    try:
        yield connection
    finally:
        if (connection):
            connection.close()
