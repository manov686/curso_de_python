senha = '123456'
senha_digitada = ''
repeticoes = 0

while senha != senha_digitada and repeticoes < 5:
    senha_digitada = input('Digite a senha: ')  
    repeticoes += 1

if senha == senha_digitada:
    print(f'Parabéns, você acertou a senha! Foram necessárias {repeticoes} tentativas.')
else:
    print('Você excedeu o limite de 5 tentativas.')
