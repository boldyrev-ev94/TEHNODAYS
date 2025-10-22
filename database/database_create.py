import psycopg2


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
