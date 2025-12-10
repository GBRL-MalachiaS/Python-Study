"""
12. Escreva um programa que calcule o IMC usando valores inseridos pelo usuário.
"""
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura**2)
print(f'Seu IMC é de [{imc}]')