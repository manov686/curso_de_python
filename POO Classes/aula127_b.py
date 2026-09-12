import json
from aula127_a import CAMINHO_ARQUIVO, Pessoa


with open(CAMINHO_ARQUIVO, 'r', encoding='utf-8') as arquivo:
    dados = json.load(arquivo)

pessoas = [
    Pessoa(pessoa['nome'], pessoa['idade'])
    for pessoa in dados
]

for pessoa in pessoas:
    print(pessoa)