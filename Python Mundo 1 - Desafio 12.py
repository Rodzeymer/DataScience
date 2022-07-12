#Desafio desconto produto

precoOriginal = float(input('Digite o valor original do produto'))

reajuste = float(input('Agora digite o percentual de reajuste'))

reajusteP = reajuste/100

print('O produto que valia R${}, com o reajuste de {:.2f}%, etá com o preço de R${}'.format(precoOriginal, reajusteP, precoOriginal*(reajusteP-1)))