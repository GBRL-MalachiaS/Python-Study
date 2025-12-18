"""
15. Crie uma função recursiva que calcula o fatorial.

"""


def fatorial_recursivo(n: int) -> int:
    if n < 0:
        raise ValueError("O fatorial não é definido para números negativos.")
    if n in (0, 1):
        return 1
    return n * fatorial_recursivo(n - 1)

# Uso:
n = int(input("Digite um número inteiro não negativo: "))
print(f"{fatorial_recursivo(n)}")
