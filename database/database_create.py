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
            cursor.execute(get_table("users"))
            rows = cursor.fetchall()
            title = [row[0] for row in rows.description]
            print(title)
            users = [json.dumps(User(*row).__dict__) for row in rows]
            print(users)
            # cursor.execute(create_categories_table)
            # cursor.execute(create_user_categories_table)
            print("✅ Таблицы успешно созданы")
    except Exception as e:
        print(f"Ощибка: {e}")
    finally:
        db.close()


def get_table(name_tabel):
    sql_qestion = f"""
SELECT * FROM {name_tabel}
"""
    return sql_qestion


if __name__ == "__main__":
    main()
