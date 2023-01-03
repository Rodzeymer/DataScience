# O desafio 11 foi o de construir um algoritimo que calculasse quantos litros de tinta
# são necessários para se pintar uma parede cujas dimensões são informadas pelo usuário, 
# o programa retorna quantos litros são necessários para isso, considerando que cada litro
# consegue pintar 2 metros quadrados

print('*' *30)
print(f"{'Python Mundo 1 - Desafio 11':^30}")
print('*' *30)

largura = float(input('Insira o largura da parede em metros'))
altura = float(input('Insira a altura da parede em metros'))

area = largura * altura
tinta = area/2

print('A parede tem uma área de {:.2f} m²'.format(area))
print('Você precisará de {} litros de tinta'.format(tinta))

print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)
    