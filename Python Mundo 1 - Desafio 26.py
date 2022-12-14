import unicodedata


nome = input('O nome completo de uma pessoa')
nomeNormalize = unicodedata.normalize(nome)

print(nomeNormalize)

https://docs.python.org/3/library/unicodedata.html