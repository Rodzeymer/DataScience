#Desafio parede pintada

largura = float(input('Insira o largura da parede em metros'))
altura = float(input('Insira a altura da parede em metros'))

area = largura * altura

print('A parede tem uma área de {:.2f} m²'.format(area))

tinta = area/2

print('Você precisará de {} litros de tinta'.format(tinta))