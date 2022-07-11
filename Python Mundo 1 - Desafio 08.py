#Desafio das medidas

metros = float(input('Digite o valor me metros'))

decimetros = metros*10
centimetros = metros*100
milimetros = metros*1000
decametros = metros/10
hecatometros = metros/100
quilometros = metros/1000


print('{} metros correspondem a {:.2f} milimetros'.format(metros, milimetros))
print('{} metros correspondem a {:.2f} centimetros'.format(metros, centimetros))
print('{} metros correspondem a {:.2f} decimetros'.format(metros, decimetros))
print('{} metros correspondem a {:.2f} decametros'.format(metros, decametros))
print('{} metros correspondem a {:.2f} hecatometros'.format(metros, hecatometros))
print('{} metros correspondem a {:.2f} quilometros'.format(metros, quilometros))
