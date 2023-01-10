# Outro desafio clássico, o usuário digita 3 valores, e o sistema retorna qual dos 3 é maior
# e qual é o menor valor digitado

print('*' *30)
print(f"{'Python Mundo 1 - Desafio 33':^30}")
print('*' *30)

valorA = int(input('Digite o valor de A'))
valorB = int(input('Digite o valor de B'))
valorC = int(input('Digite o valor de C'))

maior = 0
menor = valorA

if valorA >maior:
    maior = valorA
if valorB >maior:
    maior = valorB    
if valorC >maior:
    maior = valorC
if valorB < menor:
    menor = valorB
if valorC < menor:
    menor= valorC
    
print(f'O menor valor é {menor}')
print(f'O maior valor é {maior}')

print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)