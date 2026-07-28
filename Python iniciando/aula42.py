frase = 'Curso de Python 3 - Aula 42. Qual letra aparece mais vezes? Vamos descobrir!'
# i = 0
# letras_mostradas = set()

# while i < len(frase):
#     letra = frase[i]

#     if letra.isalpha() and letra not in letras_mostradas:
#         print(f'A letra "{letra}" aparece {frase.count(letra)} vezes')
#         letras_mostradas.add(letra)

#     i += 1

i = 0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    qtd_apareceu_mais_vezes_atual = frase.count(letra_atual)

    if qtd_apareceu_mais_vezes < qtd_apareceu_mais_vezes_atual:
        qtd_apareceu_mais_vezes = qtd_apareceu_mais_vezes_atual
        letra_apareceu_mais_vezes = letra_atual

    i += 1

print(
    'A letra que apareceu mais vezes foi '
    f'"{letra_apareceu_mais_vezes}" que apareceu '
    f'{qtd_apareceu_mais_vezes} vezes'
)