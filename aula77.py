# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]


def fazer_perguntas(perguntas):
    qtd_acertos = 0

    for pergunta in perguntas:
        print('Pergunta:', pergunta['Pergunta'])

        for i, opcao in enumerate(pergunta['Opções']):
            print(f"{i + 1}) {opcao}")

        resposta_usuario = input("Escolha a opção correta (1-4): ")

        while resposta_usuario not in ['1', '2', '3', '4']:
            print("❌ Opção inválida! Responda novamente de 1-4.")
            resposta_usuario = input("Escolha a opção correta (1-4): ")

        if pergunta['Opções'][int(resposta_usuario) - 1] == pergunta['Resposta']:
            qtd_acertos += 1
            print("😁👍 Resposta correta!\n")
        else:
            print(f"🤔❌ Resposta incorreta! A resposta correta é: {pergunta['Resposta']}\n")

    print(f"Você acertou {qtd_acertos} de {len(perguntas)} perguntas.")


fazer_perguntas(perguntas)