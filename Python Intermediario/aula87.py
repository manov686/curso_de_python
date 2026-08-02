# isinstance() - verifica se um objeto é de um determinado tipo

lista = [
    'a',
    1,
    1.1,
    True,
    [0, 1, 2],
    (1, 2),
    {0, 1},
    {'nome': 'Luiz'},
]

for item in lista:
    if isinstance(item, set):
        print('SET')
        item.add(5)
        resultado = item

    elif isinstance(item, str):
        print('STR')
        resultado = item.upper()

    elif isinstance(item, (int, float)):
        print('NUM')
        resultado = item * 2

    else:
        print('OUTRO')
        resultado = item

    print(resultado)