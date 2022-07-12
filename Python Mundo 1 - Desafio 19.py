#Sorteio de nomes

import random

confirmar = input('Aperte enter para sortear um dos alunos abaixo: \n Arthur, Bruno, Claudio, Daniel.')

alunos = ['Arthur', 'Bruno', 'Claudio', 'Daniel']
indiceAluno = random.randint(0,len(alunos)-1)

print('O aluno selecionado foi: {}'.format(alunos[indiceAluno]))