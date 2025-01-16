"""
5. **Exercício 5:** Crie uma tupla com 5 nomes de pessoas. Em seguida:
   - Exiba a tupla ordenada em ordem alfabética.
   - Verifique se um determinado nome (fornecido pelo usuário) está presente na tupla.
   
"""
nomes = ("Gabriel", "Gemildo", "Paulete", "Filipe", "Luis",)

#   - Exiba a tupla ordenada em ordem alfabética.
print(tuple(sorted(nomes)))

nome = input("Consultar pessoa, na tupla: ")

if nome in nomes:
    print(f"A pessoa está na tupla: {nome}")

else:
    print(f"A pessoa não está na tupla: {nome}")
