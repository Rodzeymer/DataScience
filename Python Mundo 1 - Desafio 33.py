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
    
print('O menor valor é {}'.format(menor))

print('O maior valor é {}'.format(maior))
    
