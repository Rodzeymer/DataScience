# Nesta primeira tabuada o usuário solicita a tabuada de um determinado valor e o sistema
# retorna essa tabuada, formatada

print('*' *30)
print(f"{'Python Mundo 1 - Desafio 09':^30}")
print('*' *30)

numero = int(input('Digite o valor da tabuada'))

print('{} * {:2} = {:2}'.format(numero, 1, numero*1))
print('{} * {:2} = {:2}'.format(numero, 2, numero*2))
print('{} * {:2} = {:2}'.format(numero, 3, numero*3))
print('{} * {:2} = {:2}'.format(numero, 4, numero*4))
print('{} * {:2} = {:2}'.format(numero, 5, numero*5))
print('{} * {:2} = {:2}'.format(numero, 6, numero*6))
print('{} * {:2} = {:2}'.format(numero, 7, numero*7))
print('{} * {:2} = {:2}'.format(numero, 8, numero*8))
print('{} * {:2} = {:2}'.format(numero, 9, numero*9))
print('{} * {:2} = {:2}'.format(numero, 10, numero*10))

print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)
    