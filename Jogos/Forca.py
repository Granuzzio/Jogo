from random import randrange


def jogar():
    mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = iniciar_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0  # contador

    while not enforcou and not acertou:
        chute = pede_chute()

        if chute in palavra_secreta:
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1
            desenho_forca(erros)

        enforcou = erros == 7
        acertou = '_' not in letras_acertadas

        print(f'{letras_acertadas} \n')

    if acertou:
        mensagem_venceu()
    else:
        mensagem_perdeu(palavra_secreta)


def mensagem_venceu():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def mensagem_perdeu(palavra_secreta=None):
    print("Puxa, você foi enforcado!")
    print(f"A palavra era {palavra_secreta}")
    print("\33[1;91m    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           \33[m")


def desenho_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if erros == 1:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if erros == 2:
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if erros == 3:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if erros == 4:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if erros == 5:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if erros == 6:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if erros == 7:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if chute == letra:
            print(f'A letra {chute} foi encontrada na posção {index + 1}')
            letras_acertadas[index] = letra
        index += 1


def pede_chute():
    chute = input('Qual letra? ')
    chute = chute.strip().upper()
    return chute


def iniciar_letras_acertadas(palavra):
    return ['_' for _ in palavra]


def mensagem_abertura():
    print('-' * 30)
    print('Jogo da forca'.center(30))
    print('-' * 30, '\n')


def carrega_palavra_secreta():
    arquivo = open('palavras.txt', 'r', encoding='utf-8')
    palavras = []

    for linha in arquivo:
        palavras.append(linha.strip())

    arquivo.close()

    numero = randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta


if __name__ == '__main__':
    jogar()