# __dict__ e vars para atributos de instância
class Pessoa:
    ano_atual = 2026

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return self.ano_atual - self.idade

dados_p1 = {'nome': 'Manoel', 'idade': 35}
p1 = Pessoa(**dados_p1)  # Desempacotando o dicionário para criar o objeto p1
# p1 = Pessoa('Manoel', 35)
print(p1.__dict__)  # Mostra os atributos de instância do objeto p1