"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
"""
#        +01234
#        -54321
#string = 'ABCDE'  # 5 caracteres (len)
# print(bool([]))  # falsy
# print(lista, type(lista))

#        0    1      2              3    4
#       -5   -4     -3             -2   -1
#lista = [123, True, 'Luiz Otávio',  1.2, []]
#lista[-3] = 'Manel'
#print(lista)
#print(lista[2], type(lista[2]))


lista = [10,20,30,40]
#lista[2] = 300
lista.append(50)
lista.pop()
lista.append(60)
lista.append(70)
ultimo_valor = lista.pop()
#print(lista)
print(f"{lista} removido: {ultimo_valor}")