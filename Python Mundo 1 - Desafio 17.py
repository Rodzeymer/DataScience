# Com os módulos na mão vamos agora pra um desafio matemático que possui duas formas de solução, 
# uma está implementada e outra comentada, com o módulo math conseguimos usar funções de raiz
# quadrada (sqrt) e de potenciação (pow) para se calcular a hipotenusa de um triângulo retângulo
# Mas podemos usar a função hypot para fazer o cálculo direto!

print('*' *30)
print(f"{'Python Mundo 1 - Desafio 17':^30}")
print('*' *30)

from math import sqrt, pow, hypot

catetoOposto = float(input('Digite o comprimento do cateto oposto'))
catetoAdjacente = float(input('Digite o comprimento do cateto adjacente'))

#hipotenusa = sqrt(pow(catetoOposto,2)+pow(catetoAdjacente,2))
hipotenusa = hypot(catetoOposto, catetoAdjacente)

print('O valor do comprimento da hipotenusa é: \n a raiz da soma do quadrado dos catetos')
print('h² = cO² + cA², {}² + {}² = h² > h={:.2f}'.format(catetoOposto, catetoAdjacente, hipotenusa))

print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)