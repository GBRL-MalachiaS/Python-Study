"""
12. Crie uma função que calcula o fatorial de um número (sem recursão).
"""

def fatorial(n):
    aux = n 
    n -= 1
    soma = aux * n
    if n == 1:
        return soma
    
    fatorial(n)
    

numero = input("Digite um numero: ")

try:
    numero = int(numero)
    fatorial(numero)
except ValueError:
    print(f"ERRO: Valor digitado [{numero}] é invalido, DIGITE UM NUMERO!")