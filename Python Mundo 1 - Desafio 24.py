# Voltando a tratar de strings, temos como descobrir se em uma string, com vários 
# nomes ou termos, há no começo, fim uma determinada string, ou sub-string, assim 
# como no meio dela, tomando cuidado para evitar falsos positivos.
# Nesse algoritmo o usuário digita o nome de uma cidade e o programa exibe ao final
# do processamento se a cidade começa com santos

print('*' *30)
print(f"{'Python Mundo 1 - Desafio 24':^30}")
print('*' *30)

nomeCidade = input('Digite o nome da sua cidade')
nomeCidadeBaixo = nomeCidade.lower()

santo = "santo"
cidadeIniciaComSanto = nomeCidadeBaixo.startswith(santo)

if cidadeIniciaComSanto:
    print('O nome da sua cidade começa com Santo')
else:
    print('O nome da sua cidade não começa com Santo')
    
print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)