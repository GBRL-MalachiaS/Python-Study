"""
17. Escreva uma função que calcula a sequência de Fibonacci usando recursão.

"""
def fibonacci(n):

    if n == 1:
        return
    
    return fibonacci(n-1)

numero = fibonacci(10)

print(numero)