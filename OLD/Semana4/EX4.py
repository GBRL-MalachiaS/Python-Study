"""
4. **Exercício 4:** Escreva um programa que receba o nome completo do usuário e retorne:
   - O nome com todas as letras maiúsculas.
   - O nome com todas as letras minúsculas.
   - A quantidade de letras do nome (sem contar os espaços).
   - O primeiro nome e a quantidade de letras que ele possui.
   
"""
nome = input("Digite seu nome completo: ")

# - O nome com todas as letras maiúsculas.
print(f"Nome Maiúscula: {nome.upper()}")

# - O nome com todas as letras minúsculas.
print(f"Nome Minuscula: {nome.lower()}")

# - A quantidade de letras do nome (sem contar os espaços).
print(f"Quantidade de Letras: {len(nome.replace(" ", ""))}")

# - O primeiro nome e a quantidade de letras que ele possui.
nome = nome.split()
print(f'Primero nome: {nome[0]} - Quantidade de Letras: {len(nome[0])}')
