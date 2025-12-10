"""
2. **Exercício 2:** 
Crie uma classe `Pessoa` com os atributos `nome` e `idade`. Em seguida, crie uma classe `Trabalhador` com o atributo `salario`. 
Crie uma terceira classe `Funcionario`, que herde tanto de `Pessoa` quanto de `Trabalhador`.
Crie um objeto da classe `Funcionario` e exiba as informações do nome, idade e salário.
"""


class Pessoa:
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade


class Trabalhador:
    def __init__(self, salario: float) -> None:
        self.salario = salario


class Funcionario(Trabalhador, Pessoa):
    def __init__(self, salario: float, nome: str, idade: int) -> None:
        Pessoa.__init__(self, nome, idade)
        Trabalhador.__init__(self, salario)

    def exibir_dados(self):
        print(f'Nome: {self.nome}')
        print(f'Salario: R${self.salario}')
        print(f'Idade: {self.idade}')


funcionario1 = Funcionario(2563.35, "Gabriel Malachias", 30)
funcionario1.exibir_dados()
