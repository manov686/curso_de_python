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
        self.adresses.append(Address(street, number))

    def list_adresses(self):
        for address in self.adresses:
            print(address.street, address.number)

class Address:
    def __init__(self, street, number):
        self.street = street
        self.number = number

    def __del__(self):
        print(f'Address {self.street}, {self.number} deleted.')



client1 = Client('Luiz')
client1.add_address('Rua A', 123)

client2 = Client('Arthur')
client2.add_address('Rua B', 456)

# print(client1.adresses[0].street)
# print(client2.adresses[0].street)
# print()
client1.list_adresses()
client2.list_adresses()
print('###### Here the code finishes. #####')