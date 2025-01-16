"""
#### Exercício 13: Usando `wraps` em Decoradores

Crie um decorador chamado `mensagem_decorador` que exibe uma mensagem antes e depois da execução da função decorada. 
Use `wraps` para manter as informações originais da função.

```python
from functools import wraps

@mensagem_decorador
def funcao_simples():
    Função exemplo para demonstrar wraps.
    print("Executando a função...")

print(funcao_simples.__name__)  # Deve exibir "funcao_simples"
print(funcao_simples.__doc__)   # Deve exibir "Função exemplo para demonstrar wraps."
```
"""
from functools import wraps


def mensagem_decorador(func):
    @wraps(func)
    def mensagem(*args,**kwargs):
        return func(*args,**kwargs)
    return mensagem

@mensagem_decorador
def funcao_simples():
    """Função exemplo para demonstrar wraps."""
    print("Executando a função...")

print(funcao_simples.__name__)  # Deve exibir "funcao_simples"
print(funcao_simples.__doc__)   # Deve exibir "Função exemplo para demonstrar wraps."
funcao_simples()