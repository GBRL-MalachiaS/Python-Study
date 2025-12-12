"""
10. Faça uma função que receba três números e retorne o maior deles.
"""

def maior_valor(n1,n2,n3):
    lista = [n1,n2,n3]
    maior = 0
    
    for n in lista:
        if n > maior:
            maior = n
    
    return maior


print(maior_valor(12,11,2))
