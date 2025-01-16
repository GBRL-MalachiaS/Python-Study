"""
**Desafio:** Crie um sistema de gerenciamento de biblioteca com as seguintes classes:
- **Livro**: Contém título, autor e status (disponível ou emprestado).
- **Usuario**: Contém nome e uma lista de livros emprestados.
- **Biblioteca**: Gerencia os livros e os usuários. Deve permitir:
  - Adicionar livros.
  - Emprestar livros para usuários.
  - Devolver livros.
  - Exibir todos os livros e seus status.
  - Exibir os usuários e os livros que eles emprestaram.

"""
from biblioteca import Biblioteca
import os


def limpa_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


# inicia a instancia da biblioteca.
biblioteca = Biblioteca()

# adiciona livros padrões do sistema.
biblioteca.adiciona_livro("machado de assis", "dom casmurro")
biblioteca.adiciona_livro("guimarães rosa", "grande sertão")
biblioteca.adiciona_livro("paulo coelho", "o alquimista")
biblioteca.adiciona_livro("graciliano ramos", "vidas secas")
biblioteca.adiciona_livro("jorge amado", "capitaes da areia")
biblioteca.adiciona_livro(
    "machado de assis", "memorias postumas de bras cubas")
biblioteca.adiciona_livro("ariano suassuna", "o auto da compadecida")
biblioteca.adiciona_livro("joaquim manuel de macedo", "a moreninha")
biblioteca.adiciona_livro("jose de alencar", "iracema")
biblioteca.adiciona_livro("clarice lispector", "a hora da estrela")

# adciona leitores padrão no sistema.
biblioteca.adiciona_usuario("gabriel")
biblioteca.adiciona_usuario("ariane")
biblioteca.adiciona_usuario("filipe")
biblioteca.adiciona_usuario("lorena")
biblioteca.adiciona_usuario("luis")
biblioteca.adiciona_usuario("angela")
biblioteca.adiciona_usuario("genildo")
biblioteca.adiciona_usuario("paulo")
biblioteca.adiciona_usuario("geraldo")

limpa_tela()

while True:

    print("---------- Menu ----------")
    print("1 - Adicionar Livros")
    print("2 - Adicionar Leitores")
    print("3 - Emprestimo de Livros")
    print("4 - Devolução ")
    print("5 - Exibir todos os livros e Status de Emprestimo")
    print("6 - Exibir Leitores x Livros Emprestados")
    print("7 - Sair")
    print("--------------------------")
    opcao = input("Opção: ")
    print("--------------------------")

    try:  # Corrige a excessão se o usuário digita algo diferente de um numero
        opcao = int(opcao)

        if opcao >= 8 or opcao <= 0:
            print(
                "Opção digitada não existe, por favor, escolha um numero do menu de 1 a 6")

            input("Precione qualquer tecla para continuar")
            limpa_tela()
            continue

        match opcao:
            case 1:  # Adicionar Livros - Status: Concluido

                autor = input("Digite o nome do autor: ").lower()
                livro = input("Digite o nome do livro: ").lower()
                biblioteca.adiciona_livro(autor, livro)

            case 2:  # Adiciona Leitores - Status: Concluido

                leitor = input("Digite o nome do leitor: ").lower()
                biblioteca.adiciona_usuario(leitor)

            case 3:  # Emprestimo de Livros - Status: Concluida

                limpa_tela()
                leitor = input("Digite o leitor: ").lower()
                titulo = input("Digite o titulo que será emprestado: ").lower()
                biblioteca.empresta_livro(leitor, titulo)

                input("\nPrecione qualquer tecla!")
                limpa_tela()

            case 4:  # Devolução de Livros - Status: Concluido

                limpa_tela()
                leitor = input("Digite o leitor: ").lower()
                titulo = input("Digite o titulo que será emprestado: ").lower()
                biblioteca.devolver_livro(leitor, titulo)

                input("\nPrecione qualquer tecla!")
                limpa_tela()

            case 5:  # Exibe o status de todos os livros - Status: Concluido

                limpa_tela()
                biblioteca.exibir_livros()
                input("\nPrecione qualquer tecla!")
                limpa_tela()

            case 6:  # Exibe os leitores que estão com os livros emprestados - Status Em produção

                limpa_tela()
                biblioteca.livros_alugados()
                input("\nPrecione qualquer tecla!")
                limpa_tela()

            case 7:  # Finaliza o programa - Status Concluido
                break

    except ValueError:
        print("Valor digitado para opção é invalido! Digite um numero entre 1 a 7")
