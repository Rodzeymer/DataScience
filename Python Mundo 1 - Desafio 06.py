#Desafio modificadores
import math
valor = int(input('Digite um valor a ser analisado'))

dobro = valor*2
triplo = valor*3
quadrado = valor**2
cubo = valor**3
raiz2 = valor**0.5
raiz3 = valor**0.3333

print('O dobro de {} é {}'.format(valor, dobro))
print('O triplo de {} é {}'.format(valor, triplo))
print('{} elevado ao quadrado é {}'.format(valor, quadrado))
print('{} elevado ao cubo é {}'.format(valor, cubo))
print('A raiz quadrada de {} é {}'.format(valor, raiz2))
print('A raiz cúbica de {} é {}'.format(valor, raiz3))