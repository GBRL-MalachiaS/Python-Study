"""
**Desafio:** Crie um programa que funcione como um simples editor de texto. O programa deve permitir ao usuário:
- Abrir um arquivo existente.
- Adicionar mais conteúdo ao arquivo.
- Exibir o conteúdo atualizado do arquivo.
- Fechar o programa.

"""
import os
import sys

while True:
    # Exibe todos os arquivos que existem no diretório local e transforma em lista
    lista_de_arquivos = os.listdir('.')
    qtd_arquivos = len(lista_de_arquivos)

    # Cria as opções de arquivos para seleção do usuário
    for n in range(qtd_arquivos):
        print(f'{n} - {lista_de_arquivos[n]}')

    # Seleciona o arquivo
    try:
        arquivo_selecionado = int(
            input("Digite o código do arquivo que deseja alterar: "))

        # Valida a opção selecionada
        if arquivo_selecionado < 0 or arquivo_selecionado >= qtd_arquivos:
            print(f'O valor digitado é inválido. Por favor, digite um valor entre 0 e {
                  qtd_arquivos - 1}')
            continue
    except ValueError:
        print("Erro: Você deve digitar um número válido.")
        continue

    # Define as opções para edição do arquivo
    while True:
        arquivo = lista_de_arquivos[arquivo_selecionado]
        print(f'\nArquivo ({arquivo}) selecionado')
        print("O que deseja fazer com o arquivo? \n"
              "1 - Editar arquivo\n"
              "2 - Exibir o arquivo\n"
              "3 - Selecionar outro arquivo\n"
              "4 - Fechar")

        try:
            opcao = int(input("Digite a opção: "))

            if opcao == 1:
                print(
                    "Digite o conteúdo que deseja adicionar ao arquivo (pressione Enter para finalizar):")
                with open(arquivo, 'a', encoding="UTF-8") as texto:
                    while True:
                        linha = input()
                        if linha == "":  # Sai do loop se o usuário pressionar Enter sem digitar nada
                            break
                        texto.write(linha + '\n')  # Adiciona nova linha

            elif opcao == 2:
                print("\nConteúdo do arquivo:")
                with open(arquivo, 'r', encoding="UTF-8") as texto:
                    print(texto.read())
                print("\n")

            elif opcao == 3:
                break

            elif opcao == 4:
                sys.exit()

            else:
                print("Opção inválida, selecione novamente.")

        except ValueError:
            print("Erro: Digite uma opção numérica válida.")
