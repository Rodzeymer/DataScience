# Neste desafio do Mundo 1 um verdadeiro Boss, em que dada string fornecida pelo usuário
# o programa deve retirar as acentuações e localizar todos os 'a' temos na frase, localizar
# a primeira e a última letra A

print('*' *30)
print(f"{'Python Mundo 1 - Desafio 26':^30}")
print('*' *30)

import unicodedata

frase = input('Escreva uma frase')
fraseNormalize = unicodedata.normalize('NFKD', frase).encode('ASCII', 'ignore').decode('ASCII')
fraseCaixaBaixa = fraseNormalize.lower()
quantosA = fraseCaixaBaixa.count('a') 
quandoPrimeiroA = fraseCaixaBaixa.find('a')+1
quandoUltimoA = fraseCaixaBaixa.rfind('a')+1

print('A frase "{}" possui {} letras A'.format(frase, quantosA))
print('O primeiro A de "{}" é a {}ª letra'.format(frase, quandoPrimeiroA))
print('O último A de "{}" é a {}ª letra'.format(frase, quandoUltimoA))

print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)