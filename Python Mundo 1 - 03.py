#Operadores matemáticos

#Calculadora inteligente

valor1 = float(input('Digite o primeiro número'))
print('O primeiro valor é {}.'.format(valor1))

valor2 = float(input('Digite o segundo número'))
print('O segundo valor é {}.'.format(valor2))
repetir = 'S'
while repetir=='S':

    print('+ para adição entre {} e {}'.format(valor1, valor2))
    print('- para subtração entre {} e {}'.format(valor1, valor2))
    print('* para multiplicação entre {} e {}'.format(valor1, valor2))
    print('/ para divisão entre {} e {}'.format(valor1, valor2))
    print('** para exponenciação entre {} e {}'.format(valor1, valor2))
    print('% para resto da divisão entre {} e {}'.format(valor1, valor2))
    print('// para divisão inteira entre {} e {}'.format(valor1, valor2))

    operador = input('Que operação deseja realizar?')

    if operador== '+':
        resultado = valor1+valor2
    if operador== '-':
        resultado = valor1-valor2
    if operador== '*':
        resultado = valor1*valor2
    if operador== '/':
        resultado = valor1/valor2
    if operador== '**':
        resultado = valor1**valor2
    if operador== '%':
        resultado = valor1%valor2
    if operador== '//':
        resultado = valor1//valor2

    print('A operação é {} {} {} = {}!'.format(valor1, operador, valor2, resultado))
    repetir = input('Quer realizar outra operação? (S/N)').capitalize()
