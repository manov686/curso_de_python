# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores



# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    # 'idade': 900,
}

pessoa.setdefault('idade', 0)

for chave, valor in pessoa.items():
    print(chave, valor)



# copy - retorna uma cópia rasa (shallow copy)
import copy

d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2],
}
d2 = d1.copy()
#d2 = copy.deepcopy(d1)  # cópia profunda (deep copy)
#d2 = copy.copy(d1)  # cópia rasa (shallow copy)
d2['c1'] = 1000
d2['l1'][1] = 999999

print(d1)
print(d2)


# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro


p1 = {
    'nome': 'Luiz',
    'sobrenome': 'Miranda',
}
lista = [['nome', 'novo valor'], ['idade', 30]]
p1.update(lista)
print(p1)

