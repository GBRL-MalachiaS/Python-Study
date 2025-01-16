"""
1. **Exercício 1:** Crie uma classe chamada `Pessoa` que tenha os seguintes atributos:
   - `nome`, `idade` e `email`.
   - Crie um método chamado `apresentar()` que exiba uma mensagem com o nome, a idade e o e-mail da pessoa.
   - Crie dois objetos dessa classe e utilize o método `apresentar()` para exibir as informações de cada pessoa.
"""


class Pessoa:

    def __init__(self, nome, idade, email):
        self.nome = nome
        self.idade = idade
        self.email = email

    def apresentar(self):
        print(f"Nome: {self.nome}\nIdade: {self.idade}\nE-mail: {self.email}")


pessoa1 = Pessoa("Gabriel", 29, "gbl.malachias@gmail.com")
pessoa2 = Pessoa("Ariane", 24, "Arika_123@hotmail.com")

pessoa1.apresentar()
pessoa2.apresentar()
