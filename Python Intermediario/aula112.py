# filter é um filtro funcional
# reduce

from functools import reduce

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]


def filtrar_preco(produto):
    return produto['preco'] > 100


# novos_produtos = [
#     p for p in produtos
#     if p['preco'] > 100
# # ]
# novos_produtos = filter(
#     # lambda produto: produto['preco'] > 100,
#     filtrar_preco,
#     produtos
# )

# total = 0
# for produto in produtos:
#     total += produto['preco']

print_iter(produtos)
# print_iter(novos_produtos)

# print(sum([produto['preco'] for produto in produtos]))

total = reduce(
    lambda acumulador, produto: acumulador + produto['preco'],
    produtos,
    0
)

print(f'Total: {total:.2f} R$')

