"""
Exercício 1: Escreva um programa que pergunte ao usuário um número inteiro e exiba uma mensagem indicando se o número é positivo, negativo ou zero.
"""
numero = int(input('Digite um numero: '))

if numero > 0:
    print('Numero é positivo')
elif numero < 0:
    print("Numero é negativo")
else:
    print('Numero igual a zero')
