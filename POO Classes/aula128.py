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

p1 = Person('Luiz', 30)
# print(p1.metodo_de_classe())