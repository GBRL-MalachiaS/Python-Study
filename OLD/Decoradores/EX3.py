"""
### Exercício 3: Temporizador de Execução

Crie um decorador chamado `temporizador` que meça o tempo de execução de uma função e exiba o tempo total em segundos após a execução.

#### Exemplo:
```python
@temporizador
def espera():
    from time import sleep
    sleep(2)

espera()
```

#### Saída esperada:
```
Tempo de execução: 2.0 segundos
```
"""

import time


def temporizador(func):
    def interna(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fim = time.time()
        tempo_execucao = fim - inicio
        print(f"Tempo de execução: {tempo_execucao:.2f} segundos")
        return resultado

    return interna


@temporizador
def espera():
    time.sleep(2)
    print("Função concluída.")


espera()
