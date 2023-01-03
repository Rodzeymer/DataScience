# O usuário digita um número inteiro e o script vai mostrar qual valor foi digitado, seu sucessor
# e seu antecessor

print('*' *30)
print(f"{'Python Mundo 1 - Desafio 05':^30}")
print('*' *30)

valor = int(input('Digite o número a ser analisado'))

antes = valor - 1
depois = valor + 1

print('O sucessor de {} é {} \n e o antecessor de {} é {}'.format(valor, depois, valor, antes))

print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)
    