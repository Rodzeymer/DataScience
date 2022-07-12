#desafio dinheiro na carteira

realCarteira = float(input('Quanto dinheiro em real você tem na carteira?'))
moeda = input('Para qual moeda deseja converter? \n D de Dólar? \n E de Euro? \n Y de Yene?')

if moeda.capitalize() == 'D':
    cotacaoMoeda = 5.38
    comprarMoeda = realCarteira / cotacaoMoeda
    print('Com R${} você consegue comprar hoje US${:.2f}'.format(realCarteira, comprarMoeda))
    
if moeda.capitalize() == 'E':
    cotacaoMoeda = 5.41
    comprarMoeda = realCarteira / cotacaoMoeda
    print('Com R${} você consegue comprar hoje EU${:.2f}'.format(realCarteira, comprarMoeda))

if moeda.capitalize() == 'Y':
    cotacaoMoeda = 0.039
    comprarMoeda = realCarteira / cotacaoMoeda
    print('Com R${} você consegue comprar hoje Y${:.2f}'.format(realCarteira, comprarMoeda))