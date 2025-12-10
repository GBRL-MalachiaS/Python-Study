"""
. **Exercício 1:** Crie três classes:
   - `Veiculo`: com os atributos `marca` e `modelo`, e um método `informacoes()` que exibe esses atributos.
   - `Terrestre`: com o atributo `num_rodas` e o método `info_terrestre()` que exibe o número de rodas.
   - `Aquatico`: com o atributo `tipo_embarcacao` e o método `info_aquatico()` que exibe o tipo de embarcação.

   Depois, crie uma classe chamada `Amfibio` que herde de `Veiculo`, `Terrestre` e `Aquatico`. Crie um objeto dessa classe e exiba todas as informações.

"""


class Veiculo:
    def __init__(self, marca: str, modelo: str) -> None:
        self.marca = marca
        self.modelo = modelo

    def informacao(self):
        print(f'Marca: {self.marca} - Modelo: {self.modelo}')


class Terrestre():
    def __init__(self, num_rodas: int) -> None:
        self.num_rodas = num_rodas

    def info_terrestre(self):
        print(f'Numero de rodas: {self.num_rodas}')


class Aquatico():
    def __init__(self, tipo_embarcacao: str) -> None:
        self.tipo_embarcacao = tipo_embarcacao

    def info_aquatico(self,):
        print(f'Tipo de embarcação: {self.tipo_embarcacao}')


class Amfibio(Aquatico, Veiculo, Terrestre):
    def __init__(self, marca: str, modelo: str, num_rodas: int, tipo_embarcacao: str) -> None:

        Veiculo.__init__(self, marca, modelo)
        Terrestre.__init__(self, num_rodas)
        Aquatico.__init__(self, tipo_embarcacao)

    def exibir_informacoes(self):
        self.informacao()
        self.info_terrestre()
        self.info_aquatico()


carro1 = Amfibio("Chevrolet", "Corsa Classic", 4, "Veiculo Terrestre")

carro1.exibir_informacoes()
