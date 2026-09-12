# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.
# from datetime import datetime
import json

CAMINHO_ARQUIVO = 'aula127.json'

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __repr__(self):
        return f'Pessoa(nome={self.nome!r}, idade={self.idade})'

p1 = Pessoa('Manoel', 35)
p2 = Pessoa('Maria', 28)
p3 = Pessoa('José', 42)

pessoas = [vars(p1), vars(p2), vars(p3)]

dados = [
    {
        'nome': pessoa['nome'],
        'idade': pessoa['idade']
    }
    for pessoa in pessoas
]

with open(CAMINHO_ARQUIVO, 'w', encoding='utf-8') as arquivo:
    json.dump(dados, arquivo, ensure_ascii=False, indent=2)
