# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]


def zipper(lista1, lista2):
    cidade_sigla = []
    for n, i in zip(lista2, lista1):
        cidade_sigla.append((n, i))
    return cidade_sigla


cidade = ['Salvador', 'Ubatuba', 'Belo Horizonte',
          'Rio de Janeiro', ]
sigla = ['BA', 'SP', 'MG', 'RJ', 'EUA', 'CHN']

print(zipper(cidade, sigla))
