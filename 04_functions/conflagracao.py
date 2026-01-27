# Função para calcular a distância de Chebyshev:
def distancia_chebyshev(linha_sam, coluna_sam, linha_neil, coluna_neil):
    diff_inha = abs(linha_sam - linha_neil)  # Distância entre as linhas de Sam e Neil
    diff_coluna = abs(
        coluna_sam - coluna_neil
    )  # Distância entre as colunas de Sam e Neil
    return max(diff_inha, diff_coluna)  # Retorna a maior das duas distâncias


# Função para a ação de atirar de Sam:
def atirar_Sam(arma_atual, distancia, hp_neil):
    # Se a arma for a Espingarda e a distância for menor ou igual a 2, o dano será 25
    if arma_atual == "Espingarda":
        if distancia <= 2:
            dano = 25
        else:
            dano = 0
    # Se a arma for o Rifle e a distância for 3, o dano será 15, caso contrário, será 5
    elif arma_atual == "Rifle":
        if distancia == 3:
            dano = 15
        else:
            dano = 5
    # Se a arma for a Metralhadora e a distância for maior ou igual a 4, o dano será 15, caso contrário, será 0
    elif arma_atual == "Metralhadora":
        if distancia >= 4:
            dano = 15
        else:
            dano = 0
    else:
        dano = 0
    hp_neil -= dano
    return dano, hp_neil  # Retorna o dano e a vida de Neil


# Função para a mecânica de teletransporte de Neil:
def teletransporte_neil(
    matriz_combate_6x6,
    linha_sam,
    coluna_sam,
    linha_neil_atual,
    coluna_neil_atual,
    piso_anterior_neil,
):
    distancia_maxima = -1
    nova_linha = -1
    nova_coluna = -1
    # Percorre a matriz 6x6 para encontrar a posição mais distante de Sam
    for i in range(6):
        for j in range(6):
            # Se a posição não for um obstáculo...
            if matriz_combate_6x6[i][j] != "I":
                # Calcula a distância de Chebyshev entre a posição atual de Sam e a posição atual de Neil
                distancia = distancia_chebyshev(linha_sam, coluna_sam, i, j)
                # Se a distância for maior que a distância máxima..
                if distancia >= distancia_maxima:
                    # Atualiza a distância máxima e a nova posição de Neil
                    distancia_maxima = distancia
                    nova_linha = i
                    nova_coluna = j

    matriz_combate_6x6[linha_neil_atual][
        coluna_neil_atual
    ] = piso_anterior_neil  # Atualiza a posição anterior de Neil na matriz
    novo_piso_neil = matriz_combate_6x6[nova_linha][
        nova_coluna
    ]  # Atualiza o novo piso de Neil
    matriz_combate_6x6[nova_linha][
        nova_coluna
    ] = "N"  # Atualiza a nova posição de Neil na matriz
    # Para cada linha e coluna da matriz 6x6...
    for i in range(6):
        for j in range(6):
            # Se a coluna for a última, imprime o elemento sem espaço
            if j == 5:
                print(matriz_combate_6x6[i][j], end="")
            # Caso contrário, imprime o elemento com espaço
            else:
                print(matriz_combate_6x6[i][j], end=" ")
        print()
    return (
        nova_linha,
        nova_coluna,
        novo_piso_neil,
    )  # Retorna a nova linha, coluna e piso de Neil


print("Sam: Mas que lugar é esse aqui?")
print("Dollman: WASD... Num exclusivo de PS5? Ah, fala sério!")
print()
# Variáveis iniciais:
hp_sam = 100
hp_neil = 100
arma_atual = "Rifle"
acoes_sam = 0
hits_neil = 0
dano_neil_total = 0
hits_fogo_total = 0
aviso_40hp_dado = False
coluna_sam = 0
linha_sam = 0
coluna_neil = 0
linha_neil = 0
matriz_combate_6x6 = []
for i in range(6):
    linha = input().split()
    matriz_combate_6x6.append(linha)

# Para cada linha e coluna da matriz 6x6...
for i in range(6):
    for j in range(6):
        # Se o elemento for "S", atualiza a linha e coluna de Sam
        if matriz_combate_6x6[i][j] == "S":
            linha_sam = i
            coluna_sam = j
        # Se o elemento for "N", atualiza a linha e coluna de Neil
        if matriz_combate_6x6[i][j] == "N":
            linha_neil = i
            coluna_neil = j
piso_sam = "P"
piso_neil = "P"

# Enquanto a vida de Sam e Neil for maior que 0...
while hp_sam > 0 and hp_neil > 0:
    entrada = input()
    # Se a entrada for "W", "A", "S" ou "D"...
    if entrada in ["W", "A", "S", "D"]:
        # Atualiza a quantidade de ações de Sam e a nova linha e coluna de Sam
        acoes_sam += 1
        nova_linha = linha_sam
        nova_coluna = coluna_sam

        if entrada == "W":
            nova_linha = linha_sam - 1
        elif entrada == "A":
            nova_coluna = coluna_sam - 1
        elif entrada == "S":
            nova_linha = linha_sam + 1
        elif entrada == "D":
            nova_coluna = coluna_sam + 1
        # Se a nova linha e coluna estiverem dentro da matriz e não for um obstáculo...
        if (
            0 <= nova_linha < 6
            and 0 <= nova_coluna < 6
            and matriz_combate_6x6[nova_linha][nova_coluna] != "I"
        ):
            matriz_combate_6x6[linha_sam][
                coluna_sam
            ] = piso_sam  # Atualiza a posição anterior de Sam na matriz
            piso_sam_novo = matriz_combate_6x6[nova_linha][
                nova_coluna
            ]  # Atualiza o novo piso de Sam
            matriz_combate_6x6[nova_linha][
                nova_coluna
            ] = "S"  # Atualiza a nova posição de Sam na matriz
            linha_sam, coluna_sam = (
                nova_linha,
                nova_coluna,
            )  # Atualiza a linha e coluna de Sam
            piso_sam = piso_sam_novo  # Atualiza o piso de Sam

    # Se a entrada for "Espingarda", "Rifle" ou "Metralhadora"...
    elif entrada in ["Espingarda", "Rifle", "Metralhadora"]:
        # Atualiza a quantidade de ações de Sam e a arma atual
        acoes_sam += 1
        arma_atual = entrada
        print(f"Arma trocada para {arma_atual}.")

    # Se a entrada for "Atirar"...
    elif entrada == "Atirar":
        # Atualiza a quantidade de ações de Sam e calcula a distância de Chebyshev entre Sam e Neil
        acoes_sam += 1
        distancia = distancia_chebyshev(linha_sam, coluna_sam, linha_neil, coluna_neil)
        dano, hp_neil = atirar_Sam(arma_atual, distancia, hp_neil)
        # Se o dano for maior que 0, atualiza a quantidade de hits de Neil
        if dano > 0:
            hits_neil += 1

    if (
        hp_sam > 0 and hp_neil > 0
    ):  # Se o piso de Sam for "F", perde 5 de vida e atualiza a quantidade de hits de fogo
        if piso_sam == "F":
            hp_sam -= 5
            hits_fogo_total += 1
    if hp_sam > 0 and hp_neil > 0:
        if acoes_sam == 4:  # Se a quantidade de ações de Sam for 4, Neil atira em Sam
            hp_sam -= 15
            dano_neil_total += 15
            print(">>> Você recebe um disparo de Neil! <<<")
            acoes_sam = 0
    if hp_sam > 0 and hp_neil > 0:
        if (
            hp_sam <= 40 and not aviso_40hp_dado
        ):  # Se a vida de Sam for menor ou igual a 40 e não tiver dado o aviso, vai dar o aviso
            print(
                "Dollman: A Fragile comeu todos os criptobiontes da DHV Magalhães... Se curar não é uma opção. Tome cuidado, Sam."
            )
            aviso_40hp_dado = True
    if hp_sam > 0 and hp_neil > 0:
        if hits_neil == 3:  # Se a quantidade de hits de Neil for 3, Neil teletransporta
            linha_neil, coluna_neil, piso_neil = teletransporte_neil(
                matriz_combate_6x6,
                linha_sam,
                coluna_sam,
                linha_neil,
                coluna_neil,
                piso_neil,
            )
            hits_neil = 0

if (
    hp_neil <= 0
):  # Se a vida de Neil for menor ou igual a 0, calcula a quantidade de likes e imprime a mensagem de missão completa
    likes = 1000 - (dano_neil_total * 8) - (hits_fogo_total * 10)
    print()
    print("MISSÃO COMPLETA! - Investigue a Anomalia")
    print("========================================")
    print(f"Likes recebidos: 👍 {likes}")
else:
    print()
    print("MISSÃO FALHOU")
    print("==============")
    print("Sam foi derrotado.")
    print("[Sua alma vaga pela Emenda, buscando reencontrar seu corpo perdido...]")
