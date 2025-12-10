"""
**Exercício 11:** Crie uma função chamada `calcula_media(notas)` que receba uma lista de notas (números) e retorne a média delas.

"""


def calcula_media(notas):
    qtd_notas = len(notas)
    soma_notas = sum(notas)
    media = soma_notas / qtd_notas
    return f'A média do aluno é: {media}'


provas = int(input("Digite quantas provas o aluno tem: "))
notas_aluno = []
for i in range(provas):
    x = float(input(f"Digite a nota[{i}]: "))
    notas_aluno.append(x)

print(calcula_media(notas_aluno))


# teste testado
