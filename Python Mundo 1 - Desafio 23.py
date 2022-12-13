numero = int(input('Digite um número de 1 a 9999'))


if numero < 10:
    print("Unidades: ", numero)

elif numero >= 10 and numero < 100:
    numeroStr = str(numero)
    