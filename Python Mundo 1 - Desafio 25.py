# Continuando a procurar por sub-strings dentro de strings, agora o algoritmo localiza no nome
# de uma pessoa o nome silva, podendo estar em qualquer posição da string

print('*' *30)
print(f"{'Python Mundo 1 - Desafio 25':^30}")
print('*' *30)

nome = input('O nome completo de uma pessoa')
oQueProcurar = "silva"

procure = oQueProcurar in nome.lower()

if procure:
    print('Neste nome há Silva')
else:
    print('Neste nome não há Silva')
    
print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)