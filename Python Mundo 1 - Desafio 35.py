ladoA = int(input('Digite o tamanho do lado A'))
ladoB = int(input('Digite o tamanho do lado B'))
ladoC = int(input('Digite o tamanho do lado C'))

if ladoA + ladoB >= ladoC and ladoA + ladoC >= ladoB and ladoB + ladoC >= ladoA:
    print('Há um triangulo possível com os lados {}, {} e {}'.format(ladoA, ladoB, ladoC))
else:
    print('Não há um triangulo possível com os lados {}, {} e {}'.format(ladoA, ladoB, ladoC))