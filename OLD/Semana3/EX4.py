"""
4. **Exercício 4:** Crie uma tupla com os valores de 1 a 5. Depois, faça o seguinte:
   - Exiba o primeiro e o último valor da tupla.
   - Converta a tupla para uma lista e adicione o número 6.
   - Converta a lista de volta para tupla.
   
"""
inteiros = (1, 2, 3, 4, 5)
# - Exiba o primeiro e o último valor da tupla.
print(f'Primeiro valor: {inteiros[0]} - Ultimo Valor: {inteiros[4]}')
# - Converta a tupla para uma lista e adicione o número 6.
lista = list(inteiros)
lista.append(6)
# - Converta a lista de volta para tupla.
inteiros = tuple(lista)

print(inteiros, type(inteiros))
