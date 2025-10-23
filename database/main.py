import psycopg2
from psycopg2 import sql
from db import Database
from model import User
import json
from db import Database

CATEGORIES = [
    ("SMS-T", "value", "main_zone"),
    ("Карандаш кассета", "time_down", "main_zone"),
    ("Домашний телефон", "time_down", "main_zone"),
    ("Словарь без инета", "time_down", "main_zone"),
    ("Старый комп VS Новый", "value", "main_zone"),
    ("Железный конструктор", "time_down", "main_zone"),
    ("Перо VS ручка VS Граф.планшет", "time_down", "main_zone"),
    ("Перемотать ДВД", "time_down", "main_zone"),
    ("За рулём", "time_up", "main_zone"),
    ("НТО", "time_down", "main_zone"),
    ("Гонки", "time_down", "cyber_zone"),
    ("Пакман", "value", "cyber_zone"),
    ("Fruit ninja", "value", "cyber_zone"),
    ("Тетрис", "value", "cyber_zone")
]


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
        for id, key in enumerate(CATEGORIES):
            sql_query = f"""
SELECT users.name, users.surname, categories.type, categories.property, user_category.value  FROM user_category
INNER JOIN categories ON categories.id = user_category.category_id
INNER JOIN users ON users.id = user_category.user_id
WHERE categories.id = {id}
"""
        cursor.execute(sql_query)
        column_names = [desc[0] for desc in cursor.description]
        rows = cursor.fetchall()
        data = [dict(zip(column_names, row)) for row in rows]
        print(data)
        value = ""
        toplist = []
        for user in data:
            print(user)
            if user['property'] == "value":
                value = int(user['value'])
            else:
                minute, sec = map(int, user['value'].split(':'))
                value = minute * 60 + sec

            toplist.append({
                "name": f"{user['surname']} {user['name']}",
                'value': value
            })
        res_list_users = []
        if user['property'] == "value":
            res_list_users = sorted(
                toplist, key=lambda x: x['value'], reverse=True)[:15]
        elif user['property'] == "time_up":
            res_list_users = sorted(
                toplist, key=lambda x: x['value'], reverse=True)[:15]
        else:
            res_list_users = sorted(
                toplist, key=lambda x: x['value'], reverse=True)[-15:]

        resaut = {
            "id": id,
            "name": key[1],
            "items": res_list_users
        }
        json_table = json.dumps(resaut, ensure_ascii=False, indent=2)
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
