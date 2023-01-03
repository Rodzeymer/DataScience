# Neste desafio o programa irá perguntar o nome, dia, mês e ano de nascimento e entregar 
# a data formatada em dd/mm/aaaa, perguntando, de forma retórica se está correto

print('*' *30)
print(f"{'Python Mundo 1 - Desafio 02':^30}")
print('*' *30)

name  = input('Olá, seja bem vindo, qual o seu nome?')
anoNasc = input('Muito bem {}, em qual ano você nasceu?'.format(name))
mesNasc = input('{}, em que mês você nasceu?'.format(name))
diaNasc = input('Finalmente, qual foi o dia do seu nascimento {}?'.format(name))
print('Então {}, você nasceu em {}/{}/{}, está correto?'.format(name, diaNasc, mesNasc, anoNasc))
print('*' *30)