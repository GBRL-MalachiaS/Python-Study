"""
9. **Exercício 9:** Faça um programa que leia um arquivo texto e substitua todas as ocorrências de uma palavra específica por outra, salvando o resultado em um novo arquivo.
   - **Dica:** Crie o arquivo `texto_original.txt` com algum conteúdo de exemplo e faça as substituições.

"""

with open('texto_original.txt', "r") as texto:
    conteudo = texto.read().lower()
    palavras_trocadas = conteudo.replace("a", "@@@")

    with open("novo_texto.txt", 'w') as texto_novo:
        texto_novo.write(palavras_trocadas)
