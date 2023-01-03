# Este algoritimo solicita o valor que o usuário tem em reais e realiza converções para dólares americanos
# euros e yenes, informando o quanto daquela moeda ele consegue comprar

print('*' *30)
print(f"{'Python Mundo 1 - Desafio 10':^30}")
print('*' *30)

realCarteira = float(input('Quanto dinheiro em real você tem na carteira?'))
moeda = input('Para qual moeda deseja converter? \n D de Dólar? \n E de Euro? \n Y de Yene?')

if moeda.upper() == 'D':
    cotacaoMoeda = 5.38
    comprarMoeda = realCarteira / cotacaoMoeda
    print('Com R${} você consegue comprar hoje US${:.2f}'.format(realCarteira, comprarMoeda))
    
if moeda.upper() == 'E':
    cotacaoMoeda = 5.41
    comprarMoeda = realCarteira / cotacaoMoeda
    print('Com R${} você consegue comprar hoje EU${:.2f}'.format(realCarteira, comprarMoeda))

if moeda.upper() == 'Y':
    cotacaoMoeda = 0.039
    comprarMoeda = realCarteira / cotacaoMoeda
    print('Com R${} você consegue comprar hoje Y${:.2f}'.format(realCarteira, comprarMoeda))

print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)
    