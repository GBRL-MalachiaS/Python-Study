"""
8. **Exercício 8:** Crie um programa que leia um arquivo texto (`texto.txt`) e exiba:
   - O número total de linhas no arquivo.
   - O número total de palavras no arquivo.
   - O número total de caracteres no arquivo.
   
"""


"""
Texto Utilizado no arquivo texto.txt:

. Texto Narrativo
A marca fundamental do texto narrativo é a existência de um enredo, no qual são desenvolvidas as ações das personagens, marcadas pelo tempo e pelo espaço.

Assim, a narração engloba o que chamamos de 5 elementos da narrativa:

Enredo: designa a história da narrativa. Dependendo de como a trama é contada, ele é classificado em dois tipos: enredo linear (sequência cronológica) e enredo não linear (não possui uma sequência cronológica).
Narrador: também chamado de foco narrativo, representa a "voz do texto", ou seja, determina quem está contando a história. Os tipos de narrador são: narrador observador (não faz parte da história, sendo somente um observador), narrador personagem (faz parte da história) e narrador onisciente (conhece todos os detalhes da narração).
Personagens: são aqueles que fazem parte da história e podem ser: personagens principais (protagonista e antagonista) ou personagens secundárias (adjuvante ou coadjuvante).
Tempo: marca o momento em que a trama está sendo desenvolvida. Ele é dividido em dois tipos: tempo cronológico e tempo psicológico.
Espaço: representa o local (ou locais) onde se desenvolve a história e que pode ser: físico, psicológico ou social.
Estrutura dos textos narrativos
Os textos narrativos possuem uma estrutura básica: apresentação, desenvolvimento, clímax e desfecho.

Apresentação: trata-se da introdução do texto, onde são apresentadas algumas de suas principais características como o tempo, o espaço e as personagem que fazem parte da trama.
Desenvolvimento: designa a maior parte do texto, onde são desenvolvidas as ações das personagens numa sequência de acontecimentos.
Clímax: representa a parte mais emocionante, surpreendente e tensa da narrativa.
Desfecho: é a parte final da trama, determinada pelo arremate de toda a história. Nela, é revelada o destino das personagens.
Alguns exemplos de textos narrativos
Conto
Fábula
Romance
Novela
Crônica
Exemplo de texto narrativo
Para entender melhor esse tipo de texto, segue abaixo um exemplo de uma fábula do escritor grego Esopo:

A Rã e o Boi

Uma rã estava no prado olhando um boi e sentiu tal inveja do tamanho dele que começou a inflar para ficar maior.

Então, outra rã chegou e perguntou se o boi era o maior dos dois.

A primeira respondeu que não – e se esforçou para inflar mais.

Depois, repetiu a pergunta:

– Quem é maior agora?

A outra rã respondeu:

– O boi.

A rã ficou furiosa e tentou ficar maior inflando mais e mais, até que arrebentou
"""
# Abrir o arquivo uma vez e fazer todas as operações necessárias
with open("texto.txt", "r", encoding="utf-8") as texto:
    conteudo = texto.read()  # Ler todo o conteúdo do arquivo

    # Contagem de linhas
    linhas = conteudo.splitlines()  # Divide o texto nas linhas
    print(f'Quantidade de Linhas: {len(linhas)}')

    # Contagem de palavras
    lista_palavras = conteudo.split()  # Divide o texto em palavras
    print(f"Quantidades de Palavras: {len(lista_palavras)}")

    # Contagem de caracteres (incluindo espaços e pontuações)
    # Conta todos os caracteres, incluindo espaços
    qtd_caracteres = len(conteudo)
    print(f"Quantidade de caracteres: {qtd_caracteres}")
