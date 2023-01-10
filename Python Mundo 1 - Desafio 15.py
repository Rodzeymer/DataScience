# O desafio proposto foi o de fazer um algoritmo de locadora de veículos, em que se escolhe
# o tipo de carro para então usar os valores de diária e quilometro rodado para se calcular
# o valor do aluguel, ao final informando o tipo de carro, o número de dias de aluguel e aluguel
# distância percorrida em quilometros

print('*' *30)
print(f"{'Python Mundo 1 - Desafio 15':^30}")
print('*' *30)

tipoCarro = input('Digite o tipo de carro alugado \n B Básico, H Hatch, S Sedan, U Utilitário, P Picape')

if tipoCarro.upper() == 'B':
    carroAlugado = 'Básico'
    valorDia = 30
    valorKm = 0.05
if tipoCarro.upper() == 'H':
    carroAlugado = 'Hatch'
    valorDia = 45
    valorKm = 0.1
if tipoCarro.upper() == 'S':
    carroAlugado = 'Sedan'
    valorDia = 60
    valorKm = 0.15
if tipoCarro.upper() == 'U':
    carroAlugado = 'Utilitário'
    valorDia = 90
    valorKm = 0.25
if tipoCarro.upper() == 'P':
    carroAlugado = 'Picape'
    valorDia = 120
    valorKm = 0.55

diasUsado = int(input('Digite o número de dias alugado'))
custoDia = valorDia*diasUsado

kmRodado = int(input('Digite quantos quilometros foram rodados'))
custoKm = valorKm*kmRodado

custoFinal = custoDia+custoKm

print('O aluguel do carro {}, por {} dias e rodando {} km, custa R${:.2f}'.format(carroAlugado, diasUsado, kmRodado,custoFinal ))

print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)