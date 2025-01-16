"""
**Exercício 3:** Escreva um programa que leia a idade do usuário e exiba uma mensagem dizendo se ele é menor de idade 
(menos de 18 anos), adulto (entre 18 e 64 anos), ou idoso (65 anos ou mais).
"""

idade = int(input("Digite sua idade: "))

if idade >= 18 and idade <= 64:
    print("Adulto")
elif idade > 65:
    print("Idoso")
else:
    print("Menor de idade")
