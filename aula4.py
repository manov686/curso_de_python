from datetime import date

# Dados pessoais
nome = 'Manoel'
sobrenome = 'Silveira'
ano_nascimento = 1991
mes_nascimento = 2
dia_nascimento = 18
altura_metros = 1.88

# Cálculo da idade
hoje = date.today()
data_nascimento = date(ano_nascimento, mes_nascimento, dia_nascimento)

idade = hoje.year - data_nascimento.year
if hoje < data_nascimento.replace(year=hoje.year):
    idade -= 1

# Verifica maioridade
maior_idade = 'Sim' if idade >= 18 else 'Não'

# Saída
print(f'Nome: {nome}')
print(f'Sobrenome: {sobrenome}')
print(f'Idade: {idade} anos')
print(f'Ano de nascimento: {ano_nascimento}')
print(f'É maior de idade?: {maior_idade}')
print(f'Altura em metros: {altura_metros}')
