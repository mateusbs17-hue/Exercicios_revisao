
itens = []
peso_total = 0
limite = 15

print("===== MOCHILA DE CAMPING =====")

while True:
    nome = input("\nNome do item (ou FIM para encerrar): ")

    if nome.upper() == "FIM":
        break

    # Validar o peso
    while True:
        try:
            peso = float(input("Peso do item em kg: ").replace(",", "."))

            if peso <= 0:
                print("O peso precisa ser maior que zero!")
            else:
                break

        except ValueError:
            print("Digite um peso válido!")

    # Adicionar o item na lista
    itens.append([nome, peso])

    peso_total += peso

    print("Item adicionado!")

    # Verificar o limite da mochila
    if peso_total > limite:
        print("ATENÇÃO! A mochila ultrapassou 15 kg!")
        print("Excesso:", round(peso_total - limite, 2), "kg")


# Mostrar o resultado
print("\n===== RESULTADO DA MOCHILA =====")

if len(itens) == 0:
    print("A mochila está vazia.")

else:
    print("\nLista de itens:")

    for i in range(len(itens)):
        print(i + 1, "-", itens[i][0], "-", itens[i][1], "kg")

    quantidade = len(itens)
    media = peso_total / quantidade

    # Encontrar o item mais pesado
    mais_pesado = itens[0]

    for item in itens:
        if item[1] > mais_pesado[1]:
            mais_pesado = item

    print("\nQuantidade de itens:", quantidade)
    print("Peso total:", round(peso_total, 2), "kg")
    print("Peso médio:", round(media, 2), "kg")

    print("Item mais pesado:", mais_pesado[0])
    print("Peso do item mais pesado:", mais_pesado[1], "kg")

    # Verificar quanto cabe ou precisa retirar
    if peso_total > limite:
        retirar = peso_total - limite
        print("É necessário retirar", round(retirar, 2), "kg.")
    else:
        restante = limite - peso_total
        print("Ainda cabem", round(restante, 2), "kg na mochila.")
