
nomes = []
inscritos = []

preco_onibus = 1800
lugares_onibus = 44

print("===== ORGANIZAÇÃO DA EXCURSÃO =====")

# Perguntar a quantidade de turmas
while True:
    try:
        quantidade_turmas = int(input("Quantas turmas participarão? "))

        if quantidade_turmas <= 0:
            print("Digite pelo menos uma turma!")
        else:
            break

    except ValueError:
        print("Digite um número inteiro válido!")


# Cadastrar as turmas e seus alunos
for i in range(quantidade_turmas):
    print("\nTurma", i + 1)

    nome = input("Nome da turma: ")

    while True:
        try:
            alunos = int(input("Quantidade de alunos inscritos: "))

            if alunos < 0:
                print("A quantidade não pode ser negativa!")
            else:
                break

        except ValueError:
            print("Digite um número inteiro válido!")

    nomes.append(nome)
    inscritos.append(alunos)


# Calcular o total de alunos
total_alunos = 0

for alunos in inscritos:
    total_alunos += alunos


# Calcular a quantidade de professores
professores = (total_alunos + 14) // 15


# Calcular o total de pessoas
total_pessoas = total_alunos + professores


# Calcular a quantidade de ônibus
onibus = (total_pessoas + lugares_onibus - 1) // lugares_onibus


# Calcular lugares sobrando
lugares_sobrando = (onibus * lugares_onibus) - total_pessoas


# Calcular custos
custo_total = onibus * preco_onibus

if total_alunos > 0:
    valor_por_aluno = custo_total / total_alunos
else:
    valor_por_aluno = 0


# Encontrar a turma com mais inscritos
maior_quantidade = inscritos[0]
turma_maior = nomes[0]

for i in range(len(inscritos)):
    if inscritos[i] > maior_quantidade:
        maior_quantidade = inscritos[i]
        turma_maior = nomes[i]


# Mostrar o resultado
print("\n===== RESULTADO DA EXCURSÃO =====")

print("Total de alunos:", total_alunos)
print("Quantidade de professores:", professores)
print("Total de pessoas:", total_pessoas)
print("Quantidade de ônibus:", onibus)
print("Lugares sobrando:", lugares_sobrando)

print("Custo total: R$", format(custo_total, ".2f"))
print("Valor por aluno: R$", format(valor_por_aluno, ".2f"))

print("Turma com mais inscritos:", turma_maior)
print("Quantidade de inscritos:", maior_quantidade)
