nome = input('O nome completo de uma pessoa')
oQueProcurar = "silva"

procure = oQueProcurar in nome.lower()

if procure:
    print('Neste nome há Silva')
else:
    print('Neste nome não há Silva')