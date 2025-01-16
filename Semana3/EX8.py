"""
8. **Exercício 8:** Crie um dicionário com os nomes e idades de 5 pessoas. Em seguida:
   - Permita que o usuário adicione mais uma pessoa ao dicionário.
   - Exiba todos os nomes e idades em ordem de inserção.
   - Exiba os nomes das pessoas que têm mais de 30 anos.

"""
pessoas = {
    "Gabriel": 29,
    "Ariane": 34,
    "Lorena": 5,
    "Angela": 55,
    "Aparecida": 69,
}
# - Permita que o usuário adicione mais uma pessoa ao dicionário.

nome = input("Digite o nome: ")
idade = int(input("Digite uma nova idade: "))

pessoas.update({nome: idade})

# - Exiba todos os nomes e idades em ordem de inserção.
for pessoa in pessoas:
    print(f'{pessoa}: {pessoas[pessoa]}')

print("=================")

for pessoa in pessoas:
    if pessoas[pessoa] >= 30:
        print(f'{pessoa}: {pessoas[pessoa]}')
