#Desafio tabuada 2.0


numero = float(input('Digite o valor da tabuada'))
c=1
while c < 11:
    print('{} * {} = {:.2f}'.format(numero, c, numero*c))
    c=c+1