CAMINHO_ARQUIVO = 'aula127.json'

import json
from aula127_a import Pessoa

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

with open(CAMINHO_ARQUIVO, 'r', encoding='utf-8') as arquivo:
    dados = json.load(arquivo)

pessoas = [
    Pessoa(pessoa['nome'], pessoa['idade'])
    for pessoa in dados
]

for pessoa in pessoas:
    print(pessoa)