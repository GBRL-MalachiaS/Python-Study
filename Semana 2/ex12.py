"""
12. Crie uma função que calcula o fatorial de um número (sem recursão).
"""

def fatorial(n):
    fator = n
    for num in range(n-1,0,-1):
        fator =  fator * n
        print(fator)

numero = input("Digite um numero: ")

try:
    numero = int(numero)
    fatorial(numero)
except ValueError:
    print(f"ERRO: Valor digitado [{numero}] é invalido, DIGITE UM NUMERO!")