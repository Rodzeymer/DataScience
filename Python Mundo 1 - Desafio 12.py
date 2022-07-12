#desafio aumento de 15%

#salarioInicial = float(input('Digite o salário a ser reajustado'))

#reajuste = salarioInicial*0.15
#salarioReajustado = salarioInicial*1.15

#print('O salario R${} reajustado a 15%, \nou R${:.2f} a mais, ficará R${}'.format(salarioInicial, reajuste, salarioReajustado))

#Desafio desconto produto

precoOriginal = float(input('Digite o valor original do produto'))

reajuste = float(input('Agora digite o percentual de reajuste'))

reajusteP = reajuste/100

print('O produto que valia R${}, com o reajuste de {:.2f}%, etá com o preço de R${}'.format(precoOriginal, reajusteP, precoOriginal*(reajusteP+1)))