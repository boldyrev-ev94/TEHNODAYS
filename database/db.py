import psycopg2
from contextlib import contextmanager
from config_reader import config


class Database:
    def __init__(self):
        try:
            print(
                f"{config.name_db, config.user, config.password.get_secret_value(), config.host, config.port}")
            self.connection = psycopg2.connect(
                dbname=config.name_db,
                user=config.user,
                password=config.password.get_secret_value(),
                host=config.host,
                port=config.port
            )
        except Exception as e:
            print(f"Error Database connect: {e}")
        except:
            print("Fatall except")

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
