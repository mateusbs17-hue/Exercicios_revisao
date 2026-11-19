
import json
import os
from datetime import datetime


ARQUIVO = "shows.json"


# Carregar os shows salvos
def carregar_shows():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    else:
        return []


# Salvar os shows no arquivo
def salvar_shows(shows):
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(shows, arquivo, ensure_ascii=False, indent=2)


# Organizar os shows por data
def ordenar_shows(shows):
    return sorted(
        shows,
        key=lambda show: datetime.strptime(show["data"], "%d/%m/%Y")
    )


# Mostrar um show
def mostrar_show(show, numero):
    if show["ingressos"] == 0:
        situacao = "ESGOTADO"
    else:
        situacao = str(show["ingressos"]) + " ingressos"

    print(
        str(numero) + ".",
        show["data"],
        show["artista"],
        show["cidade"],
        "R$ " + format(show["preco"], ".2f"),
        situacao
    )


# Listar todos os shows
def listar_shows(shows):
    ordenados = ordenar_shows(shows)

    if len(ordenados) == 0:
        print("Nenhum show cadastrado.")
    else:
        for i in range(len(ordenados)):
            mostrar_show(ordenados[i], i + 1)


# Cadastrar um show
def cadastrar_show(shows):
    artista = input("Artista/banda: ").strip()
    cidade = input("Cidade: ").strip()

    while True:
        texto_data = input("Data (dd/mm/aaaa): ")

        try:
            data = datetime.strptime(texto_data, "%d/%m/%Y")
            break
        except ValueError:
            print("Data inválida. Digite no formato dd/mm/aaaa.")

    while True:
        try:
            preco = float(
                input("Preço do ingresso: R$ ").replace(",", ".")
            )

            if preco <= 0:
                print("O preço precisa ser maior que zero!")
            else:
                break

        except ValueError:
            print("Digite um preço válido!")

    while True:
        try:
            ingressos = int(input("Ingressos disponíveis: "))

            if ingressos < 0:
                print("A quantidade não pode ser negativa!")
            else:
                break

        except ValueError:
            print("Digite um número inteiro válido!")

    novo_show = {
        "artista": artista,
        "cidade": cidade,
        "data": data.strftime("%d/%m/%Y"),
        "preco": preco,
        "ingressos": ingressos
    }

    shows.append(novo_show)

    salvar_shows(shows)

    print("Show cadastrado e agenda salva.")


# Buscar shows por cidade
def buscar_cidade(shows):
    cidade = input("Cidade: ").strip()

    encontrou = False
    ordenados = ordenar_shows(shows)

    for i in range(len(ordenados)):
        if ordenados[i]["cidade"].lower() == cidade.lower():
            mostrar_show(ordenados[i], i + 1)
            encontrou = True

    if encontrou == False:
        print("Nenhum show encontrado nessa cidade.")


# Vender ingressos
def vender_ingressos(shows):
    if len(shows) == 0:
        print("Não existem shows cadastrados.")
        return

    listar_shows(shows)

    ordenados = ordenar_shows(shows)

    while True:
        try:
            numero = int(input("Número do show: "))

            if numero < 1 or numero > len(ordenados):
                print("Número de show inválido!")
            else:
                break

        except ValueError:
            print("Digite um número inteiro válido!")

    show = ordenados[numero - 1]

    while True:
        try:
            quantidade = int(input("Quantos ingressos? "))

            if quantidade <= 0:
                print("Digite uma quantidade maior que zero!")
            else:
                break

        except ValueError:
            print("Digite um número inteiro válido!")

    if quantidade > show["ingressos"]:
        print("Só restam", show["ingressos"], "ingressos.")

    else:
        valor = quantidade * show["preco"]

        show["ingressos"] -= quantidade

        salvar_shows(shows)

        print(
            "Venda:",
            quantidade,
            "x R$",
            format(show["preco"], ".2f"),
            "=",
            "R$",
            format(valor, ".2f")
        )


# Remover um show
def remover_show(shows):
    if len(shows) == 0:
        print("Não existem shows cadastrados.")
        return

    listar_shows(shows)

    ordenados = ordenar_shows(shows)

    while True:
        try:
            numero = int(input("Número do show: "))

            if numero < 1 or numero > len(ordenados):
                print("Número de show inválido!")
            else:
                break

        except ValueError:
            print("Digite um número inteiro válido!")

    show = ordenados[numero - 1]

    shows.remove(show)

    salvar_shows(shows)

    print("Show de", show["artista"], "removido.")


# PROGRAMA PRINCIPAL

shows = carregar_shows()

print("Agenda carregada:", len(shows), "shows.")

while True:
    print("\n===== AGENDA DE SHOWS =====")
    print("1 - Listar shows")
    print("2 - Cadastrar show")
    print("3 - Shows em uma cidade")
    print("4 - Vender ingressos")
    print("5 - Remover show")
    print("0 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        listar_shows(shows)

    elif opcao == "2":
        cadastrar_show(shows)

    elif opcao == "3":
        buscar_cidade(shows)

    elif opcao == "4":
        vender_ingressos(shows)

    elif opcao == "5":
        remover_show(shows)

    elif opcao == "0":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida!")
