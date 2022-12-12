import random

confirmar = input('Aperte enter para sortear a ordem dentre os alunos abaixo: \n Arthur, Bruno, Claudio, Daniel.')

alunos = ['Arthur', 'Bruno', 'Claudio', 'Daniel']
random.shuffle(alunos)

print('A sequencia selecionada foi: {}'.format(alunos))
