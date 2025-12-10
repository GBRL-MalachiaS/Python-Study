"""
1. **Exercício 1:** Crie uma lista de 5 números inteiros fornecidos pelo usuário. Exiba:
   - O maior número da lista.
   - O menor número da lista.
   - A soma de todos os números.
   - A média dos números.
"""

lista_inteiros = []
for n in range(5):
    numero = int(input(f"Digite um numero {n} inteiro: "))
    lista_inteiros.append(numero)

# Maior numero da lista
print(f'Maior: {max(lista_inteiros)}')

# Menor numero da lista
print(f'Menor: {min(lista_inteiros)}')

# Soma da lista
print(f'Soma: {sum(lista_inteiros)}')

# Media dos numeros.
print(f'Media: {sum(lista_inteiros)/len(lista_inteiros)}')
