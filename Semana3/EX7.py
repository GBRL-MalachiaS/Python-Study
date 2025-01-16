"""
7. **Exercício 7:** Dado o dicionário `aluno = {'nome': 'João', 'idade': 20, 'nota': 8.5}`, faça o seguinte:
   - Adicione uma nova chave chamada `curso` com o valor `'Engenharia'`.
   - Atualize a idade do aluno para 21 anos.
   - Remova a chave `nota` do dicionário.
   - Exiba o dicionário final.
   
"""

aluno = {'nome': 'João', 'idade': 20, 'nota': 8.5}

# - Adicione uma nova chave chamada `curso` com o valor `'Engenharia'`.
aluno.update({"curso": 'Engenharia'})

# - Atualize a idade do aluno para 21 anos.
aluno.update({"idade": 21})
# - Remova a chave `nota` do dicionário.
aluno.pop('nota')

# - Exiba o dicionário final.
print(aluno)
