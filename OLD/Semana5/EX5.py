"""

5. **Exercício 5:** Crie uma classe chamada `Livro` que tenha os seguintes atributos:
   - `titulo`, `autor`, `paginas`.
   - Crie um método construtor que inicialize esses atributos.
   - Crie um método chamado `detalhes()` que exiba as informações do livro.
   - Crie três objetos dessa classe e exiba os detalhes de cada livro.

"""


class Livros:
    def __init__(self, titulo: str, autor: str, paginas: int) -> None:
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def detalhes(self) -> str:
        print(f'O livro {self.titulo} do autor {
              self.autor} possui {self.paginas} paginas')


livro1 = Livros("Memoria Postunas", "Bras Cubas", 256)
livro2 = Livros("Guerras dos Tronos", "RR Martin", 780)
livro3 = Livros("Mentiram Muito para mim", "Flavio Quintilha", 210)

livro1.detalhes()
livro2.detalhes()
livro3.detalhes()
