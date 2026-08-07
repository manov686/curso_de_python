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
except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print(e)
except Exception as error:
    print(f'Ocorreu um erro: {error.__class__.__name__}')

print('O código continua...')
