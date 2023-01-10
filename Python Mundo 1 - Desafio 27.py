# Agora vamos pegar um nome, e com esse programa localizar o primeiro e o último nome digitado, 
# exibindo-os separados ao final do processamento, agora com uma novidade, usando o recurso
# das f-Strings!

print('*' *30)
print(f"{'Python Mundo 1 - Desafio 27':^30}")
print('*' *30)

nome = input('Digite seu nome completo')

nomeSeparado = nome.split()
primeiroNome = nomeSeparado[0]
ultimoNome = nomeSeparado[len(nomeSeparado)-1]

print(f'O seu nome completo é "{nome}"')
print(f'Assim sendo seu primeiro nome é "{primeiroNome}",')
print(f'e seu último nome é "{ultimoNome}"')

print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)