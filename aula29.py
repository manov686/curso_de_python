"""
introdução ao Try/Except
"""

numero_str = input(
    'Vou dobrar o número digitado: '
    )

try:
    numero_float = float(numero_str)
    print(f'O dobro de {numero_float} é {numero_float * 2:.1f}')

except ValueError:
    print('Valor digitado não é um número')