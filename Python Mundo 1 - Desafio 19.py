# Os módulos ajudam a realizar tarefas que poderiam ser muito complicadas, como o de um sorteio, 
# o algoritmo a seguir escolhe um nome dentre os 4, poderiam ser mais, e exibe o nome escolhido
# ao final

print('*' *30)
print(f"{'Python Mundo 1 - Desafio 19':^30}")
print('*' *30)

import random

confirmar = input('Aperte enter para sortear um dos alunos abaixo: \n Arthur, Bruno, Claudio, Daniel.')

alunos = ['Arthur', 'Bruno', 'Claudio', 'Daniel']
indiceAluno = random.randint(0,len(alunos)-1)

print('O aluno selecionado foi: {}'.format(alunos[indiceAluno]))
print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)