# Número de convidados
num_convidados = int(input())
convidados = []

for i in range(num_convidados):
    nome_convidado = input()
    comida_convidado = input()
    valor_comida = int(input())
    convidados.append([nome_convidado, comida_convidado, valor_comida])

# Convidado Maicon Kuster
convidados_temp = []
for convidado in convidados:
    if convidado[0] == "Maicon Kuster":
        print("você é convidado DE GUÊÊ???, sai da minha festa seu FOFOQUEIRO!!")
    else:
        convidados_temp.append(convidado)
convidados = convidados_temp

# Convidado com prato repetido
pratos_vistos = {}
convidados_temp = []
for convidado in convidados:
    if convidado[1] not in pratos_vistos:
        pratos_vistos[convidado[1]] = True
        convidados_temp.append(convidado)
    else:
        print(f"Na Festa do Calabreso não pode comida Repetida SAI FORA {convidado[0]}")
convidados = convidados_temp

# Se nenhum dos convidados passar nos requisitos do Davi ou o número de convidados for 0:
if len(convidados) == 0:
    print("Nenhum convidado marcou presença na festa do calabreso!")

else:
    # Agradecimento comida mais cara
    maior_valor = -1
    for convidado in convidados:
        if convidado[2] > maior_valor:
            maior_valor = convidado[2]
            nome_maior_convidado = convidado[0]
            comida_maior_convidado = convidado[1]
        elif convidado[2] == maior_valor and convidado[0] < nome_maior_convidado:
            nome_maior_convidado = convidado[0]
            comida_maior_convidado = convidado[1]
    print(
        f"Obrigado para o(a) {nome_maior_convidado} pelo(a) excelente {comida_maior_convidado}"
    )

    if len(convidados) >= 2:
        # Comida mais barata
        menor_valor = 10000000000
        for convidado in convidados:
            if convidado[2] < menor_valor:
                menor_valor = convidado[2]
                nome_menor_convidado = convidado[0]
                comida_menor_convidado = convidado[1]
            elif convidado[2] == menor_valor and convidado[0] < nome_menor_convidado:
                nome_menor_convidado = convidado[0]
                comida_menor_convidado = convidado[1]
        print(
            f"Rapaz, {nome_menor_convidado} trouxe o(a) {comida_menor_convidado} que estava altamente mais ou menos!!!"
        )

    # Ordem alfabética em caso de empate
    for i in range(len(convidados)):
        for j in range(len(convidados) - 1 - i):
            if convidados[j][2] > convidados[j + 1][2] or (
                convidados[j][2] == convidados[j + 1][2]
                and convidados[j][0] > convidados[j + 1][0]
            ):
                convidados[j], convidados[j + 1] = convidados[j + 1], convidados[j]

    print("Lista de convidados do Calabreso")
    for i in range(1, len(convidados) + 1):
        print(f"{i}- {convidados[i-1][0]}")
