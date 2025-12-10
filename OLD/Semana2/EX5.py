"""
**Exercício 5:** Escreva um programa que exiba todos os números pares de 1 a 50.
"""

for x in range(0, 51, 2):
    print(x)

for n in range(51):
    if n % 2 == 0:
        print(n)
