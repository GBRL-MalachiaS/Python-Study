"""
    6. **Exercício 6:** Crie um dicionário que armazene as informações de 3 produtos, onde a chave é o nome do produto e o valor é o preço. Em seguida:
   - Exiba o nome e o preço de todos os produtos.
   - Permita que o usuário altere o preço de um dos produtos.
   - Exiba o dicionário atualizado.

"""


produtos = {"Coca": 8.30, "Feijão": 6.50, "Mandioca": 8.6}


#   - Exiba o nome e o preço de todos os produtos.
for n in produtos:
    print(f'Item: {n} - R${produtos[n]} ')

#   - Permita que o usuário altere o preço de um dos produtos.
x = input("Digite o item do que deseja alterar o preço: ")

if x in produtos:
    print(f'Item: {x} - R${produtos[x]}')

    novo_valor = float(input("Digite um novo valor: "))
    produtos[x] = novo_valor

#   - Exiba o dicionário atualizado.

for n in produtos:
    print(f'Item: {n} - R${produtos[n]} ')
