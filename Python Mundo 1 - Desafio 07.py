# Neste algoritimo o usuária irá dar entrada do nome do aluno a ser analisado e suas duas notas, 
# ao fim deve retornar a média simples calculada junto a uma mensagem se o aluno atingiu a média mínima, 
# ou outra se não a alcançou

print('*' *30)
print(f"{'Python Mundo 1 - Desafio 07':^30}")
print('*' *30)

aluno = input('Digite o nome do aluno')

nota1 = float(input('Digite a primeira nota de {}'.format(aluno)))
nota2 = float(input('Digite a segunda nota de {}'.format(aluno)))

media = (nota1+nota2)/2

if media>=6:
    print('Com notas {} e {}, {} conseguiu média {:.2f} e portanto está APROVADO!'.format(nota1, nota2, aluno, media))
if media<6:
    print('Com notas {} e {}, {} conseguiu média {:.2f} e foi reprovado, estude mais!'.format(nota1, nota2, aluno, media))

print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)
    