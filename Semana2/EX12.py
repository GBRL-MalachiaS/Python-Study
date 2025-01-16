"""
**Exercício 12:** Escreva uma função chamada `eh_primo(numero)` que receba um número inteiro e retorne `True` se ele for um número primo, ou `False` caso contrário. 
Em seguida, crie um programa que peça ao usuário um número e informe se ele é primo ou não, utilizando a função.

"""

import math


def eh_primo(numero):

    if numero <= 1:
        return False

    for i in range(2, int(math.sqrt(numero)) + 1):
        if numero % i == 0:
            return False
    return True


numero = 29
if eh_primo(numero):
    print(f"{numero} é primo.")
else:
    print(f"{numero} não é primo.")
