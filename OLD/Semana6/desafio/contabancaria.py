"""
6. **Desafio:** Crie um sistema de gerenciamento de contas bancárias com as seguintes classes:
   - `Conta`: com atributos `numero`, `titular`, e `saldo`. Deve ter métodos `depositar(valor)` e `sacar(valor)`.
   - `ContaCorrente`: herda de `Conta` e tem um atributo adicional `limite_credito`. Deve permitir saques que ultrapassem o saldo, mas respeitando o limite de crédito.
   - `ContaPoupanca`: herda de `Conta` e tem um atributo `taxa_juros`. Deve ter um método adicional `render_juros()`, que aumenta o saldo de acordo com a taxa de juros.
   
   Crie um menu interativo para:
   - Criar contas (corrente ou poupança).
   - Depositar em uma conta.
   - Sacar de uma conta.
   - Exibir saldo de uma conta.

"""
import os


def limpa_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


class Conta:
    def __init__(self, numero: int, titular: str, saldo: float) -> None:
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor: float):
        self.saldo = self.saldo + valor
        print(f'Saldo atualizado para R${self.saldo:0.2f}')

    def sacar(self, valor: float):
        self.saldo -= valor
        print(f'Saldo atualizado para R${self.saldo:0.2f}')


class ContaCorrente(Conta):
    def __init__(self, numero: int, titular: str, saldo: float, limite_credito: float) -> None:
        Conta.__init__(self, numero, titular, saldo)
        self.limite_credito = limite_credito

    def sacar(self, valor: float):
        limite_total = self.saldo + self.limite_credito

        if valor > limite_total:
            print(f' O valor de R${
                  valor:0.2f} supera seu limete total de R${limite_total:0.2f}, saque não realizado')

        elif valor <= self.saldo:
            self.saldo -= valor
            print(f'Saque realizado, valor em conta de {self.saldo}')
        elif valor > self.saldo:

            print('Você está utilizando do seu limete de credito')
            self.saldo -= valor
            self.limite_credito += self.saldo
            print(f'Saldo atual: R${
                  self.saldo:0.2f} - Limite de Crédito: R${self.limite_credito:0.2f}')


class ContaPoupanca(Conta):

    def __init__(self, numero: int, titular: str, saldo: float, taxa_juros: float) -> None:
        Conta.__init__(self, numero, titular, saldo)
        self.taxa_juros = taxa_juros

    def render_juros(self):

        taxa_juros = (self.taxa_juros / 100) + 1
        novo_saldo = self.saldo * taxa_juros
        self.saldo = novo_saldo
        print(f' A taxa de juros de {
              taxa_juros} foi aplicada, saldo atual de {self.saldo}')


conta_corrente = []
conta_popupanca = []


while True:

    print("======================================")
    print("1 - Criar Contas (Corrente ou Poupança)")
    print("2 - Depositar em uma conta. ")
    print("3 - Sacar de uma conta. ")
    print("4 - Exibir saldo de uma conta. ")
    print("5 - Sair")
    print("======================================")
    opcao = input("Digite uma opção: ")

    try:  # Corrige a excessão se o usuário digita algo diferente de um numero
        opcao = int(opcao)

        if opcao >= 6 or opcao <= 0:
            print(
                "Opção digitada não existe, por favor, escolha um numero do menu de 1 a 5")

            input("Precione qualquer tecla para continuar")
            limpa_tela()
            continue

        match opcao:
            case 1:  # Adicionar Livros - Status: Concluido
                ...

            case 2:  # Adiciona Leitores - Status: Concluido
                ...
            case 3:  # Emprestimo de Livros - Status: Concluida

                limpa_tela()
                limpa_tela()

            case 4:  # Devolução de Livros - Status: Concluido

                limpa_tela()
                limpa_tela()

            case 5:  # Exibe o status de todos os livros - Status: Concluido
                break
    except ValueError:
        print("Valor digitado para opção é invalido! Digite um numero entre 1 a 5")
