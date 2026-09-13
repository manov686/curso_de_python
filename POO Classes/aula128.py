# Métodos de classe + factories (fábricas)
# São métodos onde "self" será "cls", ou seja,
# ao invés de receber a instância no primeiro
# parâmetro, receberemos a própria classe.
class Person:
    year = 2026  # atributo de classe

    def __init__(self, name, age):
        self.nome = name
        self.idade = age

    @classmethod
    def metodo_de_classe(cls, name, age):
        return cls(name, age)
    @classmethod
    def sem_nome(cls, age):
        return cls('Anônimo', age)

p1 = Person.metodo_de_classe('Luiz', 30)
p2 = Person.metodo_de_classe('Maria', 20)
p3 = Person.sem_nome(25)
print(p1.nome, p1.idade)
print(p2.nome, p2.idade)
print(p3.nome, p3.idade)