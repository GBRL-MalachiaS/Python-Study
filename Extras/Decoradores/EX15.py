"""
#### Exercício 15: Decorador de Retentativa

Crie um decorador `repetir_tentativas` que receba um número de tentativas como parâmetro.
Ele deve tentar executar a função várias vezes até que ela seja bem-sucedida, e, caso todas as tentativas falhem, exiba uma mensagem de erro.

```python
import random

@repetir_tentativas(3)
def funcao_aleatoria():
    if random.choice([True, False]):
        print("Sucesso!")
    else:
        raise ValueError("Falha aleatória.")

# Teste para verificar o comportamento de várias tentativas
funcao_aleatoria()
```

"""

import random
from functools import wraps


def repetir_tentativas(repeticoes):
    def tentativas(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for n in range(repeticoes):
                try:
                    # Executa e retorna em caso de sucesso
                    return func(*args, **kwargs)
                except ValueError as erro:
                    print(f"Tentativa {n + 1} falhou: {erro}")
            print("Falha geral: não foi possível realizar nenhuma execução com sucesso!")
        return wrapper
    return tentativas


@repetir_tentativas(3)
def funcao_aleatoria():
    if random.choice([True, False]):
        print("Sucesso!")
    else:
        raise ValueError("Falha aleatória.")


# Teste para verificar o comportamento de várias tentativas
funcao_aleatoria()
