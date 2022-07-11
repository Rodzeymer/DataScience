#desafio dinheiro na carteira

realCarteira = float(input('Quanto dinheiro em real você tem na carteira?'))

cotaçãoRealDolar = 0.185932357
comprarDolar = realCarteira * cotaçãoRealDolar

print('Com R${} você consegue comprar hoje US${:.2f}'.format(realCarteira, comprarDolar))