"""
9. **Exercício 9:** Escreva uma função chamada `eh_par(numero)` que receba um número inteiro como argumento e retorne `True` se o número for par ou `False` se for ímpar.
"""


def eh_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False


numero = 1

print(eh_par(numero))
