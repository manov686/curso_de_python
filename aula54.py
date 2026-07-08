'''Exercício - Lista de Compras'''

import os

buy_list = []
while True:
    os.system('cls' if os.name == 'nt' else 'clear')

    item = input(
        'Selecione uma opção\n'
        '[i]nserir [a]pagar [l]istar [s]air: '
    ).lower()

    if item == 'i':
        add_item = input('Digite o nome do item: ')
        buy_list.append(add_item)

    elif item == 'a':
        if not buy_list:
            print('Lista vazia.')
            input('\nPressione Enter para continuar...')
            continue

        print('\nLista de compras:')
        for indice, valor in enumerate(buy_list, start=1):
            print(f'{indice} - {valor}')

        try:
            indice = int(input('\nÍndice: ')) - 1
            del buy_list[indice]
            print('Item removido com sucesso!')
        except ValueError:
            print('Digite um número.')
        except IndexError:
            print('Índice inexistente.')

        input('\nPressione Enter para continuar...')

    elif item == 'l':
        if not buy_list:
            print('Nada para listar.')
        else:
            print('\nLista de compras:')
            for indice, valor in enumerate(buy_list, start=1):
                print(f'{indice} - {valor}')

        input('\nPressione Enter para continuar...')

    elif item == 's':
        print('Programa encerrado.')
        break

    else:
        print('Opção inválida.')
        input('\nPressione Enter para continuar...')