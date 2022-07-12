#Desafio parede pintada

import math

comprimento = float(input('Insira o comprimento da parede em metros'))
altura = float(input('Insira a altura da parede em metros'))

area = comprimento * altura

print('A parede tem uma área de {:.2f} m²'.format(area))

tinta = area/2

litros = math.ceil(tinta)

print('Você precisará de {} litros de tinta'.format(litros))