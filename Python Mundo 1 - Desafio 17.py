#Desafio catetos

from math import sqrt, pow

catetoOposto = float(input('Digite o comprimento do cateto oposto'))
catetoAdjacente = float(input('Digite o comprimento do cateto adjacente'))

hipotenusa = sqrt(pow(catetoOposto,2)+pow(catetoAdjacente,2))

print('O valor do comprimento da hipotenusa é: \n a raiz da soma do quadrado dos catetos')
print('h² = cO² + cA², {}² + {}² = h² > h={:.2f}'.format(catetoOposto, catetoAdjacente, hipotenusa))