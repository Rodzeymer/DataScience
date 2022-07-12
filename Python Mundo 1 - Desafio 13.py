#desafio aumento de 15%

salarioInicial = float(input('Digite o salário a ser reajustado'))

reajuste = float(input('Digite o percentual de reajuste'))

reajustePP = 1+(reajuste/100)

salarioReajustado = salarioInicial*reajustePP

print('O salario R${} reajustado a 15%, \nou R${:.2f} a mais, ficará R${}'.format(salarioInicial, reajuste, salarioReajustado))
