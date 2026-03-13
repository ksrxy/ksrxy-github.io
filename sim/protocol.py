# protocol.py

class Protocol:
    def __init__(self, name):
        self.name = name

    def execute(self):
        print(f"Executing protocol: {self.name}")

