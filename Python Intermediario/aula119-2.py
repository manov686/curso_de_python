import os
import subprocess
import json


def listar(tarefas):
    print()
    if not tarefas:
        print('Nenhuma tarefa para listar')
        return

    print('Tarefas:')
    for tarefa in tarefas:
        print(f'\t{tarefa}')
    print()


def desfazer(tarefas, tarefas_refazer):
    print()
    if not tarefas:
        print('Nenhuma tarefa para desfazer')
        return

    tarefa = tarefas.pop()
    print(f'{tarefa=} removida da lista de tarefas.')
    tarefas_refazer.append(tarefa)
    print()


def refazer(tarefas, tarefas_refazer):
    print()
    if not tarefas_refazer:
        print('Nenhuma tarefa para refazer')
        return

    tarefa = tarefas_refazer.pop()
    print(f'{tarefa=} adicionada na lista de tarefas.')
    tarefas.append(tarefa)
    print()


def adicionar(tarefa, tarefas):
    print()
    tarefa = tarefa.strip()
    if not tarefa:
        print('Você não digitou uma tarefa.')
        return
    print(f'{tarefa=} adicionada na lista de tarefas.')
    tarefas.append(tarefa)
    print()

def ler(tarefas, caminho_arquivo):
    if not os.path.exists(caminho_arquivo):
        return

    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        tarefas_json = arquivo.read()
        tarefas.extend(json.loads(tarefas_json))

def salvar(tarefas, caminho_arquivo):
    with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
        tarefas_json = json.dumps(tarefas, indent = 2, ensure_ascii=False)
        arquivo.write(tarefas_json)

def sair(tarefas, caminho_arquivo):
    salvar(tarefas, caminho_arquivo)
    raise SystemExit


tarefas = []
tarefas_refazer = []

ler(tarefas, 'tarefas.json')

while True:

    print('Comandos: listar, desfazer e refazer')
    tarefa = input('Digite uma tarefa ou comando: ')

    comandos = {
        'listar': lambda: listar(tarefas),
        'desfazer': lambda: desfazer(tarefas, tarefas_refazer),
        'refazer': lambda: refazer(tarefas, tarefas_refazer),
        'clear': lambda: subprocess.run(
            'cls' if os.name == 'nt' else 'clear', shell=True
        ),
        'adicionar': lambda: adicionar(tarefa, tarefas),
        'sair': lambda: sair(tarefas, 'tarefas.json'),
    }

    comando = comandos.get(tarefa) if comandos.get(tarefa) is not None else \
        comandos['adicionar']

    comando()