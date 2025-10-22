import psycopg2
from psycopg2 import sql
from database_create import create_users_table, create_categories_table, create_user_categories_table
from config_reader import config

# cur = conn.cursor()
# # Подключение к серверу PostgreSQL
# conn = psycopg2.connect(
#     dbname="your_database",  # Имя бд
#     user="your_username",  # Пользователь
#     password="your_password",  # Пароль, созданный для пользователя
#     host="localhost",  # оставить так, подключаемся локально на сервере
#     port="5432"  # дефолтный порт  PostgreSQL
# )


def main():
    # # Пример использования
    # exists = check_database_exists(
    #     'mydatabase', host='localhost', user='postgres', password=str(config.password.get_secret_value()))
    # print(f"База данных существует: {exists}")
    dsn = {
        "dbname": config.name_bd,
        "user": config.user,
        "password": config.password.get_secret_value(),
        "host": config.host,
        "port": "5432"
    }
    exists = check_database_exists(
        dbname=config.name_bd,
        host=config.host,
        user=config.user,
        password=config.password.get_secret_value(),
        port=4000)

    print(f"База данных существует: {exists}")
    # # Выполнение SQL создание таблиц
    # cur.execute(create_users_table)
    # cur.execute(create_categories_table)
    # cur.execute(create_user_categories_table)
    # # Подтверждаем
    # conn.commit()

    # print("Таблицы успешно созданы")

    # cur.close()
    # conn.close()


def check_database_exists(dsn):
    try:
        # Подключаемся к базе данных postgres (системная БД)
        conn = psycopg2.connect(
            dbname=dsn['dbname'],
            user=dsn['user'],
            password=dsn['password'],
            host=dsn['host'],
            port="5432"
        )
        cursor = conn.cursor()

        # Выполняем запрос к системному каталогу pg_database
        query = sql.SQL("SELECT COUNT(*) FROM pg_database WHERE datname = %s")
        cursor.execute(query, dsn['dbname'])

        # Получаем результат
        result = cursor.fetchone()[0]
        return result > 0

    except psycopg2.Error as e:
        print(f"Ошибка при проверке БД: {e}")
        return False
    finally:
        if conn:
            cursor.close()
            conn.close()


# def check_database_exists(dbname, **kwargs):
#     try:
#         # Пытаемся подключиться к указанной БД
#         with psycopg2.connect(dbname=dbname, **kwargs) as ps:
#             return True
#     except psycopg2.DatabaseError as e:
#         # Если БД не существует, будет выброшено исключение
#         if "does not exist" in str(e):
#             return False
#         raise


if __name__ == "__main__":
    main()
