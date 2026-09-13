# Métodos de classe + factories (fábricas)
# São métodos onde "self" será "cls", ou seja,
# ao invés de receber a instância no primeiro
# parâmetro, receberemos a própria classe.
class Pessoa:
    year = 2026  # atributo de classe

    def __init__(self, name, age):
        self.nome = name
        self.idade = age