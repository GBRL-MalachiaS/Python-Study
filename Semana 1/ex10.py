"""
10. Peça ao usuário um número e retorne se ele é par ou ímpar (sem usar condicionais ainda, apenas com operadores).
"""

numero = int(input("Digite um número: "))

resultado = ("Par", "Ímpar")[numero % 2]
print(f"O número {numero} é {resultado}.")
