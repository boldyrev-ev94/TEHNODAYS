
import psycopg2

# Подключение к серверу PostgreSQL
conn = psycopg2.connect(
    dbname="your_database",  # Имя бд
    user="your_username",  # Пользователь
    password="your_password",  # Пароль, созданный для пользователя
    host="localhost",  # оставить так, подключаемся локально на сервере
    port="5432"  # дефолтный порт  PostgreSQL
)

cur = conn.cursor()

# Создание таблицы пользователей
create_users_table = """
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    id_technopredki VARCHAR(50),
    name VARCHAR(255),
    registrator_id VARCHAR(50),
    registrator_name VARCHAR(255)
);
"""

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


async def main():
    # Выполнение SQL создание таблиц
    cur.execute(create_users_table)
    cur.execute(create_categories_table)
    cur.execute(create_user_categories_table)
    # Подтверждаем
    conn.commit()

    print("Таблицы успешно созданы")

    cur.close()
    conn.close()


if __name__ == "__main__":
    asyncio.run(main())
