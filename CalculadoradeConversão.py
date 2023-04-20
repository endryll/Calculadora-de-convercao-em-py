unidades = ["bit", "byte", "kilobyte", "megabyte", "gigabyte", "terabyte", "petabyte"]
valor01 = 1024


def conversor(valor_inicial, unidade1, unidade2):
    if unidade1 not in unidades or unidade2 not in unidades:
        raise ValueError("Unidade inválida.")

    potencia1 = unidades.index(unidade1)
    potencia2 = unidades.index(unidade2)

    if potencia1 > potencia2:
        fator = valor01 ** (potencia1 - potencia2)
        valor_final = valor_inicial * fator
    else:
        fator = valor01 ** (potencia2 - potencia1)
        valor_final = valor_inicial / fator

    if unidade1 == "byte" and unidade2 == "bit":
        valor_final = valor_inicial * 8
    elif unidade1 == "bit" and unidade2 == "byte":
        valor_final = valor_inicial / 8

    return valor_final