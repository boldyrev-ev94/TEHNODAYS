import psycopg2
from psycopg2 import sql
from db import Database


# Создание таблицы пользователей
def create_users_table(name_tabel):
    res = f"""
CREATE TABLE IF NOT EXISTS {name_tabel} (
    id SERIAL PRIMARY KEY,
    id_technopredki INTEGER NOT NULL,
    name VARCHAR(50) NOT NULL,
    surname VARCHAR(50) NOT NULL,
    registrator_id VARCHAR(50),
    registrator_name VARCHAR(255)
);
"""
    return res


# Создание таблицы категорий
# *Не совсем понял про тип данных*
create_categories_table = """
CREATE TABLE IF NOT EXISTS categories (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    value VARCHAR(100),
    value_type VARCHAR(50) CHECK (value_type IN ('time', 'кол-во данных'))
);
"""

# Создание таблицы связи категорий и пользователей
create_user_categories_table = """
CREATE TABLE IF NOT EXISTS user_categories (
    user_id INT REFERENCES users(id) ON DELETE CASCADE,
    category_id INT REFERENCES categories(id) ON DELETE CASCADE,
    PRIMARY KEY (user_id, category_id)
);
"""


def main():
    try:
        db = Database()
        with db.get_cursor() as cursor:
            cursor.execute(create_users_table("users"))
            json_table = get_table("users", *cursor)
            # cursor.execute(get_table("users"))
            # data = cursor.fetchall()
            # columns = [desc[0] for desc in cursor.description]
            # print(columns)
            # users = [json.dumps(User(*row).__dict__) for row in data]
            # print(users)
            # result = {
            #     "columns": columns,
            #     "data": data
            # }
            # print(result)

            # cursor.execute(create_categories_table)
            # cursor.execute(create_user_categories_table)
            print("✅ Таблицы успешно созданы")
    except Exception as e:
        print(f"Ощибка: {e}")
    finally:
        db.close()


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

        return data
    except Exception as e:
        print(f"Ошибка при получении данных: {e}")
        return None


if __name__ == "__main__":
    main()
