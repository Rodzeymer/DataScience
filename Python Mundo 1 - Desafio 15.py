#Desafio aluguel de carro

tipoCarro = input('Digite o tipo de carro alugado \n B Básico, H Hatch, S Sedan, U Utilitário, P Picape')

if tipoCarro.capitalize() == 'B':
    carroAlugado = 'Básico'
    valorDia = 30
    valorKm = 0.05

if tipoCarro.capitalize() == 'H':
    carroAlugado = 'Hatch'
    valorDia = 45
    valorKm = 0.1

if tipoCarro.capitalize() == 'S':
    carroAlugado = 'Sedan'
    valorDia = 60
    valorKm = 0.15

if tipoCarro.capitalize() == 'U':
    carroAlugado = 'Utilitário'
    valorDia = 90
    valorKm = 0.25

if tipoCarro.capitalize() == 'P':
    carroAlugado = 'Picape'
    valorDia = 120
    valorKm = 0.55

diasUsado = int(input('Digite o número de dias alugado'))
custoDia = valorDia*diasUsado

kmRodado = int(input('Digite quantos quilometros foram rodados'))
custoKm = valorKm*kmRodado

custoFinal = custoDia+custoKm

print('O aluguel do carro {}, por {} dias e rodando {} km, custa R${:.2f}'.format(carroAlugado, diasUsado, kmRodado,custoFinal ))