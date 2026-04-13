"""
https://docs.python.org/pt-br/3/library/stdtypes.html
Imutáveis que vimos: str, int, float, bool
"""
string = 'Manoel Victor Silveira'
# print(string)
# print(outra_variavel)
#print(string.zfill(10))


outra_variavel = f'{string[:3]}eca{string[6:7]}'
print(outra_variavel)