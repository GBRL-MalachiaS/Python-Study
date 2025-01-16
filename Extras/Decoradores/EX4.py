"""
### Exercício 4: Decorador de Contagem de Execuções

Crie um decorador chamado `contador_execucoes` que conte quantas vezes uma função foi executada e exiba essa contagem após cada execução.

#### Exemplo:
```python
@contador_execucoes
def dizer_ola():
    print("Olá!")

dizer_ola()
dizer_ola()
```

#### Saída esperada:
```
Olá!
Função foi executada 1 vez(es)
Olá!
Função foi executada 2 vez(es)
```
"""


def contador_execucoes(func):
    contador_execucoes.contador = 0

    def contador(*args, **kwargs):
        contador_execucoes.contador += 1
        resultado = func(*args, **kwargs)
        print(f'Função foi executada {contador_execucoes.contador}')
        return resultado

    return contador


@contador_execucoes
def diz_ola():
    print("Olá!")


diz_ola()
diz_ola()
diz_ola()
