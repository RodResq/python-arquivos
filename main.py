from contato import Contato
from arquivo_service import *

print("-" * 30)
print(("-" * 3) + " Agenda de contatos TW " + ("-" * 3))
print("-" * 30)

opcao_menu = 1
# lista_contatos = list()

while opcao_menu != 0:
    print("1. Listar contatos")
    print("2. Cadastrar contato")
    print("3. Remover contato")
    print("4. Buscar contato")
    print("0. Sair")
    opcao_menu = int(input("Digite a opção desejada: "))

    print(buscar_contato("pedro@email.com"))

    if opcao_menu == 1:
        contatos = listar_contatos()
        for contato in contatos:
            print(f"Nome: {contato.nome} / Email: {contato.email} / Telefone: {contato.telefone}")

    if opcao_menu == 2:
        nome_contato = input("Digite o nome do contato: ")
        email_contato = input("Digite o email do contato: ")
        telefone_contato = input("Digite o telefone do contato: ")
        contato_novo = Contato(nome_contato, email_contato, telefone_contato)
        cadastrar_contato(contato_novo)

    elif opcao_menu == 3:
        contato_remover = input("Digite o email do contato que deseja remover: ")
        contato_encontrado = False
        nova_lista_contato = list()
        with open("contatos.txt", "r") as contato:
            lista_contatos = contato.readlines()
            for i in lista_contatos:
                dados = i.split("-")
                if dados[1][1:-1] != contato_remover:
                    nova_lista_contato.append(f"{contato_novo.nome} - {contato_novo.email} - {contato_novo.telefone} \n")
                else:
                    contato_encontrado = True
            if not contato_encontrado:
                print("Contato não encontrado")
        with open("contatos.txt", "w") as arquivo:
            arquivo.writelines(nova_lista_contato)

    elif opcao_menu == 4:
        try:
            contato_buscar = input("Digite o email do contato que deseja buscar: ")
            contato_encontrado = False
            with open("contatos.txt", "r") as arquivo:
                lista_contatos = arquivo.readlines()
                for i in lista_contatos:
                    dados = i.split("-")
                    if dados[1][1:-1] == contato_buscar:
                        contato_novo = Contato(dados[1][:-1], dados[1][1:-1], dados[2][1:-1])
                        print(
                            f"Nome: {contato_novo.nome} / Email: {contato_novo.email} / Telefone: {contato_novo.telefone}")
                        contato_encontrado = True
                        break
                if not contato_encontrado:
                    print("Contato não encontrado")
        except FileNotFoundError:
            print("Arquivo Nao encontrado")

    else:
        print("opcao invalida")
else:
    print("Obrigado por usar a agenda de contatos TW")
