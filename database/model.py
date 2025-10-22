class User:

    def __init__(self, id: int, name: str, surname: str):
        self.id = id
        self.name = name
        self.surname = surname

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'surname': self.surname
        }
