termo1=input('Digite um termo')

print('O termo digitado foi {} e é uma {}, pois eu não especifiquei o tipo primitivo'.format(termo1, type(termo1)))

termo2=int(input('Digite um outro termo numérico inteiro'))

print('Esse outro termo, {}, é um {} pois eu especifiquei o seu tipo'.format(termo2, type(termo2)))

termo3 = input('Digite um termo e vamos ver se ele é um número')
if termo3.isnumeric():
    print('O termo {} é um número ou pode ser convertido em um'.format(termo3))
else:
    print('O termo {} não é um número, ou não pode ser convertido em um'.format(termo3))

if termo3.isalpha():
    print('O termo {} é uma letra'.format(termo3))
else:
    print('O termo {} não é uma letra'.format(termo3))

if termo3.isalnum():
    print('O termo {} é uma letra ou um número'.format(termo3))
else:
    print('O termo {} não é uma letra nem um número'.format(termo3))
    