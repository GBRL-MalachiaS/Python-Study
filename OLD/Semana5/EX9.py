"""
9. **Exercício 9:** Crie uma classe chamada `Aluno` com os atributos `nome` e `nota` (nota deve ser privada). A classe deve ter os métodos:
   - `set_nota(nova_nota)`: Altera a nota do aluno (use validação para garantir que a nota está entre 0 e 10).
   - `get_nota()`: Retorna a nota atual.
   - `exibir_detalhes()`: Exibe o nome e a nota do aluno.
   - Crie um objeto da classe e teste os métodos.

"""


class Aluno:

    def __init__(self, nome: str, nota: float) -> None:
        self.nome = nome
        self.__nota = nota

    @property
    def nota(self):
        return self.__nota

    @nota.setter
    def nota(self, novanota: float) -> float:

        try:
            novanota = float(novanota)
            if novanota >= 0 and novanota <= 10:
                self.__nota = novanota
            else:
                print("Nota invalida")

        except ValueError:
            print("O valor digitado é invalido! Digite uma nota valida!")

    def exibir_detalhes(self):
        print(f'O aluno: {self.nome}, nota atual: {self.__nota}')


aluno1 = Aluno("Gabriel Malachias", 5.5)
aluno1.exibir_detalhes()
aluno1.nota = 8.5
aluno1.exibir_detalhes()
