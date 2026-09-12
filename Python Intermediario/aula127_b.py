import json
from aula127_a import Pessoa
from datetime import datetime

p1 = Pessoa('Manoel', 35)
p2 = Pessoa('Maria', 28)
p3 = Pessoa('José', 42)

pessoas = [p1, p2, p3]

dados = [
    {
        'nome': pessoa.nome,
        'idade': pessoa.idade
    }
    for pessoa in pessoas
]

with open('pessoas.json', 'w', encoding='utf-8') as arquivo:
    json.dump(dados, arquivo, ensure_ascii=False, indent=2)