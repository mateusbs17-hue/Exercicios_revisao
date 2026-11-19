
from datetime import datetime


# Converte um texto em uma data
def converter_data(texto):
    return datetime.strptime(texto, "%d/%m/%Y").date()


# Calcula os dias de atraso
def dias_de_atraso(data_prevista, data_devolucao):
    dias = (data_devolucao - data_prevista).days

    if dias < 0:
        return 0
    else:
        return dias


# Calcula o valor da multa
def valor_multa(dias, por_dia=1.50, maximo=30.00):
    multa = dias * por_dia

    if multa > maximo:
        multa = maximo

    return multa


# Testes do módulo
if __name__ == "__main__":
    prevista = converter_data("05/11/2026")
    devolucao = converter_data("10/11/2026")

    dias = dias_de_atraso(prevista, devolucao)

    print("Dias de atraso:", dias)
    print("Valor da multa:", valor_multa(dias))
