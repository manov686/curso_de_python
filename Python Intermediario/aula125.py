#Atributos de classe

ANO_ATUAL = 2026

class pessoa:
    ano_atual = 2026

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return pessoa.ano_atual - self.idade

p1 = pessoa('Manoel', 35)
p2 = pessoa('Maria', 20)
print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())