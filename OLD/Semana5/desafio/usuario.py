class Usuario:
    def __init__(self, leitor: str, emprestimo=None) -> None:
        self.leitor = leitor
        self.emprestimo = emprestimo

    def __repr__(self) -> str:
        if self.emprestimo == None:
            return f'Usuário: {self.leitor} - Emprestimo: Sem Emprestimo'
        else:
            return f'Usuário: {self.leitor} - Emprestimo: {self.emprestimo}'
