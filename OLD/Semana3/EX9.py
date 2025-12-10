"""
9. **Exercício 9:** Crie dois conjuntos de números inteiros. O primeiro conjunto deve conter os números pares de 1 a 10, e o segundo deve conter os números ímpares de 1 a 10.
Em seguida:
   - Exiba a união dos dois conjuntos.
   - Exiba a interseção dos dois conjuntos (deve ser vazia).
   - Exiba a diferença entre o conjunto de números pares e o de ímpares.

"""

a = set()
b = set()

for n in range(1,11):
    if n % 2 == 0:
       a.add(n)

    if n == 1:
      b.add(n)
   
    if n % 3 == 0:
       if n % 2 == 0:
         continue
       
       else:
          b.add(n)

print(a, b)
print(f'Interseção A e B: {a.intersection(b)}')
print(f'Diferença entre A e B: {a - b} e {b-a}')