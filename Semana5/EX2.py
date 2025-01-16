"""
2. **Exercício 2:** Crie uma classe chamada `Retangulo` que tenha os atributos `largura` e `altura`. A classe deve ter dois métodos:
   - `calcular_area()` que retorna a área do retângulo (largura x altura).
   - `calcular_perimetro()` que retorna o perímetro do retângulo (2 * (largura + altura)).
   - Crie dois objetos da classe e exiba a área e o perímetro para ambos.

"""


class Retangulo:

    def __init__(self, largura: float, altura: float) -> None:
        self.largura = largura
        self.altura = altura

    def calcular_area(self) -> float:
        return self.largura * self.altura

    def calcular_perimetro(self) -> float:
        return (2*(self.largura + self.altura))


um = Retangulo(15.5, 21.2)
dois = Retangulo(2.5, 6.5)

print(um.calcular_area())
print(dois.calcular_area())
print(um.calcular_perimetro())
print(dois.calcular_perimetro())
