"""
3. **Exercício 3:** Crie uma classe chamada `ContaBancaria` com os seguintes atributos:
   - `titular`, `saldo`.
   - Métodos:
     - `depositar(valor)`: Adiciona o valor ao saldo.
     - `sacar(valor)`: Subtrai o valor do saldo, se houver saldo suficiente.
     - `exibir_saldo()`: Exibe o saldo atual.
   - Crie um objeto dessa classe e faça depósitos, saques e exiba o saldo em diferentes momentos.

"""


class ContaBancaria:
    def __init__(self, titular: str, saldo: float) -> None:
        self.titualar = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        return self.saldo

    def sacar(self, valor):
        self.saldo -= valor
        return self.saldo

    def exibir_saldo(self):
        return self.saldo


titular1 = ContaBancaria("Gabriel Malachias", 55)
titular2 = ContaBancaria("Luciana Goncalves", 89)

print(f"Deposito realizado no valor de: R${titular1.depositar(69)}")
print(f"Saque realizado no valor de: R${titular1.sacar(38)}")
print(f"Seu saldo é de: R${titular1.exibir_saldo()}")

print(f"Deposito realizado no valor de: R${titular2.depositar(69)}")
print(f"Saque realizado no valor de: R${titular2.sacar(38)}")
print(f"Seu saldo é de: R${titular2.exibir_saldo()}")
