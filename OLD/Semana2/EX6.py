"""
**Exercício 6:** Crie um programa que peça ao usuário um número inteiro positivo e calcule a soma de todos os números inteiros de 1 até o número informado.

"""
# Com While
numero = int(input("Digite um numero inteiro: "))
contador = 0
soma = 0

while numero > contador:
    contador += 1
    soma += contador

print(soma)

# Com for
soma = 0
for n in range(numero+1):
    soma += n

print(soma)
