# Dicionários em Python (tipo dict)
# Dicionários são estruturas de dados do tipo
# par de "chave" e "valor".
# Chaves podem ser consideradas como o "índice"
# que vimos na lista e podem ser de tipos imutáveis
# como: str, int, float, bool, tuple, etc.
# O valor pode ser de qualquer tipo, incluindo outro
# dicionário.
# Usamos as chaves - {} - ou a classe dict para criar
# dicionários.
# Imutáveis: str, int, float, bool, tuple
# # Mutável: dict, list

# person = {
#     'Nome:': 'Manoel Victor',
#     'Sobrenome:': 'Silveira',
#     'Idade:': 35,
#     'Altura:': 1.88,
#     'Endereços:': [
#         {'rua': 'ten. da cunha silva', 'número': 123},
#         {'rua': 'olimpia cruz', 'número': 321},
#     ],
# }

# for key in person:
#     print(key, person[key])
pessoa = {}

chave = 'nome'

pessoa[chave] = 'Manoel Victor'
pessoa['sobrenome'] = 'Silveira'


print(pessoa[chave])

pessoa[chave] = 'Maria'

del pessoa['sobrenome']
print(pessoa)
print(pessoa['nome'])

# print(pessoa.get('sobrenome'))
if pessoa.get('sobrenome') is None:
    print('NÃO EXISTE')
else:
    print(pessoa['sobrenome'])

# print('ISSO Não vai')