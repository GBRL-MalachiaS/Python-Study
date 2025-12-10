"""
4. **Exercício 4:** Crie uma classe chamada `Carro` com os atributos `marca`, `modelo` e `ano`. A classe deve ter um método construtor (`__init__`) que inicialize esses
atributos automaticamente quando um objeto da classe for criado. Além disso, crie um método chamado `exibir_informacoes()` que exiba as informações do carro.
   - Crie dois objetos dessa classe e exiba as informações de cada carro.

"""


class Carro:

    def __init__(self, marca: str, modelo: str, ano: int) -> None:
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def exibir_informacoes(self) -> None:

        print(f'Marca: {self.marca}\nModelo: {self.modelo}\nAno: {self.ano}')


carroca1 = Carro("Chevrolet", "Corsa", 2006)
carroca1.exibir_informacoes()
carroca2 = Carro("Fiat", "Argo", 2019)
carroca2.exibir_informacoes()
