# E pra finalizar o Mundo 1 mais um Boss, agora envolvendo trigonometria, novamente, mas para
# descobrir, através de princípios matemáticos se dado 3 valores eles podem formar um trângulo, 
# pois a soma de dois desses lados deve ser igual ou maior que o lado restante

print('*' *30)
print(f"{'Python Mundo 1 - Desafio 35':^30}")
print('*' *30)

ladoA = int(input('Digite o tamanho do lado A'))
ladoB = int(input('Digite o tamanho do lado B'))
ladoC = int(input('Digite o tamanho do lado C'))

if ladoA + ladoB >= ladoC and ladoA + ladoC >= ladoB and ladoB + ladoC >= ladoA:
    print(f'Há um triangulo possível com os lados {ladoA}, {ladoB} e {ladoC}')
else:
    print(f'Não há um triangulo possível com os lados {ladoA}, {ladoB} e {ladoC}')
print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)