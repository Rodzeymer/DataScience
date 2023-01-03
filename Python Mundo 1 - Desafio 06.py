# Ao ser digitado um número inteiro o programa retorna os valores de seu dobro, triplo,
# potencias quadradas, cubicas e raízes, quadrada, cúbica e à quarta, diretamente na formatação
# das strings, reduindo o número de linhas e de variáveis

print('*' *30)
print(f"{'Python Mundo 1 - Desafio 06':^30}")
print('*' *30)

valor = int(input('Digite um valor a ser analisado'))

print('O dobro de {} é {}'.format(valor, valor*2))
print('O triplo de {} é {}'.format(valor, valor*3))
print('{} elevado ao quadrado é {}'.format(valor, valor**2))
print('{} elevado ao cubo é {}'.format(valor, valor**3))
print('A raiz quadrada de {} é {}'.format(valor, valor**(1/2)))
print('A raiz cúbica de {} é {}'.format(valor, valor**(1/3)))
print('A raiz quarta de {} é {}'.format(valor, valor**(1/4)))

print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)
    