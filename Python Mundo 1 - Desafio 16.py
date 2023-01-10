# Agora começamos a importar módulos externos ao core do Python, primeiramente, e mais fácil, 
# o módulo math para pegar somente a parte inteira de um número de ponto flutuante

print('*' *30)
print(f"{'Python Mundo 1 - Desafio 16':^30}")
print('*' *30)

import math

numDecimal = float(input('Digite um número quebrado, com casas decimais'))
parteInteira = math.trunc(numDecimal)

print('A parte inteira de {} é {}'.format(numDecimal, parteInteira))

print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)