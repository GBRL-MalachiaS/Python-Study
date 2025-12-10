"""
15. Peça ao usuário um número e converta esse valor para todos os tipos básicos possíveis (int, float, str, bool).

"""

numero = input("Digite um numero: ")
numero = int(numero)
print(f'inteiro: [{numero}] - Tipo: [{type(numero)}]')
numero = float(numero)
print(f'Float: [{numero}] - Tipo: [{type(numero)}]')
numero = str(numero)
print(f'String: [{numero}] - Tipo: [{type(numero)}]')
numero = bool(numero)
print(f'Boleano: [{numero}] - Tipo: [{type(numero)}]')