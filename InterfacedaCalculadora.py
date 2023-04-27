from CalculadoradeConversão import unidades,conversor

if __name__ == '__main__':
    valor_inicial = int(input("Insira o valor para ser convertido: "))
    unidade1 = input(f"Insira a unidade inicial {unidades}: ")
    while unidade1 not in unidades:
        unidade1 = input(f"Escolha a unidade para conversão {unidades}: ")
    unidade2 = input(f"Escolha a unidade para qual deseja converter {unidades}: ")
    while unidade2 not in unidades:
        unidade2 = input(f"Escolha a unidade para qual deseja converter {unidades}: ")

    valor_final = conversor(valor_inicial, unidade1, unidade2)
    print(f"{valor_inicial} {unidade1} = {valor_final} {unidade2}")