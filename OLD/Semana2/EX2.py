"""
    **Exercício 2:** Crie um programa que pergunte ao usuário três números e determine qual deles é o maior.
"""
lista_numeros = []
maior = 0
for numero in range(3):
    numero = int(input("Digite um numero: "))
    lista_numeros.append(numero)

for x in lista_numeros:

    if maior < x:
        maior = x

print(maior)
