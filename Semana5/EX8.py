"""
8. **Exercício 8:** Crie uma classe chamada `ContaCorrente` com os atributos `titular` e `saldo` (saldo deve ser privado). Crie os métodos:
   - `depositar(valor)`: Adiciona o valor ao saldo.
   - `sacar(valor)`: Subtrai o valor do saldo, se houver saldo suficiente.
   - `get_saldo()`: Retorna o saldo.
   - **Dica:** Use `self.__saldo` para criar um atributo privado.
   - Crie um objeto dessa classe, faça depósitos, saques e use `get_saldo()` para exibir o saldo.
"""


class ContaCorrente():
    def __init__(self, titular: str, saldo: float) -> None:
        self.titular = titular
        self.__saldo = saldo

    def depositar(self, valor: float) -> None:
        if valor > 0:
            self.__saldo += valor
        else:
            print(f'O valor R${valor}digitado é invalido')

    def sacar(self, valor: float) -> None:
        if self.__saldo < valor:
            print(f"Saldo insulficiente ! Você possui somente {self.__saldo}")
        else:
            self.__saldo -= valor

    def get_saldo(self):
        print(f'Saldo atual de R${self.__saldo}')


cliente = ContaCorrente("Gabriel", 32500.80)

cliente.depositar(95)
cliente.get_saldo()
cliente.sacar(35)
cliente.get_saldo()
