from livro import Livro
from usuario import Usuario


class Biblioteca:

    def __init__(self) -> None:
        self.livros = {}
        self.leitores = {}

    # Metodos para acrescentar e exibir o livro e seus status

    def adiciona_livro(self, autor, titulo):

        if len(self.livros) == 0:
            livro = Livro(autor, titulo)
            self.livros.update({titulo: livro})
            print(f'O livro {titulo} do autor {
                  autor}, foi adicionado com sucesso')
        else:

            if self.existe_livro(titulo):
                print(f'O titulo {livro.titulo} do autor {
                    livro.autor}, já consta cadastrado na biblioteca!')
            else:
                livro = Livro(autor, titulo)
                self.livros.update({titulo: livro})
                print(f'O livro {titulo} do autor {
                    autor}, foi adicionado com sucesso')

    def existe_livro(self, titulo):
        for l in self.livros:
            if titulo == l:
                return True
        return False

    def exibir_livros(self):
        if self.livros:
            print("Livros Cadastrados:")

            for l in self.livros:
                print(self.livros[l])

    # Metodos para acrescentar o usuário

    def adiciona_usuario(self, leitor):

        if len(self.leitores) == 0:
            usuario = Usuario(leitor)
            self.leitores.update({leitor: usuario})
        else:
            if self.existe_leitor(leitor):
                print(f'O leitor {leitor}, já existe cadastrado')
            else:
                usuario = Usuario(leitor)
                self.leitores.update({leitor: usuario})
                print(f'O leitor {leitor}, foi adicionado com sucesso')

    def existe_leitor(self, leitor):

        for l in self.leitores:
            if leitor == l:
                return True
        return False

    def exibir_leitores(self):
        if self.leitores:
            print("Leitores Cadastrados:")

            for l in self.leitores:
                print(self.leitores)

    def livros_alugados(self):
        for l in self.leitores:
            leitor = self.leitores[l]
            if leitor.emprestimo is not None:
                print(leitor)
    # Metodos para locação / devolução de livros.

    def empresta_livro(self, leitor, titulo):
        if self.existe_leitor(leitor) and self.existe_livro(titulo):
            # acessa o titulo e adiciona a uma variavel para alterar o status do livro
            livro = self.livros[titulo]

            if livro.status is not None:
                print(f'O Livro {livro.titulo}, já está em emprestimo !')
            else:
                livro.status = leitor

            # Acessa o leitor e adiciona o livro que está em emprestimo.
            leitor = self.leitores[leitor]

            if leitor.emprestimo is not None:
                print(f'O Leitor já possui um livro emprestado, por favor, realizar a devolução do titulo: {
                    leitor.emprestimo}')
            else:
                leitor.emprestimo = titulo
                print(f"Emprestimo do titulo '{
                    livro.titulo}' realizado para o leitor '{leitor.leitor}'")
        else:
            print(f'Por favor, validar os cadastros do leitor: {
                  leitor} | titulo: {titulo}')

    def devolver_livro(self, leitor, titulo):

        if self.existe_leitor(leitor) and self.existe_livro(titulo):
            # acessa o titulo e adiciona a uma variavel para alterar o status do livro
            livro = self.livros[titulo]

            if livro.status == leitor:
                livro.status = None

            # Acessa o leitor e adiciona o livro que está em emprestimo.
            leitor = self.leitores[leitor]

            if leitor.emprestimo == titulo:
                leitor.emprestimo = None

            print(f'Feita a devolução do {
                  livro.titulo} que estava com o leitor {leitor.leitor}')
        else:
            print(f'Por favor, validar os cadastros do leitor: {
                  leitor} | titulo: {titulo}')
