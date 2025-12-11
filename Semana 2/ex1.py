"""
1. Escreva um programa que verifica se um número é positivo usando `if`.
"""

numero = input("Escreva um numero: ")
try:
    numero = int(numero)
    if numero >= 0:
        print(f"o numero [{numero}] é positivo")
    else:
        print(f"o numero [{numero}] é")
except ValueError:
    print(f"ERRO: Valor fornecido para o numero é do tipo{type(numero).__str__}, por favor informe um numero! ")

