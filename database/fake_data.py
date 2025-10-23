import random
import psycopg2
from psycopg2 import sql
from db import Database
import json
from datetime import datetime

CATEGORYLIST = [
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


def add_user(id):
    id_technopredki = id
    name = f"Игрок {id}"
    surname = f"Фамилия {id}"
    mng_id = str(random.randint(1, 5))
    registrator_id = mng_id
    registrator_name = f"РЕГИСТРАТОР {mng_id}"
    date_registr = f'{datetime.now()}'
    sql = """
    INSERT INTO users (id_technopredki, name, surname, registrator_id, registrator_name, date_registr) 
    VALUES (%s, %s, %s, %s, %s, %s) 
    """
    return [sql, (id_technopredki, name, surname, registrator_id, registrator_name, date_registr)]


def category_for_user():
    pass


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


def main():
    try:
        db = Database()
        with db.get_cursor() as cursor:
            for i in range(20):
                sql_query = add_user(i)
                print(sql_query)
                cursor.execute(sql_query[0], sql_query[1])
                db.connection.commit()

            data = get_table("users", cursor)
            json_table = json.dumps(data, ensure_ascii=False, indent=2)
            print(json_table)

            for user_id in range(1, 20):
                for count_category in range(1, random.randint(1, 14)):
                    sql = """INSERT INTO user_category (user_id, category_id, value) VALUES (%s, %s, %s)"""
                    l = [i for i in range(1, 13)]
                    rand = random.randint(0, len(l))
                    if CATEGORYLIST[rand][1] == "value":
                        cursor.execute(
                            sql, (user_id, l[rand], str(random.randint(80, 1000))))
                    else:
                        cursor.execute(sql, (user_id, l[rand], str(
                            f"{random.randint(0, 23):02}:{random.randint(0, 59):02}")))
                    db.connection.commit()
                    l.pop(rand)

            data = get_table("user_category", cursor)
            json_table = json.dumps(data, ensure_ascii=False, indent=2)
            print(json_table)

    except Exception as e:
        print(f"Ошибка при добавлении пользователей: {e}")
    finally:
        db.close()


if __name__ == "__main__":
    main()
