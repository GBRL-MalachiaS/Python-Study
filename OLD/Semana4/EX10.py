"""
10. **Exercício 10:** Crie um programa que abra um arquivo de texto e remova todas as linhas vazias do arquivo. Salve o resultado em outro arquivo.

"""
with open("texto_original.txt", "r", encoding="UTF-8") as texto:
    linhas = texto.readlines()
    with open("texto_novo.txt", "w", encoding="UTF-8") as novo_texto:
        for n in linhas:
            if n == "\n":
                continue
            novo_texto.write
