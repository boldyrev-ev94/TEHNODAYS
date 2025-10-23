import random
import psycopg2
from psycopg2 import sql
from db import Database
import json


def add_user(id):
    id_technopredki = id
    name = f"Игрок {id}"
    surname = f"Фамилия {id}"
    mng_id = str(random.randint(5))
    registrator_id = mng_id
    registrator_name = f"РЕГИСТРАТОР {mng_id}"
    date_registr = "NOW()"
    sql = f"""
    INSERT INTO users (id_technopredki, name, surname, registrator_id, registrator_name, date_registr) 
    VALUES ({id_technopredki}, {name}, {surname}, {registrator_id}, {registrator_name}, {date_registr})
    """
    return sql


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
                cursor.execute(sql_query)
                # db.connection.commit()

            data = get_table("users", cursor)
            json_table = json.dumps(data, ensure_ascii=False, indent=2)
            print(json_table)
    except Exception as e:
        print(f"Ошибка при добавлении пользователей: {e}")
    finally:
        db.close()


if __name__ == "__main__":
    main()
