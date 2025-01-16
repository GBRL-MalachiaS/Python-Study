"""
### Exercício 9: Decorador de Verificação de Tipo de Argumento

Crie um decorador chamado `verificar_tipo` que receba o tipo esperado dos argumentos e verifique se todos os argumentos passados para uma função estão corretos.
Se algum argumento tiver um tipo incorreto, o decorador deve exibir uma mensagem de erro.

#### Exemplo:
```python
@verificar_tipo(int, int)
def soma(a, b):
    return a + b

print(soma(3, 5))  # Executa normalmente
print(soma(3, "5"))  # "Erro: Argumento com tipo incorreto"
```

"""


def verificar_tipo(tipo1, tipo2):
    def decorador(func):
        def tipo_dado(*args, **kwargs):
            numeros = list(args)
            if type(numeros[0]) == tipo1:
                if type(numeros[1]) == tipo2:
                    args = tuple(numeros)
                    return func(*args, **kwargs)
                else:
                    return f'Erro: O argumento {numeros[1]} é do tipo {type(numeros[1])}, por favor, digite um numero inteiro!'

            else:
                return f'Erro: O argumento {numeros[0]} é do tipo {type(numeros[0])}, por favor, digite um numero inteiro!'
        return tipo_dado
    return decorador


@verificar_tipo(int, int)
def soma(a, b):
    return a + b


print(soma(3, 5))  # Executa normalmente
print(soma(3, "5"))  # "Erro: Argumento com tipo incorreto"


def verificar_tipo2(*tipos_esperados):
    def decorador(func):
        def tipo_dado(*args, **kwargs):
            for i, (arg, tipo) in enumerate(zip(args, tipos_esperados)):
                if not isinstance(arg, tipo):
                    return f"Erro: O argumento {i+1} é do tipo {type(arg).__name__}, mas o tipo esperado é {tipo.__name__}."
            return func(*args, **kwargs)
        return tipo_dado
    return decorador


@verificar_tipo2(int, int)
def soma(a, b):
    return a + b


# Testes
print(soma(3, 5))   # Executa normalmente
print(soma(3, "5"))  # "Erro: Argumento com tipo incorreto"
