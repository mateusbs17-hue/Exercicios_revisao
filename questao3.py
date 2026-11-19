
# Função que calcula o subtotal de um item
def subtotal_item(preco, quantidade=1):
    return preco * quantidade


# Função que aplica o cupom de desconto
def aplicar_cupom(total, cupom):
    cupom = cupom.strip().upper()

    if cupom == "PROMO10":
        desconto = 0.10
    elif cupom == "VOLTAASAULAS":
        desconto = 0.15
    elif cupom == "BLACK25":
        desconto = 0.25
    else:
        desconto = 0

    return total * desconto


# Função que calcula o frete
def calcular_frete(total, gratis_acima=200.0, valor=25.0):
    if total >= gratis_acima:
        return 0
    else:
        return valor


# Função que calcula o valor de cada parcela
def valor_parcela(total, parcelas=1):
    if parcelas <= 6:
        return total / parcelas
    else:
        return total * (1 + 0.02 * parcelas) / parcelas


# PROGRAMA PRINCIPAL

carrinho = []
subtotal = 0

print("===== CARRINHO DA LOJA VIRTUAL =====")

while True:
    produto = input("\nNome do produto (Enter para finalizar): ")

    if produto == "":
        break

    # Validar preço
    while True:
        try:
            preco = float(input("Preço do produto: R$ ").replace(",", "."))

            if preco <= 0:
                print("O preço precisa ser maior que zero!")
            else:
                break

        except ValueError:
            print("Digite um preço válido!")

    # Validar quantidade
    while True:
        try:
            quantidade = int(input("Quantidade: "))

            if quantidade <= 0:
                print("A quantidade precisa ser maior que zero!")
            else:
                break

        except ValueError:
            print("Digite uma quantidade inteira válida!")

    # Calcular subtotal do item
    valor_item = subtotal_item(preco, quantidade)

    carrinho.append([produto, preco, quantidade, valor_item])

    subtotal += valor_item

    print("Item adicionado!")
    print("Valor atual do carrinho: R$", format(subtotal, ".2f"))


# Mostrar os produtos
print("\n===== SEU CARRINHO =====")

for item in carrinho:
    print(item[0], "-", item[2], "unidade(s) - R$", format(item[3], ".2f"))


# Aplicar cupom
cupom = input("\nDigite seu cupom (ou Enter para não usar): ")

desconto = aplicar_cupom(subtotal, cupom)

if cupom != "" and desconto == 0:
    print("Cupom inválido!")

# Calcular valor após desconto
total_com_desconto = subtotal - desconto

# Calcular frete sobre o valor com desconto
frete = calcular_frete(total_com_desconto)

# Calcular total final
total_final = total_com_desconto + frete

# Escolher quantidade de parcelas
while True:
    try:
        parcelas = int(input("\nEm quantas vezes deseja pagar? (1 a 12): "))

        if parcelas < 1 or parcelas > 12:
            print("Escolha entre 1 e 12 parcelas!")
        else:
            break

    except ValueError:
        print("Digite um número inteiro válido!")

# Calcular valor da parcela
valor = valor_parcela(total_final, parcelas)


# Nota final
print("\n===== NOTA DO PEDIDO =====")
print("Subtotal: R$", format(subtotal, ".2f"))
print("Desconto: R$", format(desconto, ".2f"))
print("Frete: R$", format(frete, ".2f"))
print("Total: R$", format(total_final, ".2f"))
print("Parcelas:", parcelas)
print("Valor de cada parcela: R$", format(valor, ".2f"))
