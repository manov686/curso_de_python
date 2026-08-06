# Try, except, else e finally

# a = 18
# b = 0
# c = a/b

try:
    a = 18
    b = 0
    c = a/b
except NameError:
    print('Variável não definida!')
except ZeroDivisionError:
    print('Não é possível dividir por zero!')
except Exception as erro:
    print(f'Ocorreu um erro: {erro.__class__}')

print('O código continua...')