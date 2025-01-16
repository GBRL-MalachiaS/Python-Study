"""
10. **Exercício 10:** Crie uma classe chamada `FormaGeometrica` com um método `calcular_area()`, que exibe uma mensagem dizendo que a área será calculada. Depois, crie duas subclasses:
    - `Circulo`: Deve sobrescrever o método `calcular_area()` para calcular a área de um círculo (use π * raio²).
    - `Quadrado`: Deve sobrescrever o método `calcular_area()` para calcular a área de um quadrado (use lado²).
    - Crie objetos de ambas as classes e chame o método `calcular_area()`.

"""

# Classe base


class FormaGeometrica:
    def calcular_area(self) -> None:
        print("A área será calculada.")

# Subclasse Circulo


class Circulo(FormaGeometrica):
    def __init__(self, raio: float):
        self.raio = raio

    def calcular_area(self) -> float:
        return 3.14159 * (self.raio ** 2)

# Subclasse Quadrado


class Quadrado(FormaGeometrica):
    def __init__(self, lado: float):
        self.lado = lado

    def calcular_area(self) -> float:
        return self.lado ** 2

# Função polimórfica que calcula a área de qualquer forma geométrica


def imprimir_area(figura: FormaGeometrica):
    area = figura.calcular_area()
    print(f"A área da figura é: {area:.2f}")


# Criando objetos das subclasses
circulo = Circulo(5)  # Círculo com raio 5
quadrado = Quadrado(4)  # Quadrado com lado 4

# Chamando a função polimórfica
imprimir_area(circulo)   # Saída: A área da figura é: 78.54
imprimir_area(quadrado)  # Saída: A área da figura é: 16.00
