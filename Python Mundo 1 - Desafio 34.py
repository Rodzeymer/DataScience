# Mais um desafio classudo, o usuário entra o valor de um salário e dependendo do seu valor, 
# menor que 1250 reais, sofre um reajuste de 15%, maior que isso recebe apenas 10%

print('*' *30)
print(f"{'Python Mundo 1 - Desafio 34':^30}")
print('*' *30)

salarioBase = int(input('Digite o seu salário'))

if salarioBase >= 1250:
    fatorAumento = 0.1
else:
    fatorAumento = 0.15
aumento = salarioBase*fatorAumento
salarioNovo = salarioBase+aumento

print(f'Seu salário que era de R${salarioBase} agora é R${salarioNovo}, pois teve um aumento de R${aumento}')

print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)