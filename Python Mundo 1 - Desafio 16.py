#Desafio parte inteira

import math

numDecimal = float(input('Digite um número quebrado, com casas decimais'))

parteInteira = math.trunc(numDecimal)

print('A parte inteira de {} é {}'.format(numDecimal, parteInteira))