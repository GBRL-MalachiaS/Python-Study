"""

3. **Exercício 3:** Crie uma lista com 10 números inteiros e, em seguida:
   - Remova todos os números pares da lista.
   - Exiba a lista resultante.

"""

inteiros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
impares = []

for n in inteiros:

    if n % 2 == 0:
        continue

    impares.append(n)

print(impares)
