# Relações entre classes: associação, agregação e composição
# Agregação é uma forma mais especializada de associação
# entre dois ou mais objetos. Cada objeto terá
# seu ciclo de vida independente.
# Geralmente é uma relação de um para muitos, onde um
# objeto tem um ou muitos objetos.
# Os objetos podem viver separadamente, mas pode
# se tratar de uma relação onde um objeto precisa de
# outro para fazer determinada tarefa.
# (existem controvérsias sobre as definições de agregação).

class Chart:

    def __init__(self):
        self._products = []

    def ttlprice(self):
        return sum(p.price for p in self._products)

    def insert_product(self, *products):
        for p in products:
            self._products.append(p)

    def list_products(self):
        for p in self._products:
            print(p.name, f'R$ {p.price:.2f}')


class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price


chart = Chart()

p1, p2 = Product('camiseta', 50), Product('bermuda', 100)

chart.insert_product(p1, p2)

chart.list_products()
print()
print(f'Total: R$ {chart.ttlprice():.2f}')