nome = input('O nome completo de uma pessoa')
oQueProcurar = "Silva"

procure = oQueProcurar in nome

if procure:
    print('Neste nome há Silva')
else:
    print('Neste nome não há Silva')