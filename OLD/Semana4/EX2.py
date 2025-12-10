"""
2. **Exercício 2:** Escreva um programa que verifique se uma string inserida pelo usuário é um palíndromo (uma palavra que é lida da mesma forma de trás para frente).
   - Exemplo de palíndromo: "arara", "radar", "reviver".
"""
texto = input("Digite um possivel palintromo: ")
texto_limpo = texto.replace(" ", "").lower()

if texto_limpo == texto_limpo[::-1]:
    print(f"A palavra {texto} é um palindromo")
else:
    print(f'A palavra {texto}, não é um palindromo')
