"""
#### Exercício 11: Decorador com `*args` e `**kwargs`

Crie um decorador chamado `verificar_parametros` que valide se todos os parâmetros passados para uma função são do tipo `int` ou `float`. 
Esse decorador deve funcionar para qualquer função, independentemente da quantidade de parâmetros.

```python
@verificar_parametros
def calcular_media(*numeros):
    return sum(numeros) / len(numeros)

print(calcular_media(10, 20, 30))        # Executa normalmente
print(calcular_media(10, "vinte", 30))   # "Erro: Todos os parâmetros devem ser números"

"""


def verificar_parametros(func):
    def parametros(*args, **kwargs):
        for n in args:
            if not isinstance(n, (int, float)):
                print(f"[Erro] - O valor '{n}' é do tipo {type(n).__name__}, "
                      "por favor insira apenas números inteiros ou ponto flutuante.")
                return None
        return func(*args, **kwargs)
    return parametros


@verificar_parametros
def calcular_media(*numeros):
    return sum(numeros) / len(numeros)


print(calcular_media(10, 20, 30))        # Executa normalmente
# "Erro: Todos os parâmetros devem ser números"
print(calcular_media(10, "vinte", 30))
print(calcular_media(10, "gabriel", 30))
