"""
14. Faça uma função que retorna o número de vogais em uma string.
"""

def total_vogais(texto):
    vogais = ["a","e","i","o","u"]
    contador = 0
    for letra in texto:
        if letra.lower() in vogais:
            contador += 1
    
    return contador


string = """
    um texto edigita para digitação para saber quantas vogais tem nesta budega
"""

print(total_vogais(string))