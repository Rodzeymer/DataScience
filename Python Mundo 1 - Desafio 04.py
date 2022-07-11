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