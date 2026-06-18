import subprocess
import os


def clear_screen():
    if os.name == "nt":
        subprocess.run("cls", shell=True)
    else:
        subprocess.run("clear")


secret_word = "python"

letters_found = set()
used_letters = set()

attempts = 0
errors = 0

secret_word_display = "*" * len(secret_word)

while True:
    clear_screen()

    print("=" * 30)
    print("JOGO DA FORCA")
    print("=" * 30)
    print(f"Palavra: {secret_word_display}")
    print(f"Letras usadas: {' '.join(sorted(used_letters))}")
    print()

    user_input = input("Digite uma letra: ").lower().strip()

    # Permite apenas uma letra
    if len(user_input) != 1:
        print("\nDigite apenas uma letra!")
        input("\nPressione ENTER para continuar...")
        continue

    # Verifica se já foi digitada
    if user_input in used_letters:
        print("\nVocê já tentou essa letra!")
        input("\nPressione ENTER para continuar...")
        continue

    used_letters.add(user_input)
    attempts += 1

    if user_input in secret_word:
        letters_found.add(user_input)
        print("\nAcertou!")
    else:
        errors += 1
        print("\nErrou!")

    input("\nPressione ENTER para continuar...")

    secret_word_display = ""

    for letter in secret_word:
        if letter in letters_found:
            secret_word_display += letter
        else:
            secret_word_display += "*"

    if secret_word_display == secret_word:
        clear_screen()

        accuracy = ((attempts - errors) / attempts) * 100

        print("=" * 30)
        print("PARABÉNS!")
        print("=" * 30)
        print(f"Você acertou a palavra: {secret_word}")
        print(f"Total de tentativas: {attempts}")
        print(f"Total de erros: {errors}")
        print(f"Precisão: {accuracy:.2f}%")
        print("=" * 30)

        break