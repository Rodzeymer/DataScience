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