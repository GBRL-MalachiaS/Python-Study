"""

5. **Exercício 5:** Dada a frase `"Python é uma linguagem de programação divertida"`, faça o seguinte:
   - Substitua a palavra "divertida" por "incrível".
   - Encontre o índice da palavra "linguagem" na frase.
   - Divida a frase em uma lista de palavras.

"""

frase = "Python é uma linguagem de programação divertida"
# - Substitua a palavra "divertida" por "incrível".

print(frase.replace("divertida", "incrivel"))

# - Encontre o índice da palavra "linguagem" na frase.
print(frase.find("linguagem"))

# - Divida a frase em uma lista de palavras.
print(frase.split())
