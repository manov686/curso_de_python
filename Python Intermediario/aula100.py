# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)


import copy

from dados import produtos

novos_produtos = copy.deepcopy(produtos)

for produto in novos_produtos:
    produto['preco'] = round(produto['preco'] * 1.1, 2)

# Ordenar por nome decrescente
produtos_ordenados_por_nome = sorted(
    copy.deepcopy(novos_produtos),
    key=lambda produto: produto['nome'],
    reverse=True
)

# Ordenar por preço crescente
produtos_ordenados_por_preco = sorted(
    copy.deepcopy(novos_produtos),
    key=lambda produto: produto['preco']
)

print(*produtos_ordenados_por_nome, sep='\n')
print()
print(*produtos_ordenados_por_preco, sep='\n')