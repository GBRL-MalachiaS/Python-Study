"""
4. **Exercício 4:** Crie uma classe `Calculadora` com dois métodos:
   - Um método **estático** chamado `somar()` que recebe dois números e retorna a soma.
   - Um método **de classe** chamado `criar_calculadora()`, que retorna uma instância da classe.
   
   Teste o método estático sem criar uma instância da classe e, em seguida, teste o método de classe para criar uma instância

"""


class Calculadora():
    def __init__(self, numero1, numero2) -> None:
        self.numero1 = numero1
        self.numero2 = numero2

    @staticmethod
    def somar(a, b):
        return a+b

    @classmethod
    def criar_calculadora(cls, numero1, numero2):

        return cls(numero1, numero2)


soma = Calculadora.somar(2, 3)
print(soma)

nova_calc = Calculadora.criar_calculadora(1, 2)

print(f'{nova_calc.numero1} e {nova_calc.numero2}')


match nova_calc:
    case 2:
        ...
