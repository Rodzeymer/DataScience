# Nesta primeira aula vamos perguntar pro usu´rio informações simples e retorná-las concatenadas em uma 
# única string

print('*' *30)
print(f"{'Python Mundo 1 - Aula 01':^30}")
print('*' *30)

nome = input('Qual o seu nome?')
idade = input('Qual a sua idade?')
peso = input('Quanto você pesa?')

print('O funcionário ',nome, 'tem ', idade, ' anos de idade e pesa '
, peso, ' quilos.')
print('*' *30)
