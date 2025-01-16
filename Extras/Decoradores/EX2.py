"""
### Exercício 2: Decorador de Validação de Argumentos

Crie um decorador chamado `valida_positivo` que garanta que todos os argumentos passados para uma função sejam números positivos. Caso algum argumento não seja positivo, a função não deve ser executada e o decorador deve exibir uma mensagem de erro.

#### Exemplo:
```python
@valida_positivo
def soma(a, b):
    return a + b

print(soma(3, 5))  # 8
print(soma(3, -1))  # "Erro: Valores negativos não são permitidos!"
```

"""


def valida_positivo(func):
    def interna(*args, **kwargs):
        if valida_negativos(*args):
            print("Erro: Valores negativos não são permitidos!")
            return None  # para evitar execução quando houver número negativo
        else:
            return func(*args, **kwargs)  # chama a função original

    return interna


def valida_negativos(*args):
    # Verifica se algum argumento é negativo
    return any(x < 0 for x in args)


@valida_positivo
def soma(a, b):
    return a + b


# Testes
print(soma(3, 5))   # 8
print(soma(3, -1))  # "Erro: Valores negativos não são permitidos!"
