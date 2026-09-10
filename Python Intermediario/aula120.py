# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classes.
# string = 'Luiz'  # str
# print(string.upper())
# print(isinstance(string, str))

class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

p1 = Person('Manoel Victor', 'Silveira')
p2 = Person('Luiz', 'Otávio')

# p1.name = 'Manoel'
# p1.surname = 'Silveira'

# p2 = Person()
# p2.name = 'Luiz'
# p2.surname = 'Otávio'

print(p1.name, p1.surname)
print(p2.name, p2.surname)