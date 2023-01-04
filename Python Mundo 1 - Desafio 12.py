# Este desafio foi construir um algoritmo que calcula o valor final de um produto, o valor original
# do produto e seu reajuste deve ser informado pelo usuário e o programa devolve o valor inicial
# o percentual de reajuste e o valor reajustado.

print('*' *30)
print(f"{'Python Mundo 1 - Desafio 12':^30}")
print('*' *30)

precoOriginal = float(input('Digite o valor original do produto'))
reajuste = float(input('Agora digite o percentual de reajuste'))

precodesconto = precoOriginal-(precoOriginal*reajuste/100)

print('O produto que valia R${}, com o reajuste de {:.2f}%, está com o preço de R${}'.format(precoOriginal, reajuste, precodesconto))

print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)