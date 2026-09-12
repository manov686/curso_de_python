import json
from aula127_a import CAMINHO_ARQUIVO, Pessoa


with open(CAMINHO_ARQUIVO, 'r', encoding='utf-8') as arquivo:
    dados = json.load(arquivo)

pessoal = [
    Pessoa(**pessoal)
    for pessoal in dados
]

for pessoa in pessoal:
    print(pessoa)