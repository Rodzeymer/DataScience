# Manipular um número possui duas formas, tratar com fórmulas matemáticas e operadores, 
# que economiza muito código, ou transformar em string, 'parseando' (str()) para string,
# o que nesse caso ocupa muitas linhas, e tratando como número facilita muito.
# Aqui demonstramos o poder da MateMágica, em poucas linhas conseguimos desmembrar um número
# em milhar, centena, dezena e unidade, dá pra fazer como string, mas demora muito e 
# é mais complicado, mas vale a experiência

print('*' *30)
print(f"{'Python Mundo 1 - Desafio 23':^30}")
print('*' *30)
numero = int(input("Digite um numero de 1 a 9999"))

### MÉTODO EM INTEGER ###
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 %10
milhar = numero // 1000 %10

print('{} milhar, {} centenas, {} dezenas, {} unidades'.format(milhar, centena, dezena, unidade))

### MÉTODO EM STRING ###
# if numero <10:
# 	print('0 milhar, 0 centena, 0 dezena, {} unidades'.format(numero))
	
# elif numero >= 10 and numero <100:
# 	numeroQuebrado=[int(d) for d in str(numero)]
# 	numeroDezena=numeroQuebrado[0]
# 	numeroUnidade=numeroQuebrado[1]
# 	print('0 milhar, 0 centena, {} dezenas, {} unidades'.format(numeroDezena, numeroUnidade))

# elif numero >= 100 and numero <1000:
# 	numeroQuebrado=[int(d) for d in str(numero)]
# 	numeroCentena=numeroQuebrado[0]
# 	numeroDezena=numeroQuebrado[1]
# 	numeroUnidade=numeroQuebrado[2]
# 	print('0 milhar, {} centena, {} dezenas, {} unidades'.format(numeroCentena, numeroDezena, numeroUnidade))
	
# elif numero >= 1000 and numero <10000:
# 	numeroQuebrado=[int(d) for d in str(numero)]
# 	numeroMilhar=numeroQuebrado[0]
# 	numeroCentena=numeroQuebrado[1]
# 	numeroDezena=numeroQuebrado[2]
# 	numeroUnidade=numeroQuebrado[3]
# 	print('{} milhar, {} centena, {} dezenas, {} unidades'.format(numeroMilhar, numeroCentena, numeroDezena, numeroUnidade))
	
# elif numero >= 10000:
# 	print('O numero {} e muito grande!'.format(numero))
print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)