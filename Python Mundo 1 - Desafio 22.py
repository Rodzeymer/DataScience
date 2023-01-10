# Agora começamos a abordar um tema mais complexo, manipulação de strings, que desagua na
# manipulação de arrays, que é mais complexo, mas funciona para muitas coisas.
# Aqui vamos pegar o nome completo, colocar em maiúsculas, minúsculas, separar o primeiro nome
# e medir quantos caracteres ele possui, tudo usando funções e métodos de strings

print('*' *30)
print(f"{'Python Mundo 1 - Desafio 22':^30}")
print('*' *30)

nome = input("Digite seu nome completo")

nomeCaixaAlta = nome.upper()
nomeCaixaBaixa = nome.lower()
nomeSemEspacos = nome.replace(" ", "")
nomeCompleto = nome.split()
primeiroNome = nomeCompleto[0]
letrasPrimeiroNome = len(primeiroNome)

print("Em maiúsculas", nomeCaixaAlta)
print("Em minúsculas", nomeCaixaBaixa)
print("Sem espaços", nomeSemEspacos)
print("Primeiro Nome", primeiroNome)
print("Letras do primeiro nome", letrasPrimeiroNome)

print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)