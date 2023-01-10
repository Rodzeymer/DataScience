# O desafio é de construir um programa que reajuste um salário, cujos valores, do salário
# e do reajuste sejam dados pelos usuários, e ao final exiba uma mensagem com o salário original, 
# o percentual de reajuste, o valor do reajuste e o valor final do salário

print('*' *30)
print(f"{'Python Mundo 1 - Desafio 13':^30}")
print('*' *30)

salarioInicial = float(input('Digite o salário a ser reajustado'))
reajuste = float(input('Digite o percentual de reajuste'))

reajustePP = 1+(reajuste/100)
reajusteValor = salarioInicial*(reajuste/100)
salarioReajustado = salarioInicial*reajustePP

print('O salario R${} reajustado a {}%, \nou R${:.2f} a mais, ficará R${}'.format(salarioInicial, reajuste, reajusteValor, salarioReajustado))

print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)