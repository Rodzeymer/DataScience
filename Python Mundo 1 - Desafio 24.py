nomeCidade = input('Digite o nome da sua cidade')

santo = "Santo"
cidadeIniciaComSanto = nomeCidade.startswith(santo)

if cidadeIniciaComSanto:
    print('O nome da sua cidade começa com Santo')
else:
    print('O nome da sua cidade não começa com Santo')