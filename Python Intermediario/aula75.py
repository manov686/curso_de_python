'''criar functions multiplicadora'''

"""método pré-histórico"""

# def multiply_x2(number_user):
#     return number_user * 2
# def multiply_x3(number_user):
#     return number_user * 3
# def multiply_x4(number_user):
#     return number_user * 4

# print(multiply_x2(5))
# print(multiply_x3(5))
# print(multiply_x4(5))

# number_user = input("Digite um número: ")
# print(f'seu número vezes 2 é: {multiply_x2(int(number_user))}')
# print(f'seu número vezes 3 é: {multiply_x3(int(number_user))}')
# print(f'seu número vezes 4 é: {multiply_x4(int(number_user))}')



"""Novo método mais complexo, mas mais eficiente"""

def create_multiplier(multiplier):
    def multiply(number):
        return number * multiplier
    return multiply

double = create_multiplier(2)
triple = create_multiplier(3)
quadruple = create_multiplier(4)

number = int(input("Digite um número: "))

print(f'{number} vezes 2 é {double(number)}')
print(f'{number} vezes 3 é {triple(number)}')
print(f'{number} vezes 4 é {quadruple(number)}')