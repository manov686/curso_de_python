# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']

import os

import subprocess

def add_task(tarefa, lista=None):

    if lista is None:

        lista = []

    lista.append(tarefa)

    return lista

todo = []

desfazer = []

while True:

    entrada = input('Digite uma tarefa ou comando (listar, desfazer, refazer, limpar, sair): ')

    if entrada == 'listar':

        print('\nLista de tarefas:')

        for tarefa in todo:

            print(f'- {tarefa}')

    elif entrada == 'desfazer':

        if todo:

            tarefa = todo.pop()

            desfazer.append(tarefa)

            print(f'Tarefa desfeita: {tarefa}')

        else:

            print('Não há tarefas para desfazer.')

    elif entrada == 'refazer':

        if desfazer:

            tarefa = desfazer.pop()

            todo.append(tarefa)

            print(f'Tarefa refeita: {tarefa}')

        else:

            print('Não há tarefas para refazer.')

    elif entrada == 'limpar':

        subprocess.run(['cls'] if os.name == 'nt' else ['clear'], shell=True)

    elif entrada == 'sair':

        print('Programa encerrado.')

        break

    else:

        print('Comando inválido.')

        add_task(entrada, todo)

        desfazer.clear()