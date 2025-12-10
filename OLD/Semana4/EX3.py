"""
3. **Exercício 3:** Crie um programa que leia uma frase do usuário e:
   - Conte quantas vogais (a, e, i, o, u) há na frase.
   - Substitua todas as ocorrências da letra "a" por "@".
"""
texto = input("Digite um texto: ").lower()
vogais = ["a", "e", "i", "o", "u"]
qtd_vogais = 0
texto_limpo = texto.replace(" ", "")

for n in texto_limpo:
    for i in vogais:
        if n == i:
            qtd_vogais += 1
novo_texto = texto_limpo.replace("a", "@")

print(f'Quantidade de vogais: {qtd_vogais}')
print(novo_texto)
