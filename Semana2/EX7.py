"""
**Exercício 7:** Escreva um programa que leia um número inteiro e exiba a tabuada de multiplicação desse número de 1 a 10.
"""
tabuada = int(input("Digite o numero da tabuada que deseja saber: "))
# com for


for n in range(11):
    print(f'{tabuada} x {n} = {tabuada*n}')

# com while

print('')

contador = 0
while 11 > contador:
    print(f'{tabuada} x {contador} = {tabuada*contador}')
    contador += 1
