# Try, except, else e finally

a = 18
b = 0
c = a/b

try:
    c = a/b
except NameError:
    print('Variável não definida!')
except ZeroDivisionError:
    print('Não é possível dividir por zero!')

print('O código continua...')