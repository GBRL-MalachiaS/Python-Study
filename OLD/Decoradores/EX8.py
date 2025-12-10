"""
### Exercício 8: Decorador para Conversão de Resultado

Crie um decorador chamado `converter_resultado` que converta o valor retornado por uma função para um tipo específico, 
como `str`, `int` ou `float`. O tipo de conversão deve ser especificado como parâmetro do decorador.

#### Exemplo:
```python
@converter_resultado(str)
def soma(a, b):
    return a + b

print(soma(10, 5))  # Retorna '15' como string
```

---
"""


def converter_resultado(tipo_conversao):
    def decorador(func):
        def conversor(*args, **kwargs):
            lista_numeros = list(args)
            conversao = [tipo_conversao(x) for x in lista_numeros]
            args = tuple(conversao)
            resultado = func(*args, **kwargs)
            return tipo_conversao(resultado)
        return conversor
    return decorador


@converter_resultado(str)
def soma(a, b):
    return a + b


print(soma(1, 5))  # Retorna '15' como string
