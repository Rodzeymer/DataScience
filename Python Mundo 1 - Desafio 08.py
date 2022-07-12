#Desafio das medidas

metros = float(input('Digite o valor me metros'))



print('{:.0f} metros correspondem a {:.0f} milimetros'.format(metros, metros*1000))
print('{:.0f} metros correspondem a {:.0f} centimetros'.format(metros, metros*100))
print('{:.0f} metros correspondem a {:.0f} decimetros'.format(metros, metros*10))
print('{:.0f} metros correspondem a {:.3f} decametros'.format(metros, metros/10))
print('{:.0f} metros correspondem a {:.3f} hecatometros'.format(metros, metros/100))
print('{:.0f} metros correspondem a {:.4f} quilometros'.format(metros, metros/1000))
