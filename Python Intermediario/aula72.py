# def funcao_mult(x, y, *_r):
#     resultado = x * y
#     for valor in _r:
#         resultado *= valor
#     return resultado

# resultado = funcao_mult(1, 2, 3, 4, 5)


'''
melhorado
'''
def multiply(*args):
    result = 1

    for number in args:
        result *= number

    return result

print(multiply(1, 2, 3, 4, 5))


def even_odd(number):
    if number % 2 == 0:
        return f"{number} is even"
    return f"{number} is odd"

print(even_odd(2))
print(even_odd(3))