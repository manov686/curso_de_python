# Exercício - Adiando execução de funções
def soma(x, y):
    return x + y


def multiplica(x, y):
    return x * y


def criar_funcao(funcao, x):
    def funcao_adicionada(*args):
        return funcao(x, *args)
    return funcao_adicionada


soma_com_cinco = criar_funcao(soma, 5)
multiplica_por_dez = criar_funcao(multiplica, 10)


print(soma_com_cinco(3))  # Saída: 8
print(multiplica_por_dez(4))  # Saída: 40


# solução professor

# def soma(x, y):
#     return x + y


# def multiplica(x, y):
#     return x * y


# def criar_funcao(funcao, x):
#     def interna(y):
#         return funcao(x, y)
#     return interna


# soma_com_cinco = criar_funcao(soma, 5)
# multiplica_por_dez = criar_funcao(multiplica, 10)

# print(soma_com_cinco(10))
# print(multiplica_por_dez(10))