import psycopg2
from psycopg2 import sql
from db import Database
from model import User
import json

db = Database()


def main():
    with db.get_cursor() as cursor:
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        users = [json.dumps(User(*row).__dict__) for row in rows]
        print(users)


if __name__ == "__main__":
    main()
