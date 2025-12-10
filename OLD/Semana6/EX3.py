"""
3. **Exercício 3:** Crie uma classe `Animal` com o método `emitir_som()`. Depois, crie três subclasses:
   - `Cachorro`: que sobrescreve o método `emitir_som()` para exibir `"O cachorro está latindo"`.
   - `Gato`: que sobrescreve o método `emitir_som()` para exibir `"O gato está miando"`.
   - `Vaca`: que sobrescreve o método `emitir_som()` para exibir `"A vaca está mugindo"`.
   
   Crie uma função chamada `fazer_barulho()` que receba um objeto do tipo `Animal` e chame o método `emitir_som()`. Teste com cada uma das subclasses.
   
"""


class Animal:
    def __init__(self, nome: str) -> None:
        self.nome = nome
        
    def emitir_som(self):
        print(f'O animal {self.nome} está emitindo som')
    
    
class Cachorro(Animal):
    def emitir_som(self):
        print(f'O Cachorro {self.nome} está latindo')
        
class Gato(Animal):
    def emitir_som(self):
        print(f'O Gato  {self.nome} está miando')
        
class Vaca(Animal):
    def emitir_som(self):
        print(f'O Vaca {self.nome} está mugindo')


def fazer_barulho(animal):
    return animal.emitir_som()


cachorro = Cachorro("Rex")
gato = Gato("miau miau")
vaca = Vaca("vacoza")


fazer_barulho(cachorro)
fazer_barulho(gato)
fazer_barulho(vaca)
