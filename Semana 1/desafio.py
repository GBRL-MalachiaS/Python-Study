"""
Mini Calculadora Inteligente com Relatório

Desenvolva um programa que:

1. Peça ao usuário:

   * Nome
   * Idade
   * Dois números
2. Realize automaticamente as operações:

   * Soma
   * Subtração
   * Multiplicação
   * Divisão
   * Resto
   * Expoente
3. Gere um **relatório final** bem formatado com todos os resultados.
4. Todos os textos do relatório devem usar **f-strings**.
5. Trate divisão por zero usando `try/except`.
6. Mostre ao final:

   * Tipo de cada dado recebido
   * Data e horário atual (sem módulos externos)

Esse desafio força a usar tudo da Semana 1.
"""

from datetime import datetime

nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
numero1 = input("Digite um numero: ")
numero2 = input("Digite um novo numero: ")

try:
   numero1 = int(numero1)
   numero2 = int(numero2)
   soma = numero1 + numero2
   subtracao = numero1 - numero2
   multiplicacao = numero1 * numero2
   divisao = numero1 / numero2
   resto = numero1 % numero2
   expoente = numero1**numero2
   print("\n")
   print(f"Soma: [{soma}]")
   print(f"Subtração: [{subtracao}]")
   print(f"Multiplicação: [{multiplicacao}]")
   print(f"Divisão: [{divisao:.2f}]")
   print(f"Resto: [{resto}]")
   print(f"Expoente: [{expoente}]")
   print("\n")
   print("Tipos de dados recebidos pelas variaveis")
   print(f"Nome: [{type(nome)}]")
   print(f"Idade: [{type(idade)}]")
   print(f"Numero1: [{type(numero1)}]")
   print(f"Numero2: [{type(numero2)}]")
   print(f"\n")
   data_atual  = datetime.now().strftime("%d/%m/%Y - %H:%M:%S")
   print(data_atual)

except ZeroDivisionError:
   print("ERRO: Não pode ser realizada a divisão por 0")

except ValueError:
   print("ERRO: por favor, preencher os numeros numeros e não com strings")
