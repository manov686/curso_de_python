"""
Iterando strings com while
"""

nome = "Manoel"
i = 0
resultado = ""

while True:
    if i >= len(nome):
        break

    resultado += nome[i]

    # Só adiciona o * se não for a última letra
    if i < len(nome) - 1:
        resultado += "*"

    i += 1

print(resultado)