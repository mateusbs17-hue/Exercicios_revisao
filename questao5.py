
def ler_texto(mensagem, vazio=False):
    while True:
        texto = input(mensagem).strip()

        if texto != "" or vazio:
            return texto
        else:
            print("Este campo não pode ficar vazio!")


def ler_inteiro(mensagem, minimo=None, maximo=None):
    while True:
        try:
            numero = int(input(mensagem))

            if minimo is not None and numero < minimo:
                print("O valor mínimo é", minimo)

            elif maximo is not None and numero > maximo:
                print("O máximo é", maximo)

            else:
                return numero

        except ValueError:
            print("Digite um número inteiro válido!")


def linha(caractere="-", tamanho=40):
    return caractere * tamanho


# Testes do módulo
if __name__ == "__main__":
    print("===== TESTANDO UTILIDADES =====")

    nome = ler_texto("Digite seu nome: ")
    print("Nome:", nome)

    idade = ler_inteiro("Digite sua idade: ", 1, 120)
    print("Idade:", idade)

    print(linha("=", 40))
