"""

2. **Exercício 2:** Dada a lista `frutas = ['maçã', 'banana', 'uva', 'abacaxi', 'laranja']`, faça o seguinte:
   - Adicione a fruta 'manga' ao final da lista.
   - Insira a fruta 'kiwi' na posição 2.
   - Remova a fruta 'banana' da lista.
   - Ordene a lista em ordem alfabética.
   
"""

frutas = ['maçã', 'banana', 'uva', 'abacaxi', 'laranja']

# - Adicione a fruta 'manga' ao final da lista.
frutas.append('manga')
print(frutas)
# - Insira a fruta 'kiwi' na posição 2.
frutas.insert(1, 'kiwi')
print(frutas)
# - Remova a fruta 'banana' da lista.
frutas.remove('banana')
print(frutas)
# - Ordene a lista em ordem alfabética.
frutas.sort()
print(frutas)
