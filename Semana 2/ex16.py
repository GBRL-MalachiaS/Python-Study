"""
16. Crie um programa com um menu usando `while` + `if/elif`.
"""

while True:
    print("========= Menu =========")
    print("1.Opcao um")
    print("2.Opcao dois")
    print("3.sair")
    menu = input("Digite uma opção: ")
    
    if menu == "1":
        print("Opção 1")
    elif menu == "2":
        print("Opção 2")
    elif menu == "3":
        print("sair")
        break
    else:
        print("Digite uma opção valida")