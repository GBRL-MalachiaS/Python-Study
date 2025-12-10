"""
**Desafio:** Crie um programa que simule uma agenda de contatos. Use um **dicionário**, onde as chaves são os nomes dos contatos e os valores são os números de telefone. 
O programa deve permitir ao usuário:
- Adicionar novos contatos.
- Exibir todos os contatos.
- Buscar o telefone de um contato específico.
- Alterar o telefone de um contato existente.
- Remover um contato da agenda.

"""
contatos = {
    "Contato1": 551199885533,
    "Contato2": 119955223388,
    "Contato3": 115587766882,
    "Contato4": 112255668844,
    "Contato5": 112236684544,
    "Contato6": 665588779988,
}

# - Adicionar novos contatos.

nome = input("Digite um nome contato para acrescentar na agenda: ")

if nome in contatos:
    print("Contato ja existe na agenda. Deseja altera contato? [S]/[N]")
    opcao = input("").upper()
    if opcao == "S":
        contatos[nome] = int(input("Digite um numero de telefone: "))
    elif opcao == "N":
        pass

else:
    telefone = int(input("Digite um telefone: "))
    contatos.update({nome: telefone})

# - Exibir todos os contatos.

for n in contatos:
    print(f'Nome: {n} - Telenfone: {contatos[n]}')

# -  Buscar o telefone de um contato específico.

nome = input("Digite um contato para buscar: ")

if nome in contatos:
    print(f'Contato: {nome} - Telefone: {telefone}')
else:
    print("Contatoa não existe!")


# - Alterar o telefone de um contato existente.

nome = input("Digite o nome de contato que deseja alterar: ")

if nome in contatos:
    telefone = int(input("Digite o nome telefone: "))
    contatos[nome] = telefone
    print(f'O contatato {nome} foi alterado o telefone para {telefone}')


# - Remover um contato da agenda.

remover_usuario = input("Digite o contato que quer remover: ")

if remover_usuario in contatos:
    contatos.pop(remover_usuario)
else:
    print("Usuário não existe")

for n in contatos:
    print(f'Nome: {n} - Telenfone: {contatos[n]}')
