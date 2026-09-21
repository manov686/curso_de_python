# Relações entre classes: associação, agregação e composição
# Composição é uma especialização da agregação.
# Mas nela, quando o objeto "pai" for apagado, todas
# as referências dos objetos filhos também são
# apagadas.

class Client:
    def __init__(self, name):
        self.name = name
        self.adresses = []

    def add_address(self, street, number):
        self.adresses.append()

class Address:
    def __init__(self, street, number):
        self.street = street
        self.number = number