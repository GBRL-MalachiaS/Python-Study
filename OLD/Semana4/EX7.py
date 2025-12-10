"""
7. **Exercício 7:** Escreva um programa que leia um arquivo texto contendo números inteiros (um por linha), calcule a soma desses números e exiba o resultado.
   - **Dica:** Primeiro, crie o arquivo `numeros.txt` com alguns números inteiros.
"""

with open("inteiros.txt", "r") as inteiros:
    numeros = inteiros.readlines()
    soma = 0
    for n in numeros:
        soma += int(n)
    print(f"Soma dos numeros da lista: {soma}")
