"""
#### Exercício 14: Decorador de Controle de Retorno

Crie um decorador `log_com_retorno` que recebe um nível de log como parâmetro
(`INFO`, `WARNING`, `ERROR`) e, dependendo do nível, exiba uma mensagem de log e retorne `None` se o nível for `"ERROR"`.

```python
@log_com_retorno("INFO")
def multiplicar(a, b):
    return a * b

@log_com_retorno("ERROR")
def dividir(a, b):
    return a / b

# Exibe "[INFO] Executando a função multiplicar" e retorna 15
print(multiplicar(3, 5))
# Exibe "[ERROR] A função dividir encontrou um problema." e retorna None
print(dividir(3, 5))
```
"""
from functools import wraps


def log_com_retorno(log):
    def decorador(func):
        @wraps(func)
        def nivel_log(*args, **kwargs):
            tipo_log = log.upper()
            match(tipo_log):
                case "INFO":
                    print(f'[INFO] Executando a função {func.__name__}')
                    return func(*args, **kwargs)
                case "WARNING":
                    print(f'[WARNING] A função {func.__name__}'
                          f' entrá em execução')
                    return func(*args, **kwargs)
                case "ERROR":
                    print(f'[ERROR] A função {func.__name__}, '
                          f'encontrou um problema')
                    return None
                case _:
                    print(f'[LOG] Nível de log desconhecido: {tipo_log}')
                    return func(*args, **kwargs)
        return nivel_log
    return decorador


@ log_com_retorno("INFO")
def multiplicar(a, b):
    return a * b


@ log_com_retorno("ERROR")
def dividir(a, b):
    return a / b


# Exibe "[INFO] Executando a função multiplicar" e retorna 15
print(multiplicar(3, 5))
# Exibe "[ERROR] A função dividir encontrou um problema." e retorna None
print(dividir(3, 5))
