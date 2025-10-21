# from Category import Category
list_events = ['Гонки', 'Пакман', 'Fruit Ninja', 'Тетрис']
list_category = [
    {1: "", }
]


class User():

    def __init__(self, id: int, name: str, surname: str):
        self.id = id
        self.name = name
        self.surname = surname
        self.events = list()
        for ev_name in list_events:
            self.events.append(self.Category(ev_name))

    class Category:
        def __init__(self, name: str):
            self.name = name
            self.param = dict()
            self.value = ""

        def get_name(self):
            return self.name

        def update(self, key: str, value):
            try:
                if hasattr(self, key):
                    setattr(self, key, value)
            except:
                return print(f"Error update class User {self.id} {key} -> {value} ")

    def get_info(self):
        return {
            "id": self.id,
            "name": self.name,
            "surname": self.surname,
            "events": self.events,
        }

    def get_stat(self):
        pass

    def update(self, key: str, value):
        try:
            if hasattr(self, key):
                setattr(self, key, value)
        except:
            return print(f"Error update class User {self.id} {key} -> {value} ")
