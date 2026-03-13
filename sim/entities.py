# entities.py

class Entity:
    def __init__(self, name):
        self.name = name

class User(Entity):
    def __init__(self, name, balance):
        super().__init__(name)
        self.balance = balance

