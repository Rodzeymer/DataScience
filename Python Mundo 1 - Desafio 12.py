#desafio aumento de 15%

salarioInicial = float(input('Digite o salário a ser reajustado'))

reajuste = salarioInicial*0.15
salarioReajustado = salarioInicial*1.15

print('O salario R${} reajustado a 15%, \nou R${:.2f} a mais, ficará R${}'.format(salarioInicial, reajuste, salarioReajustado))