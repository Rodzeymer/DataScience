velocidadeCarro = int(input('Digite a velocidade do carro'))

limiteVelocidade = 80
multa = 7*(velocidadeCarro-80)
print('O carro está andando a {}Km/h'.format(velocidadeCarro))

if velocidadeCarro > limiteVelocidade:
    print(multa)
    print('O carro está acima do limite de velocidade de {}Km/h, levou uma multa de R${},00'.format(limiteVelocidade, multa))
else:
    print('O carro está dentro do limite de velocidade, boa viagem.')