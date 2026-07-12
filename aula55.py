'''imprecisão de ponto flutuante'''
import decimal

numero1 = decimal.Decimal(0.1)
numero2 = decimal.Decimal(0.2)
numero3 = numero1 + numero2

print(numero1 + numero2)  # 0.30000000000000004
print(numero3)            # 0.30000000000000004
print(round(numero3, 2))  # 0.3