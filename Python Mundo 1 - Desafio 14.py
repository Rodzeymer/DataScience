#Desafio conversão de temperatura

medidaInicial = input('Deseja inserir qual temperatura? \n Célsius? C \n Fahrenheit? F \n Kelvin? K')

if medidaInicial.capitalize() == 'C':
    temperatura = float(input('Qual a temperatura?'))
    medidaFinal = input('Deseja transformar {} graus Célsius em que medida? \n Fahrenheit? F \n Kelvin? K'.format(temperatura))
    if medidaFinal.capitalize() == 'F':
        temperaturaConvertida = (temperatura * (9/5)) +32
        print('{} graus Célsius correspondem a {} graus Fahrenheit'.format(temperatura, temperaturaConvertida))
    if medidaFinal.capitalize() == 'K':
        temperaturaConvertida = temperatura + 273.15
        print('{} graus Célsius correspondem a {} Kelvin'.format(temperatura, temperaturaConvertida))

if medidaInicial.capitalize() == 'F':
    temperatura = float(input('Qual a temperatura?'))
    medidaFinal = input('Deseja transformar {} graus Fahrenheit em que medida? \n Célsius? C \n Kelvin? K'.format(temperatura))
    if medidaFinal.capitalize() == 'C':
        temperaturaConvertida = (temperatura - 32) * 5/9
        print('{} graus Fahrenheit correspondem a {} graus Célsius'.format(temperatura, temperaturaConvertida))
    if medidaFinal.capitalize() == 'K':
        temperaturaConvertida = ((temperatura - 32) * 5/9) + 273.15
        print('{} graus Fahrenheit correspondem a {} Kelvin'.format(temperatura, temperaturaConvertida))

if medidaInicial.capitalize() == 'K':
    temperatura = float(input('Qual a temperatura?'))
    medidaFinal = input('Deseja transformar {} Kelvin em que medida? \n Célsius? C \n Fahrenheit? F'.format(temperatura))
    if medidaFinal.capitalize() == 'C':
        temperaturaConvertida = temperatura - 273.15
        print('{} Kelvin correspondem a {} graus Célsius'.format(temperatura, temperaturaConvertida))
    if medidaFinal.capitalize() == 'F':
        temperaturaConvertida =  (temperatura - 273.15) * (9/5) + 32
        print('{} Kelvin correspondem a {} Fahrenheit'.format(temperatura, temperaturaConvertida))