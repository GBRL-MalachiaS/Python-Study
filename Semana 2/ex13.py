"""
13. Implemente a tabuada de um número informado pelo usuário.
"""

def tabuada(n):
    for numero in range(1,11):
        print(f'{n} x {numero} = {n*numero}')
        

numero = 4
tabuada(numero)