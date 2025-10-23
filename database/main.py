import psycopg2
from psycopg2 import sql
from db import Database
from model import User
import json
from db import Database


def main():
    # db = Database()

    # with db.get_cursor() as cursor:
    #     cursor.execute("SELECT * FROM users")
    #     rows = cursor.fetchall()
    #     users = [json.dumps(User(*row).__dict__) for row in rows]
    #     print(users)
    res = get_categorys_dict()


def get_categorys_dict():
    db = Database()
    with db.get_cursor() as cursor:
        # data = get_table("user_category")
        #         sql_query = """
        # SELECT * FROM user_category
        # INNER JOIN categories ON categories.id = user_category.category_id
        # INNER JOIN users ON users.id = user_category.user_id
        # """
        sql_query = """
SELECT categories.name  FROM user_category
INNER JOIN categories ON categories.id = user_category.category_id
INNER JOIN users ON users.id = user_category.user_id
WHERE cat_name = 'SMS-T'
"""
        cursor.execute(sql_query)
        column_names = [desc[0] for desc in cursor.description]
        rows = cursor.fetchall()
        data = [dict(zip(column_names, row)) for row in rows]
        resaut = {
            "name_tabel": "JOIN INNER JOIN INNER",
            "columns": column_names,
            "data": data
        }
        json_table = json.dumps(data, ensure_ascii=False, indent=2)
        print(json_table)
    return json_table


def get_table(table_name, cursor):
    try:
        # Выполняем запрос
        cursor.execute(f"SELECT * FROM {table_name}")
        # Получаем названия столбцов
        column_names = [desc[0] for desc in cursor.description]
        # Получаем данные
        rows = cursor.fetchall()
        # Преобразуем в список словарей
        data = [dict(zip(column_names, row)) for row in rows]
        resaut = {
            "name_tabel": table_name,
            "columns": column_names,
            "data": data
        }
        return resaut
    except Exception as e:
        print(f"Ошибка при получении данных: {e}")
        return None


if __name__ == "__main__":
    main()
