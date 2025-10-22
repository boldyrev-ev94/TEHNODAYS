import psycopg2
from contextlib import contextmanager
from config_reader import config


class Database:
    def __init__(self):
        try:
            self.connection = psycopg2.connect(
                dbname=config.name_db,
                user=config.user,
                password=config.password,
                host=config.host,
                port=config.port
            )
        except OperationalError as e:
            print(f"Ошибка подключения к базе данных: {e}")
        except Exception as e:
            print(f"Error Database connect: {e}")

    @contextmanager
    def get_cursor(self):
        with self.connection.cursor() as cursor:
            try:
                yield cursor
                self.connection.commit()
            except Exception as e:
                self.connection.rollback()
                raise e

    def close(self):
        self.connection.close()
