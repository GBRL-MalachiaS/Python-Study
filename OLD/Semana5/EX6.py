"""
6. **Exercício 6:** Crie uma classe chamada `Animal` com um método `emitir_som()`, que exibe uma mensagem genérica como "O animal está emitindo um som". Depois, crie duas subclasses:
   - `Cachorro`: Deve sobrescrever o método `emitir_som()` para exibir "O cachorro está latindo".
   - `Gato`: Deve sobrescrever o método `emitir_som()` para exibir "O gato está miando".
   - Crie objetos das subclasses e chame o método `emitir_som()` para cada um.
"""


class Animal:
    def __init__(self, nome: str) -> None:
        self.nome = nome

    def emitir_som(self):
        print(f'{self.nome} um animal qualquer está emitindo o som')


class Gato(Animal):
    def emitir_som(self):
        print(f'O gato {self.nome} está miando')


class Cachorro(Animal):
    def emitir_som(self):
        print(f'O Cachorro {self.nome} está latindo')


dog = Cachorro("Rex")
cat = Gato("Gatuno")

dog.emitir_som()
cat.emitir_som()
