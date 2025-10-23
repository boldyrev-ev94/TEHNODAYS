def add_user():
    pass


def main():
    try:
        db = Database()
        with db.get_cursor() as cursor:
            cursor.execute(add_users())

    except Exception as e:
        print(f"Ощибка при добавлении пользователей: {e}")
    finally:
        db.close()


if __name__ == "__main__":
    main()
