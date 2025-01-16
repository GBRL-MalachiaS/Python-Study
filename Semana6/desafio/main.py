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
        print(f'Saldo anterior: R${self.saldo}')
        self.saldo += valor
        print(f'Saldo atualizado para R${self.saldo:0.2f}')

    def sacar(self, valor: float):
        if valor > self.saldo:
            print(f'Saldo insuficiente para sacar R${valor:.2f}')
        else:
            self.saldo -= valor
            print(f'Saldo atualizado para R${self.saldo:0.2f}')

    def exibir_saldo(self):
        print(f'Conta: {self.numero}')
        print(f'Saldo: R${self.saldo:0.2f}')


class ContaCorrente(Conta):
    def __init__(self, numero: int, titular: str, saldo: float, limite_credito: float) -> None:
        super().__init__(numero, titular, saldo)
        self.limite_credito = limite_credito

    def sacar(self, valor: float):
        limite_total = self.saldo + self.limite_credito

        if valor > limite_total:
            print(f'O valor de R${valor:.2f} supera seu limite total de R${
                  limite_total:.2f}, saque não realizado.')
        elif valor <= self.saldo:
            self.saldo -= valor
            print(f'Saque realizado. Saldo atual: R${self.saldo:.2f}')
        else:
            valor_excedente = valor - self.saldo
            self.saldo = 0
            self.limite_credito -= valor_excedente
            print(f'Saque realizado utilizando limite de crédito.')
            print(f'Saldo atual: R${
                  self.saldo:.2f} - Limite de Crédito: R${self.limite_credito:.2f}')


class ContaPoupanca(Conta):
    def __init__(self, numero: int, titular: str, saldo: float, taxa_juros: float) -> None:
        super().__init__(numero, titular, saldo)
        self.taxa_juros = taxa_juros

    def render_juros(self):
        self.saldo += self.saldo * (self.taxa_juros / 100)
        print(f'A taxa de juros de {
              self.taxa_juros}% foi aplicada. Saldo atual: R${self.saldo:.2f}')


conta_corrente = {}
conta_poupanca = {}

while True:
    print("======================================")
    print("1 - Criar Contas (Corrente ou Poupança)")
    print("2 - Depositar em uma conta. ")
    print("3 - Sacar de uma conta. ")
    print("4 - Exibir saldo de uma conta. ")
    print("5 - Sair")
    print("======================================")
    opcao = input("Digite uma opção: ")

    try:
        opcao = int(opcao)

        if opcao >= 6 or opcao <= 0:
            print(
                "Opção digitada não existe, por favor, escolha um número do menu de 1 a 5")
            input("Pressione qualquer tecla para continuar")
            limpa_tela()
            continue

        match opcao:
            case 1:  # Criar Contas (Corrente ou Poupança)
                limpa_tela()
                while True:
                    print("Escolha abaixo o tipo de conta que deseja criar")
                    print("1 - Conta Corrente")
                    print("2 - Conta Poupança")
                    tipo_conta = input("Digite o tipo de conta: ")

                    try:
                        tipo_conta = int(tipo_conta)
                        if tipo_conta >= 3 or tipo_conta <= 0:
                            print("Valor digitado para a conta está incorreto.")
                        else:
                            numero_conta = input("Número da conta: ")
                            titular = input("Nome do titular: ")
                            saldo = input("Saldo inicial: ")

                        try:
                            numero_conta = int(numero_conta)
                            saldo = float(saldo)
                        except ValueError:
                            print("Valores inválidos para número da conta ou saldo.")

                        match tipo_conta:
                            case 1:  # Conta Corrente
                                limite_credito = input("Limite de crédito: ")
                                try:
                                    limite_credito = float(limite_credito)
                                    conta_corrente[numero_conta] = ContaCorrente(
                                        numero_conta, titular, saldo, limite_credito)  # noqa
                                    limpa_tela()
                                    print(f"Conta corrente {numero_conta} criada com sucesso!")  # noqa
                                    input(
                                        "Pressione qualquer tecla para continuar")
                                    limpa_tela()
                                    break
                                except ValueError:
                                    print(
                                        "Valor inválido para limite de crédito.")
                            case 2:  # Conta Poupança
                                taxa = input("Digite a taxa de juros (%): ")
                                try:
                                    taxa = float(taxa)
                                    conta_poupanca[numero_conta] = ContaPoupanca(
                                        numero_conta, titular, saldo, taxa)
                                    print(f"Conta poupança {
                                          numero_conta} criada com sucesso!")
                                    input(
                                        "Pressione qualquer tecla para continuar")
                                    limpa_tela()
                                    break
                                except ValueError:
                                    print("Valor inválido para a taxa de juros.")
                    except ValueError:
                        print("Opção inválida para tipo de conta.")
            case 2:  # Depositar em uma conta
                numero_conta = input("Número da conta: ")
                valor = input("Valor para depósito: ")

                try:
                    numero_conta = int(numero_conta)
                    valor = float(valor)

                    if numero_conta in conta_corrente:
                        conta = conta_corrente[numero_conta]
                        conta.depositar(valor)
                    elif numero_conta in conta_poupanca:
                        conta = conta_poupanca[numero_conta]
                        conta.depositar(valor)
                    else:
                        print("Conta não encontrada.")

                    input("Pressione qualquer tecla para continuar")
                    limpa_tela()

                except ValueError:
                    print("Valor inválido para número da conta ou depósito.")
            case 3:  # Sacar de uma conta
                numero_conta = input("Número da conta: ")
                valor = input("Valor para saque: ")

                try:
                    numero_conta = int(numero_conta)
                    valor = float(valor)

                    if numero_conta in conta_corrente:
                        conta = conta_corrente[numero_conta]
                        conta.sacar(valor)
                    elif numero_conta in conta_poupanca:
                        conta = conta_poupanca[numero_conta]
                        conta.sacar(valor)
                    else:
                        print("Conta não encontrada.")

                    input("Pressione qualquer tecla para continuar")
                    limpa_tela()

                except ValueError:
                    print("Valor inválido para número da conta ou saque.")
            case 4:  # Exibir saldo de uma conta
                numero_conta = input("Número da conta: ")

                try:
                    numero_conta = int(numero_conta)

                    if numero_conta in conta_corrente:
                        conta = conta_corrente[numero_conta]
                        conta.exibir_saldo()
                    elif numero_conta in conta_poupanca:
                        conta = conta_poupanca[numero_conta]
                        conta.exibir_saldo()
                    else:
                        print("Conta não encontrada.")

                    input("Pressione qualquer tecla para continuar")
                    limpa_tela()

                except ValueError:
                    print("Valor inválido.")
            case 5:  # Sair
                break

    except ValueError:
        print("Opção inválida! Digite um número entre 1 a 5.")
