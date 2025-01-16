"""
7. **Exercício 7:** Crie uma classe chamada `Funcionario` que tenha os atributos `nome` e `salario`. Em seguida, crie uma subclasse chamada `Gerente`, que herda de `Funcionario` 
e tenha um atributo adicional chamado `departamento`. O `Gerente` deve ter um método chamado `exibir_detalhes()` que exiba todas as informações (nome, salário e departamento).
   - Crie um objeto da classe `Gerente` e exiba os detalhes.

"""


class Funcionario:
    def __init__(self, nome: str, salario: float) -> None:
        self.nome = nome
        self.salario = salario


class Gerente(Funcionario):
    def __init__(self, nome: str, salario: float, departamento: str) -> None:
        # Chama o construtor da superclasse (Funcionario)
        super().__init__(nome, salario)
        # Atributo específico da classe Gerente
        self.departamento = departamento

    def exibir_detalhes(self) -> None:
        print(f'Colaborador: {self.nome}\nDepartamento: {
              self.departamento}\nSalário: R${self.salario:.2f}')


# Criando um objeto da classe Gerente
colab = Gerente("Gabriel", 1225.65, "Comercial")
colab.exibir_detalhes()
