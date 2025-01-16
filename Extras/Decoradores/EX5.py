"""
### Exercício 5: Decorador de Cache de Resultados

Crie um decorador chamado `cache_resultados` que armazene os resultados das chamadas de uma função com 
base nos argumentos recebidos. Se a função for chamada novamente com os mesmos argumentos, o decorador 
deve retornar o resultado armazenado, evitando a execução repetida.

#### Exemplo:
```python
@cache_resultados
def calcula_soma(a, b):
    print("Calculando...")
    return a + b

print(calcula_soma(3, 5))  # Calculando...
print(calcula_soma(3, 5))  # Retorna o resultado armazenado sem calcular novamente

Minha resposta:
```


def cache_resultados(func):
    cache_resultados.resultado = 0

    def cache(*args, **kwargs):
        if cache_resultados.resultado == 0:
            funcao = func(*args, **kwargs)
            cache_resultados.resultado = funcao
        else:
            print(f'Resultado da conta: {cache_resultados.resultado}')
        return None
    return cache


@cache_resultados
def calcula_soma(a, b):
    print("Calculando...")
    return a + b


print(calcula_soma(2, 3))
print(calcula_soma(2, 3))


"""

# Correção


def cache_resultados(func):
    # Inicializa o cache como um dicionário
    cache = {}

    def cache_func(*args, **kwargs):
        # Cria uma chave única com args e kwargs
        chave = (args, frozenset(kwargs.items()))

        # Se o resultado já está no cache, retorna-o diretamente sem recalcular
        if chave in cache:
            return cache[chave]

        # Caso contrário, executa o cálculo e armazena o resultado no cache
        print("Calculando...")
        resultado = func(*args, **kwargs)
        cache[chave] = resultado
        return resultado

    return cache_func


@cache_resultados
def calcula_soma(a, b):
    return a + b


# Testando a função
print(calcula_soma(2, 3))  # Executa o cálculo e armazena no cache
print(calcula_soma(2, 3))  # Retorna o valor do cache sem "Calculando..."
print(calcula_soma(3, 5))  # Executa o cálculo para novos argumentos
print(calcula_soma(3, 5))  # Retorna o valor do cache sem "Calculando..."
