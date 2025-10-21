

class Category:
    def __init__(self, name: str):
        self.name = name
        self.param = dict()

    def get_name(self):
        return self.name

    def update(self, key: str, value):
        try:
            if hasattr(self, key):
                setattr(self, key, value)
        except:
            return print(f"Error update class User {self.id} {key} -> {value} ")
