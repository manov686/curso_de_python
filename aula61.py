"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

# cpf_enviado = input('Digite o CPF: ')\
#     .replace('.', '')\
#     .replace('-', '')\
#     .replace('/', '')\
#     .replace(' ', '')

import re

cpf_enviado = re.sub(r'[^0-9]', '', input('Digite o CPF: '))
entrada_repetida = cpf_enviado == cpf_enviado[0] * len(cpf_enviado)

if len(cpf_enviado) != 11 or entrada_repetida:
    print('CPF inválido!')
    exit()

nove_digitos = str(cpf_enviado)[:9]
contador_regressivo_1 = 10

resultado_dig_1 = 0
for digito_1 in nove_digitos:
    resultado_dig_1 += int(digito_1) * contador_regressivo_1
    contador_regressivo_1 -= 1

digito_1 = (resultado_dig_1*10 % 11 if resultado_dig_1 * 10 % 11 <= 9 else 0)


dez_digitos = str(cpf_enviado)[:10]
contador_regressivo_2 = 11

resultado_dig_2 = 0
for digito_2 in dez_digitos:
    resultado_dig_2 += int(digito_2) * contador_regressivo_2
    contador_regressivo_2 -= 1

digito_2 = (resultado_dig_2*10 % 11 if resultado_dig_2 * 10 % 11 <= 9 else 0)

cpf_calculado = f'{nove_digitos}{digito_1}{digito_2}'

if cpf_enviado == cpf_calculado:
    print(f'{cpf_calculado}: CPF Válido')
else:
    print(f'{cpf_calculado}: CPF Inválido')