class Livro:
    def __init__(self, autor: str, titulo: str, status=None) -> None:

        self.autor = autor
        self.titulo = titulo
        self.status = status

    def __repr__(self) -> str:

        if self.status is not None:
            return f'Autor: {self.autor} - Titulo: {self.titulo} - Status: Alugado'
        else:
            return f'Autor: {self.autor} - Titulo: {self.titulo} - Status: livre'
