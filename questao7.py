
import json


# Carregar o arquivo JSON
with open("catalogo.json", "r", encoding="utf-8") as arquivo:
    catalogo = json.load(arquivo)

print("Catálogo carregado:", len(catalogo), "títulos.")


# Função para mostrar um título
def mostrar_titulo(titulo):
    if titulo["classificacao"] == 0:
        idade = "L"
    else:
        idade = str(titulo["classificacao"])

    print(
        f'{titulo["id"]:2} '
        f'{titulo["titulo"]:25} '
        f'{titulo["tipo"]:15} '
        f'{titulo["genero"]:15} '
        f'{titulo["ano"]:4} '
        f'{idade:3} '
        f'nota {titulo["nota"]:.1f}'
    )


# Opção 1 - Listar todos os títulos
def listar_tudo(catalogo):
    for titulo in catalogo:
        mostrar_titulo(titulo)


# Função para descobrir os gêneros existentes
def generos_existentes(catalogo):
    generos = []

    for titulo in catalogo:
        if titulo["genero"] not in generos:
            generos.append(titulo["genero"])

    return generos


# Opção 2 - Filtrar por gênero
def filtrar_por_genero(catalogo, genero):
    encontrou = False

    for titulo in catalogo:
        if titulo["genero"].lower() == genero.lower():
            mostrar_titulo(titulo)
            encontrou = True

    if encontrou == False:
        print("Nenhum título encontrado nesse gênero.")


# Opção 3 - Buscar título
def buscar_titulo(catalogo, texto):
    encontrou = False

    for titulo in catalogo:
        if texto.lower() in titulo["titulo"].lower():
            mostrar_titulo(titulo)
            encontrou = True

    if encontrou == False:
        print("Nenhum título encontrado.")


# Opção 4 - Títulos para determinada idade
def titulos_para_idade(catalogo, idade):
    encontrou = False

    for titulo in catalogo:
        if titulo["classificacao"] <= idade:
            mostrar_titulo(titulo)
            encontrou = True

    if encontrou == False:
        print("Nenhum título encontrado para essa idade.")


# Opção 5 - Mais bem avaliados
def mais_bem_avaliados(catalogo, quantidade):
    ordenados = sorted(
        catalogo,
        key=lambda titulo: titulo["nota"],
        reverse=True
    )

    for titulo in ordenados[:quantidade]:
        mostrar_titulo(titulo)


# Opção 6 - Estatísticas
def estatisticas(catalogo):
    filmes = 0
    series = 0
    soma_notas = 0

    for titulo in catalogo:
        if titulo["tipo"] == "Filme":
            filmes += 1

        elif titulo["tipo"] == "Série":
            series += 1

        soma_notas += titulo["nota"]

    if len(catalogo) > 0:
        media = soma_notas / len(catalogo)
    else:
        media = 0

    generos = generos_existentes(catalogo)

    print("Títulos:", len(catalogo))
    print("Filmes:", filmes)
    print("Séries:", series)
    print("Nota média:", round(media, 2))
    print("Gêneros:", ", ".join(generos))


# MENU PRINCIPAL
while True:
    print("\n===== CINEFLIX =====")
    print("1 - Listar tudo")
    print("2 - Filtrar por gênero")
    print("3 - Buscar título")
    print("4 - Títulos para a minha idade")
    print("5 - Mais bem avaliados")
    print("6 - Estatísticas")
    print("0 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        listar_tudo(catalogo)

    elif opcao == "2":
        generos = generos_existentes(catalogo)

        print("Gêneros:", ", ".join(generos))

        genero = input("Gênero: ")

        filtrar_por_genero(catalogo, genero)

    elif opcao == "3":
        texto = input("Parte do título: ")

        buscar_titulo(catalogo, texto)

    elif opcao == "4":
        try:
            idade = int(input("Sua idade: "))

            if idade < 0:
                print("A idade não pode ser negativa!")
            else:
                titulos_para_idade(catalogo, idade)

        except ValueError:
            print("Digite uma idade válida!")

    elif opcao == "5":
        texto = input("Quantos (Enter = 5)? ")

        if texto == "":
            quantidade = 5

        else:
            try:
                quantidade = int(texto)

                if quantidade <= 0:
                    print("Digite uma quantidade maior que zero!")
                    continue

            except ValueError:
                print("Digite um número inteiro válido!")
                continue

        mais_bem_avaliados(catalogo, quantidade)

    elif opcao == "6":
        estatisticas(catalogo)

    elif opcao == "0":
        print("Saindo da Cineflix...")
        break

    else:
        print("Opção inválida!")
