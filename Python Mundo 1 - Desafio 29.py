# Este algoritmo calcula se o carro, que o usuário irá informar a velocidade, está acima do
# limite permitido de 80km/h, e se estiver retorna o valor da multa baseado no excedente 
# de velocidade, 7 reais por km/h excedido

print('*' *30)
print(f"{'Python Mundo 1 - Desafio 29':^30}")
print('*' *30)

velocidadeCarro = int(input('Digite a velocidade do carro'))

limiteVelocidade = 80
multa = 7*(velocidadeCarro-80)
print(f'O carro está andando a {velocidadeCarro}Km/h')

if velocidadeCarro > limiteVelocidade:
    print(f'O carro está acima do limite de velocidade de {limiteVelocidade}Km/h e levou uma multa de R${multa},00')
else:
    print('O carro está dentro do limite de velocidade, boa viagem.')
print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)