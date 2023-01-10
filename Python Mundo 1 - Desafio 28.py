# Agora um jogo rápido, de adivinhação, o programa irá sortear um número de 0 a 5 e o usuário
# irá dar um palpite, se acertar exibe uma mensagem e se errar outra, ambas mostrando o palpite
# do usuário e o número sorteado pelo sistema

print('*' *30)
print(f"{'Python Mundo 1 - Desafio 28':^30}")
print('*' *30)

import random
numeroEscolhido = random.randint(0, 5)

palpite = int(input('Tente adivinha o número escolhido, de 0 a 5'))

if palpite == numeroEscolhido:
    print(f'ACERTOU! Seu palpite foi {palpite} o mesmo que o número escolhido {numeroEscolhido}')
else:
    print(f'Errou, o número escolhido foi {numeroEscolhido} e você digitou {palpite}')
print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)