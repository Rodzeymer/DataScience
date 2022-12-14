import unicodedata


nome = input('Escreva uma frase')
nomeNormalize = unicodedata.normalize('NFKD', nome).encode('ASCII', 'ignore').decode('ASCII')
nomeCaixaBaixa = nomeNormalize.lower()

quantosA = nomeCaixaBaixa.count('a') 
quandoPrimeiroA = nomeCaixaBaixa.find('a')+1
quandoUltimoA = nomeCaixaBaixa.rfind('a')+1

print('A palavara {} possui {} letras A'.format(nomeCaixaBaixa, quantosA))
print('O primeiro A de {} é a {}ª letra'.format(nomeCaixaBaixa, quandoPrimeiroA))
print('O último A de {} é a {}ª letra'.format(nomeCaixaBaixa, quandoUltimoA))