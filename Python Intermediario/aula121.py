# Métodos em instâncias de classes Python

class Car:
    def __init__(self, name, model):
        self.name = name
        self.model = model

    def description(self):
        return f'{self.name} {self.model}'