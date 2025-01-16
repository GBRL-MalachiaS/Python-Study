"""
### Exercício 1: Decorador de Logging

Crie um decorador chamado `log_execucao` que registre a data e hora de execução de uma função. Esse decorador deve exibir uma mensagem `"Executando função <nome_da_funcao> em <data_hora>"` antes de chamar a função.

#### Exemplo:
```python
@log_execucao
def saudacao(nome):
    print(f"Olá, {nome}!")

saudacao("Alice")
```

#### Saída esperada:
```
Executando função saudacao em YYYY-MM-DD HH:MM:SS
Olá, Alice!
```
"""
from datetime import datetime, date


def log_execucao(func):

    def interna(*args, **kwargs):
        data_hora = datetime.now()  # busca a data e hora atual
        # Faz a separação da data e hora e exibe uma das duas, conforme desejar.
        hora_atual = data_hora.strftime('%H:%M:%S')
        print(f'Executando função saudacao em {date.today()} - {hora_atual}')
        resultado = func(*args, **kwargs)
        print("depois")
        return resultado

    return interna


@log_execucao
def saudacao(nome):
    print(f'Olá, {nome}')


teste = saudacao("Gabriel")
