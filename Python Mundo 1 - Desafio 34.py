salarioBase = int(input('Digite o seu salário'))

if salarioBase >= 1250:
    fatorAumento = 0.1
else:
    fatorAumento = 0.15
    
aumento = salarioBase*fatorAumento
salarioNovo = salarioBase+aumento

print('Seu salário que era de R${} agora é R${}, pois teve um aumento de R${}'.format(salarioBase, salarioNovo, aumento))