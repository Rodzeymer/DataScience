#Desafio Trigonometria

from math import cos, sin, tan, radians

anguloRad = int(input('Digite o valor de um ângulo'))

anguloDeg = radians(anguloRad)

cosseno = cos(anguloDeg)
seno = sin(anguloDeg)
tangente = tan(anguloDeg)

print('Dado o angulo {}, temos seno={:.2f}, cosseno={:.2f}, tangente={:.2f}'.format(anguloRad, seno, cosseno, tangente))
