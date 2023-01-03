# Agora o usuário deve digitar algo e o algorítimo deve retornar o tipo do que foi digitado,
# se é alfanumérico, números ou letras

print('*' *30)
print(f"{'Python Mundo 1 - Desafio 04':^30}")
print('*' *30)

digitado = input('Digite algo!')
print('Foi digitado {}.'.format(digitado))
print(type(digitado))

if digitado.isalnum():
    print('O {} são letras ou números'.format(digitado))
else:
    print('O {} não são letras nem números'.format(digitado))   
if digitado.isalpha():
    print('O {} são letras'.format(digitado))
if digitado.isnumeric():
    print('O {} são números'.format(digitado))

print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)
    