distancia = int(input('Digite a distancia da viagem em quuilômetros'))

if distancia < 200:
    custoPassagem = 0.5
else:
    custoPassagem = 0.45
    
precoPassagem = distancia*custoPassagem

print('Para essa viagem de {}Km o preço da passagem é R${}'.format(distancia, precoPassagem))