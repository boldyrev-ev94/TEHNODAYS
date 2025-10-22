import psycopg2
from psycopg2 import sql
from db import Database
import json


def drop_tables(name_tabel):
    res = f"""
	DROP TABLE IF EXISTS {name_tabel} CASCADE;
"""
    return res


def main():
    try:
        db = Database()
        with db.get_cursor() as cursor:
            cursor.execute(drop_tables("users"))
            print(f"✅ Таблица {"users"} успешно удалена")
    except Exception as e:
        print(f"Ощибка при удалении: {e}")
    finally:
        db.close()


if __name__ == "__main__":
    main()
