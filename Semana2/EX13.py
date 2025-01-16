"""
 **Desafio:** Escreva um programa que simule uma calculadora simples. O programa deve oferecer ao usuário um menu com as opções de soma, subtração, multiplicação, divisão e sair.
 Após o usuário escolher a operação, ele deve digitar dois números, e o programa deve calcular e exibir o resultado. O programa deve permitir que o usuário faça quantos cálculos quiser até escolher a opção de sair.
"""


def soma(x, y):
    return x + y


def subtracao(x, y):
    return x - y


def multiplicacao(x, y):
    return x * y


def divisao(x, y):
    return x / y


while True:

    operacao = input("Digite a operação [+], [-], [*] e [/]: ")
    operacoes = ["+", "-", "*", "/"]

    if operacao not in operacoes:
        print("Valor digitado é invalido, programa finalizado.")
        break

    numero1 = float(input("Valor 1: "))
    numero2 = float(input('Valor 2: '))

    if operacao == '+':
        print(f'{numero1} + {numero2} = {soma(numero1, numero2)}')
    elif operacao == '-':
        print(f'{numero1} + {numero2} = {subtracao(numero1, numero2)}')
    elif operacao == '*':
        print(f'{numero1} + {numero2} = {multiplicacao(numero1, numero2)}')
    elif operacao == '/':
        print(f'{numero1} + {numero2} = {divisao(numero1, numero2)}')

    opcao = input("Deseja fazer outra operação: [S] ou [N]: ").upper()

    if opcao == 'S':
        continue
    elif opcao == 'N':
        break
    else:
        print('Opcao Invalida, programa reiniciado')
