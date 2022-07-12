#Desafio Trigonometria

from math import cos, sin, tan

angulo = int(input('Digite o valor de um ângulo'))

cosseno = cos(angulo)
seno = sin(angulo)
tangente = tan(angulo)

print('Dado o angulo {}, temos seno={:.2f}, cosseno={:.2f}, tangente={:.2f}'.format(angulo, seno, cosseno, tangente))
