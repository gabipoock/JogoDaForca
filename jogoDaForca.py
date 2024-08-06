import random

def escolher_palavra():
    palavras = ['python', 'desenvolvimento', 'java', 'programação', 'algoritmo']
    return random.choice(palavras).upper()

def jogo_da_forca():
    palavra = escolher_palavra()
    letras_adivinhadas = []
    tentativas = 6

    print('| JOGO DA FORCA |')
    print('Seja bem-vindo(a)!')
    print('_' * len(palavra))

    while tentativas > 0:
        tentativa = input('Digite uma letra: ').upper()

        if tentativa in letras_adivinhadas:
            print('Você já tentou essa letra. Digite outra: ')
            continue

        letras_adivinhadas.append(tentativa)

        if tentativa in palavra:
            print('Muito bem! A letra está na palavra.')
        else:
            tentativas -= 1
            print('Errado! Você tem {} tentativas restantes.'.format(tentativas))

        palavra_oculta = ''.join([letra if letra in letras_adivinhadas else '_' for letra in palavra])
        print(''.join(palavra_oculta))

        if '_' not in palavra_oculta:
            print('Parabéns! Você adivinhou a palavra! :)')
            break

    if tentativas == 0:
        print('Você perdeu! :( A Palavra era {}.'.format(palavra))

jogo_da_forca()