"""
11.Use `while` para pedir um número até que o usuário digite 0.
"""

while True:
    numero = input('Digite um numero: ')
    try:
        numero = int(numero)
        print(f"Numero digitado [{numero}]")
        if numero == 0:
            break
        
    except ValueError:
        print(f"ERROR: Valor digitado [{numero}] é invalido digite um numero!")