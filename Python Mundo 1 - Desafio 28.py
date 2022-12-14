import random

numeroEscolhido = random.randint(0, 5)

palpite = int(input('Tente adivinha o número escolhido, de 0 a 5'))

if palpite == numeroEscolhido:
    print('ACERTOU! Seu palpite foi {} o mesmo que o número escolhido {}'.format(palpite, numeroEscolhido))
else:
    print('Errou, o número escolhido foi {} e você digitou {}'.format(numeroEscolhido, palpite))