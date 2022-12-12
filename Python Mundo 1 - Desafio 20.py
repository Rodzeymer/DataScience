from random import sample

confirmar = input('Aperte enter para sortear a ordem dentre os alunos abaixo: \n Arthur, Bruno, Claudio, Daniel.')

alunos = ['Arthur', 'Bruno', 'Claudio', 'Daniel']
sequenciaAlunos = sample(alunos, len(alunos))

print('A sequencia selecionada foi: {}'.format(sequenciaAlunos))
