"""
**Exercício 8:** Crie um programa que peça ao usuário para digitar uma senha e permita que ele tenha até 3 tentativas para acertar a senha correta. 
Se ele errar nas 3 tentativas, exiba uma mensagem de acesso bloqueado.
"""
senha = "banana123"

for x in range(3, 0, -1):

    opcao_senha = input("Digite sua senha:")
    if opcao_senha == senha:
        print("Senha está certa!")
        break
    else:
        print(f"Você possui {x} tentativas")
