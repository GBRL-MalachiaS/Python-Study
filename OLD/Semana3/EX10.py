"""
10. **Exercício 10:** Crie um conjunto com os nomes de 5 frutas. Em seguida:
   - Verifique se a fruta 'maçã' está presente no conjunto.
   - Adicione a fruta 'melancia' ao conjunto.
   - Remova a fruta 'uva' do conjunto (se existir).
   - Exiba o conjunto resultante.

"""

frutas = ['maçã', 'banana', 'uva', 'abacaxi', 'laranja']

if 'maçã' in frutas:
    print("A Fruta Maçã existe no grupo")

frutas.append('Melancia')

frutas.remove('uva')

print(frutas)