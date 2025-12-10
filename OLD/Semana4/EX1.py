"""
1. **Exercício 1:** Crie um programa que receba uma string do usuário e:
   - Exiba a quantidade de caracteres da string.
   - Exiba a string toda em maiúsculas.
   - Exiba a string toda em minúsculas.
   - Exiba a string com a primeira letra de cada palavra em maiúsculo.
   
"""

texto = input("Digite um texto: ")

# - Exiba a quantidade de caracteres da string.
print(f"Quantidade de caracteres: {len(texto)}")
# - Exiba a string toda em maiúsculas.
print(f"Texto em maiusculo: {texto.upper()}")
# - Exiba a string toda em minúsculas.
print(f'Texto em minuscula: {texto.lower()}')
# - Exiba a string com a primeira letra de cada palavra em maiúsculo.
print(f'texto com as uniciais maiscula: {texto.title()}')
