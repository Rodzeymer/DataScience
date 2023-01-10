# Mais um desafio clássico, aqui o usuário digita um ano qualquer e o programa analisa se o 
# ano digitado é ou não bissexto, se o ano for divísivel por 4 mas não por 100 ou se for 
# divisível por 400 então é bissexto

print('*' *30)
print(f"{'Python Mundo 1 - Desafio 32':^30}")
print('*' *30)

ano = int(input('Digite um ano a ser analisado'))

if (ano%4==0 and ano%100!=0) or (ano%400==0):
    print(f'O ano {ano} é bissexto')
else:
    print(f'O ano {ano} não é bissexto')

print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)