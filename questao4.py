
# Função para formatar o tempo em horas e minutos
def formatar_duracao(minutos):
    horas = minutos // 60
    resto = minutos % 60

    if horas > 0:
        return f"{horas}h{resto:02d}min"
    else:
        return f"{minutos}min"


# Função para somar as durações
def tempo_total(duracoes):
    total = 0

    for duracao in duracoes:
        total += duracao

    return total


# Função para calcular os dias necessários
def dias_para_terminar(total_minutos, minutos_por_dia=120):
    dias = (total_minutos + minutos_por_dia - 1) // minutos_por_dia

    return dias


# Função para classificar a maratona
def classificar_maratona(total_minutos):
    if total_minutos < 300:
        return "Leve"
    elif total_minutos <= 900:
        return "Média"
    else:
        return "Intensa"


# PROGRAMA PRINCIPAL

print("=== MARATONA DE SÉRIE ===")

nome_serie = input("Nome da série: ")

while True:
    try:
        temporadas = int(input("Quantas temporadas? "))

        if temporadas <= 0:
            print("Digite pelo menos uma temporada!")
        else:
            break

    except ValueError:
        print("Digite um número inteiro válido!")


duracoes_temporadas = []

# Cadastro das temporadas
for i in range(temporadas):
    print("\nTemporada", i + 1)

    while True:
        try:
            episodios = int(input("Número de episódios: "))

            if episodios <= 0:
                print("Digite pelo menos um episódio!")
            else:
                break

        except ValueError:
            print("Digite um número inteiro válido!")

    while True:
        try:
            duracao = int(input("Duração média do episódio (min): "))

            if duracao <= 0:
                print("A duração precisa ser maior que zero!")
            else:
                break

        except ValueError:
            print("Digite um número inteiro válido!")

    # Calcula o tempo total da temporada
    total_temporada = episodios * duracao

    duracoes_temporadas.append(total_temporada)


# Calcula o tempo total da série
total_serie = tempo_total(duracoes_temporadas)

# Mostra os resultados
print("\n=== " + nome_serie.upper() + " ===")

for i in range(len(duracoes_temporadas)):
    print(
        "Temporada", i + 1, ":",
        formatar_duracao(duracoes_temporadas[i])
    )

print(
    "Total:",
    formatar_duracao(total_serie),
    "(" + classificar_maratona(total_serie) + ")"
)


# Calcula os dias para terminar
while True:
    try:
        minutos_dia = int(
            input("\nQuantos minutos por dia você pode assistir? ")
        )

        if minutos_dia <= 0:
            print("Digite um valor maior que zero!")
        else:
            break

    except ValueError:
        print("Digite um número inteiro válido!")


dias = dias_para_terminar(total_serie, minutos_dia)

dias_padrao = dias_para_terminar(total_serie)

print(
    "Você termina", nome_serie,
    "em", dias, "dias."
)

print(
    "Com 2 horas por dia (padrão), seriam",
    dias_padrao, "dias."
)
