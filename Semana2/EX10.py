"""
**Exercício 10:** Crie uma função chamada `calcula_fatorial(numero)` que receba um número inteiro positivo e retorne o fatorial desse número.

"""


def calcula_fatorial(numero):
    contador = 1
    fatorial = 1
    while numero >= contador:
        fatorial *= contador
        contador += 1

    return f'Fatorial de {numero}! = {fatorial}'


print(calcula_fatorial(numero=4))
