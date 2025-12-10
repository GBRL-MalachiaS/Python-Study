"""
### Exercício 12: Melhorando Feedback e Tratamento de Erros

Crie um decorador `verificar_tipo` que recebe uma tupla de tipos esperados e verifica se cada argumento corresponde ao tipo esperado. Se houver uma discrepância, ele deve exibir uma mensagem detalhada mencionando o argumento problemático.

```python
@verificar_tipo((int, int, str))
def funcao_exemplo(a, b, c):
    return f"{a} e {b} são números, e '{c}' é uma string."

print(funcao_exemplo(1, 2, "texto"))  # Executa normalmente
# "Erro: Argumento 2 é do tipo str, mas int era esperado."
print(funcao_exemplo(1, "dois", "texto"))

"""

def verificar_tipo(tipos_dados):
    def decorador(func):
        def dados(*args, **kwargs):
            for i, tipo_esperado in zip(args, tipos_dados):
                if not isinstance(i,tipo_esperado):
                    print(f'[ERROR]: Argumento {i} é o tipo {type(i).__name__}'
                          f'mas era esperado um valor {tipo_esperado.__name__}')
                    return None
            return func(*args, **kwargs)
        return dados
    return decorador


@ verificar_tipo((int, int, str))
def funcao_exemplo(a, b, c):
    return f"{a} e {b} são números, e '{c}' é uma string."


print(funcao_exemplo(1, 2, "texto"))  # Executa normalmente
# "Erro: Argumento 2 é do tipo str, mas int era esperado."
print(funcao_exemplo(1, "dois", "texto"))
