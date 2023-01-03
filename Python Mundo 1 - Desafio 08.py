# Neste desafio o usuário irá enra um valor em emtros e o sstema irá retornar suas equivalências em 
# milímetros, centímetros, decímetros, decâmetros, hecatômetros e quilómetros

print('*' *30)
print(f"{'Python Mundo 1 - Desafio 08':^30}")
print('*' *30)

metros = float(input('Digite o valor me metros'))

print('{:.0f} metros correspondem a {:.0f} milimetros'.format(metros, metros*1000))
print('{:.0f} metros correspondem a {:.0f} centimetros'.format(metros, metros*100))
print('{:.0f} metros correspondem a {:.0f} decimetros'.format(metros, metros*10))
print('{:.0f} metros correspondem a {:.3f} decametros'.format(metros, metros/10))
print('{:.0f} metros correspondem a {:.3f} hecatometros'.format(metros, metros/100))
print('{:.0f} metros correspondem a {:.4f} quilometros'.format(metros, metros/1000))

print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)
    