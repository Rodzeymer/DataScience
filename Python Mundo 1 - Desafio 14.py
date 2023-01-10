# Este algoritmo foi criado para primeiro solicitar qual a medida de temperatura a ser, 
# inserida, o seu valor e para qual temperatura converter, incluindo entradas e saídas, 
# em Célsius, Fahrenheit e Kelvin

print('*' *30)
print(f"{'Python Mundo 1 - Desafio 14':^30}")
print('*' *30)

#Desafio conversão de temperatura

medidaInicial = input('Deseja inserir qual temperatura? \n Célsius? C \n Fahrenheit? F \n Kelvin? K')

if medidaInicial.upper() == 'C':
    temperatura = float(input('Qual a temperatura?'))
    medidaFinal = input('Deseja transformar {} graus Célsius em que medida? \n Fahrenheit? F \n Kelvin? K'.format(temperatura))
    if medidaFinal.upper() == 'F':
        temperaturaConvertida = (temperatura * (9/5)) +32
        print('{} graus Célsius correspondem a {} graus Fahrenheit'.format(temperatura, temperaturaConvertida))
    if medidaFinal.capitalize() == 'K':
        temperaturaConvertida = temperatura + 273.15
        print('{} graus Célsius correspondem a {} Kelvin'.format(temperatura, temperaturaConvertida))

if medidaInicial.upper() == 'F':
    temperatura = float(input('Qual a temperatura?'))
    medidaFinal = input('Deseja transformar {} graus Fahrenheit em que medida? \n Célsius? C \n Kelvin? K'.format(temperatura))
    if medidaFinal.upper() == 'C':
        temperaturaConvertida = (temperatura - 32) * 5/9
        print('{} graus Fahrenheit correspondem a {} graus Célsius'.format(temperatura, temperaturaConvertida))
    if medidaFinal.upper() == 'K':
        temperaturaConvertida = ((temperatura - 32) * 5/9) + 273.15
        print('{} graus Fahrenheit correspondem a {} Kelvin'.format(temperatura, temperaturaConvertida))

if medidaInicial.upper() == 'K':
    temperatura = float(input('Qual a temperatura?'))
    medidaFinal = input('Deseja transformar {} Kelvin em que medida? \n Célsius? C \n Fahrenheit? F'.format(temperatura))
    if medidaFinal.upper() == 'C':
        temperaturaConvertida = temperatura - 273.15
        print('{} Kelvin correspondem a {} graus Célsius'.format(temperatura, temperaturaConvertida))
    if medidaFinal.upper() == 'F':
        temperaturaConvertida =  (temperatura - 273.15) * (9/5) + 32
        print('{} Kelvin correspondem a {} Fahrenheit'.format(temperatura, temperaturaConvertida))
print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)