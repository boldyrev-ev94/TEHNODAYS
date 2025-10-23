import psycopg2
from psycopg2 import sql
from db import Database
import json
from db import Database
import random

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


def get_categorys_dict():
    db = Database()
    with db.get_cursor() as cursor:
        # data = get_table("user_category")
        #         sql_query = """
        # SELECT * FROM user_category
        # INNER JOIN categories ON categories.id = user_category.category_id
        # INNER JOIN users ON users.id = user_category.user_id
        # """
        list_categories = []
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
            # data_json = json.dumps(data, ensure_ascii=False, indent=2)
            value = ""
            toplist = []
            for user in data:
                # print(user)
                try:
                    if user['property'] == "value":
                        value = int(user['value'])
                    if user['property'] == "time_up" or user['property'] == "time_down":
                        # print(user['value'])
                        minute, sec = map(int, user['value'].split(':'))
                        value = minute * 60 + sec
                    toplist.append({
                        "name": f"{user['surname']} {user['name']}",
                        'value': value,
                        "property": user['property']
                    })
                except:
                    pass

            res_list_users = []
            for user in toplist:
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
                "name": key[0],
                "items": res_list_users
            }

            list_categories.append(resaut)
        # json_table = json.dumps(list_categories, ensure_ascii=False, indent=2)
        # print(json_table)
    return list_categories


def get_categories_tables():
    colors = [
        "#e74c3c", "#3498db", "#2ecc71", "#f1c40f", "#9b59b6", "#e67e22", "#1abc9c", "#34495e", "#f39c12", "#7f8c8d", "#1abc9c", "#1abc9c", "#1abc9c", "#1abc9c", "#1abc9c"
    ]
    data = get_categorys_dict()
    resaut = []
    for item in data:
        res = {
            "id": item["id"],
            "name": item["name"],
            "items": [i["name"] for i in item["items"]],
            "color": colors[random.randint(0, len(colors)-1)]
        }
        resaut.append(res)
    return resaut


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
