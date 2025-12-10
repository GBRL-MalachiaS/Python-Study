"""
17. Leia um valor e verifique se é numérico usando tratamento com `try/except`.
"""

valor = input("Digite um valor: ")
try:
    valor = int(valor)
except ValueError:
    print(f'Não é possivel transformar o valor [{valor}] em um numero inteiro, pois ele é uma [{type(valor)}]')