"""

### Exercício 7: Decorador para Repetir Execução

Crie um decorador chamado `repetir` que receba um número como parâmetro e repita a execução de uma função esse número de vezes.

#### Exemplo:
```python
@repetir(3)
def diga_bom_dia():
    print("Bom dia!")

diga_bom_dia()
```

#### Saída esperada:
```
Bom dia!
Bom dia!
Bom dia!
```

"""
def repetir(n):
    def decorador(func):
        def repetindo(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return repetindo
    return decorador

@repetir(3)  # Agora o número de repetições é passado aqui
def diga_bom_dia():
    print("Bom dia!")

# Chamando a função decorada
diga_bom_dia()
