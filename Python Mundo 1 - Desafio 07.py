#Desafio média

aluno = input('Digite o nome do aluno')

nota1 = float(input('Digite a primeira nota de {}'.format(aluno)))
nota2 = float(input('Digite a segunda nota de {}'.format(aluno)))

media = (nota1+nota2)/2

if media>=6:
    print('Com notas {} e {}, {} conseguiu média {:.2f} e portanto está APROVADO!'.format(nota1, nota2, aluno, media))

if media<6:
    print('Com notas {} e {}, {} conseguiu média {:.2f} e foi reprovado, estude mais!'.format(nota1, nota2, aluno, media))
