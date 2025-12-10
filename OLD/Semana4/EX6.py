"""
6. **Exercício 6:** Crie um arquivo chamado `nomes.txt` e escreva nele o nome de 5 pessoas, uma em cada linha. Em seguida:
   - Leia o arquivo e exiba o conteúdo na tela.
   - Adicione mais 2 nomes ao arquivo e exiba o conteúdo atualizado.
"""
# - Leia o arquivo e exiba o conteúdo na tela.
with open("nome.txt", "r") as file:
    print(file.read())

# - Adicione mais 2 nomes ao arquivo e exiba o conteúdo atualizado.
with open("nome.txt", "a") as file:
    file.seek(0, 2)
    if file.tell() > 0:
        file.write("Juninhos\n")
        file.write("Jorginho\n")

with open("nome.txt", "r") as file:
    print(file.read())
