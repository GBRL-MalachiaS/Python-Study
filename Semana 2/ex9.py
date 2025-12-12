"""
9. Crie um programa que imprime todos os números pares entre 1 e 50.
"""

for pares in range(0, 51):
    if pares % 2 == 0:
        print(pares)


par = 0
while par <= 50:
    if par % 2 == 0:
        print(par)
    par+=1