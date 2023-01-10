# Neste algoritmo o usuário entra com uma distância a ser viajada em quilometros e o sistem
# retorna o valor da passagem de acordo com a distância, viagens acima de 200 km tem uma 
# tarifa reduzida

print('*' *30)
print(f"{'Python Mundo 1 - Desafio 31':^30}")
print('*' *30)
distancia = int(input('Digite a distancia da viagem em quilômetros'))

if distancia < 200:
    custoPassagem = 0.5
else:
    custoPassagem = 0.45
    
precoPassagem = distancia*custoPassagem

print(f'Para essa viagem de {distancia}Km o preço da passagem é R${precoPassagem}')
print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)