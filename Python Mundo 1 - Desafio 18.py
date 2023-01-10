# Agora o desafio de trigonometria, em que o módulo math possui funções para transformações de 
# valor de angulo em graus para radianos, vice e versa, e para o cálculo de seno, cosseno e 
# tangente, facilitando o seu uso em alforitmos futuros

print('*' *30)
print(f"{'Python Mundo 1 - Desafio 18':^30}")
print('*' *30)

from math import cos, sin, tan, radians

anguloRad = int(input('Digite o valor de um ângulo em graus'))

anguloDeg = radians(anguloRad)

cosseno = cos(anguloDeg)
seno = sin(anguloDeg)
tangente = tan(anguloDeg)

print('Dado o angulo de {}°, temos seno={:.2f}, cosseno={:.2f}, tangente={:.2f}'.format(anguloRad, seno, cosseno, tangente))

print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)