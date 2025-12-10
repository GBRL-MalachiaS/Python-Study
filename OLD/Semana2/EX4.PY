"""
    **Exercício 4:** Escreva um programa que peça ao usuário uma nota (entre 0 e 10) e exiba se ele foi aprovado ou reprovado, considerando que a média de aprovação é 7.0.
    Caso a nota seja inválida (não esteja entre 0 e 10), exiba uma mensagem de erro.

"""

nota = int(input("Digite uma nota: "))

if nota >= 7 and nota <= 10:
    print("Aprovado")
elif nota >= 0 and nota <= 6:
    print("Reprovado")
else:
    print("Nota invalida")
