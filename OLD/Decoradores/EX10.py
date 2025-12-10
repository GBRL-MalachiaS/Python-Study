"""
### Exercício 10: Decorador para Logging com Níveis

Crie um decorador chamado `log_nivel` que receba um nível de log (`INFO`, `WARNING`, `ERROR`) e exiba uma mensagem de log antes de chamar a função.
O nível deve ser especificado como parâmetro do decorador.

#### Exemplo:
```python
@log_nivel("INFO")
def soma(a, b):
    return a + b

soma(3, 5)
```

#### Saída esperada:
```
[INFO] Executando a função soma
8
```
"""


def log_nivel(log):
    def decorador(func):
        def nivel_log(*args, **kwargs):
            tipo_log = log.upper()
            match(tipo_log):
                case "INFO":
                    print(f'[INFO] Executando a função {func.__name__}')
                    return func(*args, **kwargs)
                case "WARNING":
                    print(f'[WARNING] A função {
                          func.__name__} entrá em execução')
                    return func(*args, **kwargs)
                case "ERROR":
                    print(f'[ERROR] A função {
                          func.__name__} não será executada por favor, verifique o erro!')
                    return None
                case _:
                    print(f'[LOG] Nível de log desconhecido: {tipo_log}')
                    return func(*args, **kwargs)
        return nivel_log
    return decorador


@log_nivel("warning")
def soma(a, b):
    return a + b


print(soma(1, 5))
