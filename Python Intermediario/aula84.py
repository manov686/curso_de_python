# Introdução à List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.
# print(list(range(10)))
# lista = []
# for numero in range(10):
#     lista.append(numero)
# print(lista)

# lista = [
#     numero * 2
#     for numero in range(10)
# ]
# print(lista)

# import pprint


# def p(v):
#     pprint.pprint(v, sort_dicts=False, width=40)

produtos = [
    {'nome': 'frango', 'preco': 20, 'validade': 2026},
    {'nome': 'acem', 'preco': 30, 'validade': 2026},
    {'nome': 'coxao mole', 'preco': 40, 'validade': 2026}
]

reajuste = [
    {**produto, 'preco': produto['preco'] * 1.05}
    for produto in produtos
]

print(
    *[
        f"{produto['nome']}: R$ {produto['preco']:.2f}".replace('.', ',')
        for produto in reajuste
    ],
    sep='\n'
)