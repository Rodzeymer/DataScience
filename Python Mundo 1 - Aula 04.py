# Agora vamos trabaçhar mais com importação de pacotes, neste caso estamos importando 3 pacotes
# o pacote math para usar a ferramenta sqrt (Square Root) realizar a operação de raíz quadrada
# o pacote random, para usar a ferramenta randint, que retorna um número inteiro, aleatório, dentro do intervalo especificado
# e o pcote emoji, para usar o emojize, que retorna emojis no meio do print (infelimente não funciona no online-python.com)

print('*' *30)
print(f"{'Python Mundo 1 - Aula 04':^30}")
print('*' *30)

import emoji
import math
import random

num=random.randint(1, 100)
raiz = math.sqrt(num)

print('A raiz de {} é {}'.format(num, raiz))
print(emoji.emojize('Olá mundo :sunglasses: :earth_americas', use_aliases=True))
print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)
    