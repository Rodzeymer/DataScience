# Agora usaremos uma função para sortear a ordem de uma lista, a cada vez que o programa
# é usado ele sorteia uma sequencia de nomes, com base numa dada lista, que poderia ter
# qualquer tamanho

print('*' *30)
print(f"{'Python Mundo 1 - Desafio 20':^30}")
print('*' *30)

import random
confirmar = input('Aperte enter para sortear a ordem dentre os alunos abaixo: \n Arthur, Bruno, Claudio, Daniel.')

alunos = ['Arthur', 'Bruno', 'Claudio', 'Daniel']
random.shuffle(alunos)

print('A sequencia selecionada foi: {}'.format(alunos))

print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)