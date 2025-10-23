import psycopg2
from contextlib import contextmanager
from config_reader import config
from psycopg2 import OperationalError, InterfaceError


class Database:
    def __init__(self):
        try:
            self.connection = psycopg2.connect(
                dbname=config.name_db.lower(),
                user=config.user_db.lower(),
                password=config.password_db.get_secret_value(),
                host=config.host_db.lower(),
                port=config.port_db
            )
            print("Коннект прошел успешно!")
        except OperationalError as e:
            print(f"Ошибка подключения к БД: {e}")
            self.connection = None

    @contextmanager
    def get_cursor(self):
        if not self.connection or self.connection.closed:
            raise Exception("Соединение с БД закрыто")

        try:
            with self.connection.cursor() as cursor:
                try:
                    yield cursor
                finally:
                    try:
                        self.connection.commit()
                    except InterfaceError:
                        # Если соединение уже закрыто, просто пропускаем
                        pass
        except Exception as e:
            try:
                self.connection.rollback()
            except InterfaceError:
                pass
            raise e
        finally:
            # Проверка состояния соединения
            if self.connection and not self.connection.closed:
                print("Соединение активно")
            else:
                print("Соединение закрыто")

    def close(self):
        if self.connection and not self.connection.closed:
            try:
                self.connection.close()
            except InterfaceError:
                pass
