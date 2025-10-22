import psycopg2
from psycopg2 import sql
from db import Database
import json

# Создание таблицы пользователей


def create_users_table(name_tabel):
    res = f"""
CREATE TABLE IF NOT EXISTS {name_tabel} (
    id SERIAL PRIMARY KEY,
    id_technopredki INTEGER NOT NULL,
    name VARCHAR(50) NOT NULL,
    surname VARCHAR(50) NOT NULL,
    registrator_id VARCHAR(50),
    registrator_name VARCHAR(255),
    date_registr TIMESTAMP,
    CONSTRAINT chk_date_registr CHECK (date_registr >= '2000-01-01')
);
"""
    return res


# Создание таблицы категорий
# *Не совсем понял про тип данных*
def create_categories_table(name_tabel):
    res = f"""
CREATE TABLE IF NOT EXISTS {name_tabel} (
    id SERIAL PRIMARY KEY,
    name VARCHAR(150) NOT NULL,
    property VARCHAR(50) CHECK (property IN ('time_up', 'time_down', 'value')) NOT NULL,
    type VARCHAR(50) CHECK (property IN ('main_zone', 'cyber_zone', 'other_zone')) NOT NULL
);
"""
    return res

# Создание таблицы связи категорий и пользователей


def create_user_categories_table(name_tabel):
    res = f"""
CREATE TABLE IF NOT EXISTS {name_tabel} (
    user_id INT REFERENCES users(id) ON DELETE CASCADE,
    category_id INT REFERENCES categories(id) ON DELETE CASCADE,
    value VARCHAR(100),
    PRIMARY KEY (user_id, category_id)
);
"""
    return res


def input_data_category(cursor):
    data_list = [
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
    try:
        db = Database()
        with db.get_cursor() as cursor:
            cursor.executemany(
                "INSERT INTO categories (name, property, type)"
                "VALUES (%s, %s, %s)"
                "RETURNING id",
                data_list
            )
            # inserted_ids = [row[0] for row in cursor.fetchall()]
            # print(inserted_ids)
            data = get_table("categories", cursor)
            json_table = json.dumps(data, ensure_ascii=False, indent=2)
            print(json_table)
    except Exception as e:
        print(f"Ошибка при массовой вставке: {e}")
    finally:
        db.close()


def main():
    try:
        db = Database()
        with db.get_cursor() as cursor:
            cursor.execute(create_users_table("users"))
            print(f"✅ Таблицa {"users"} успешно создана")

            data = get_table("users", cursor)
            json_table = json.dumps(data, ensure_ascii=False, indent=2)
            print(json_table)

            cursor.execute(create_categories_table("categories"))
            print(f"✅ Таблица {"categories"} успешно создана")

            data = get_table("categories", cursor)
            json_table = json.dumps(data, ensure_ascii=False, indent=2)
            print(json_table)

            cursor.execute(create_user_categories_table("user_category"))
            print(f"✅ Таблица {"user_category"} успешно создана")

            data = get_table("user_category", cursor)
            json_table = json.dumps(data, ensure_ascii=False, indent=2)
            print(json_table)
    except Exception as e:
        print(f"Ощибка: {e}")
    finally:
        db.close()
    input_data_category()
    print(f"✅ Данные добавлены")


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
