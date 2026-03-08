entrada = input('[E]ntrar [S]air: ')
senha_permitida = '123456'

if (entrada == 'E' or entrada == 'e') and input('Senha: ') == senha_permitida:
    print('Entrada autorizada')
else:
    print('Saindo do sistema')