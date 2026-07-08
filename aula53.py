"""
enumerate - enumera iteráveis (índices)
"""
# [(0, 'Maria'), (1, 'Helena'), (2, 'Luiz'), (3, 'João')]
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

# for item in enumerate(lista, start=1):
#     indice, nome = item
#     print(indice, nome)
    
##lista_enumerada = enumerate(lista)
##lista_enumerada = list(enumerate(lista))

# for indice, nome in enumerate(lista):
#     print(indice, nome, lista[indice])


for tupla_enumerada in enumerate(lista,start=1):
    print('FOR da tupla:')
    for valor in tupla_enumerada:
        print(f'\t{valor}')
