# Jimmy Jab = Bocatona, Corrida volumosa e Grande circuito final
# Provas eliminatórias
# 4 participantes somente. Se o Sargento Jeffords ou o Capitão Holt estiverem infiltrados, a competição é cancelada

participante_1 = input()
participante_2 = input()
participante_3 = input()
participante_4 = input()

# TERRY OU HOLT
if (
    (participante_1 == "Terry" or participante_1 == "Holt")
    or (participante_2 == "Terry" or participante_2 == "Holt")
    or (participante_3 == "Terry" or participante_3 == "Holt")
    or (participante_4 == "Terry" or participante_4 == "Holt")
):
    print("Bem-vindos ao Jimmy Jab!")
    print("Jimmy Jab CANCELADO!")

else:
    # BOCATONA : COMER MAIOR QUANTIDADE DE COMIDA
    if (
        (participante_1 == "Scully")
        or (participante_2 == "Scully")
        or (participante_3 == "Scully")
        or (participante_4 == "Scully")
    ):
        vencedor_bocatona = "Scully"
        perdedor_bocatona = input()
    else:
        vencedor_bocatona = input()
        perdedor_bocatona = input()

    # CORRIDA VOLUMOSA: PARTICIPANTES RESTANTES INFORMAM UM NÚMERO, MESMA ORDEM,
    tempo_participante1 = int(input())
    tempo_participante2 = int(input())
    tempo_participante3 = int(input())
    tempo_maximo = max(tempo_participante1, tempo_participante2, tempo_participante3)
    tempo_minimo = min(tempo_participante1, tempo_participante2, tempo_participante3)

    if perdedor_bocatona == participante_1:
        terceirista_1, terceirista_2, terceirista_3 = (
            participante_2,
            participante_3,
            participante_4,
        )
    elif perdedor_bocatona == participante_2:
        terceirista_1, terceirista_2, terceirista_3 = (
            participante_1,
            participante_3,
            participante_4,
        )
    elif perdedor_bocatona == participante_3:
        terceirista_1, terceirista_2, terceirista_3 = (
            participante_1,
            participante_2,
            participante_4,
        )
    else:
        terceirista_1, terceirista_2, terceirista_3 = (
            participante_1,
            participante_2,
            participante_3,
        )

    if tempo_maximo == tempo_participante1:
        perdedor_corrida = terceirista_1
    elif tempo_maximo == tempo_participante2:
        perdedor_corrida = terceirista_2
    else:
        perdedor_corrida = terceirista_3

    if tempo_minimo == tempo_participante1:
        vencedor_corrida = terceirista_1
    elif tempo_minimo == tempo_participante2:
        vencedor_corrida = terceirista_2
    else:
        vencedor_corrida = terceirista_3

    if perdedor_corrida == terceirista_1:
        finalista_1, finalista_2 = terceirista_2, terceirista_3
    elif perdedor_corrida == terceirista_2:
        finalista_1, finalista_2 = terceirista_1, terceirista_3
    else:
        finalista_1, finalista_2 = terceirista_1, terceirista_2

    if (finalista_1 == "Amy" and finalista_2 == "Jake") or (
        finalista_1 == "Jake" and finalista_2 == "Amy"
    ):
        empate = "sim"
        ganhador = "Amy"
    else:
        empate = "nao"
        ganhador = input()

    if ganhador == finalista_1:
        finalista = finalista_2
    else:
        finalista = finalista_1

    print("Bem-vindos ao Jimmy Jab!")
    print("Nosso primeiro evento é...\nA Bocatona!")
    if vencedor_bocatona == "Scully":
        print("Scully leva a melhor, não tem como competir com ele.")
    else:
        print(f"{vencedor_bocatona} levou a melhor na Bocatona!")
    print(f"{perdedor_bocatona} não avançou para a próxima fase!")
    print("O segundo evento é A corrida volumosa!")
    print(
        f"{vencedor_corrida} levou a melhor na Corrida Volumosa!\n{perdedor_corrida} não avançou para a próxima fase!"
    )
    if empate == "sim":
        print("Jake ficou com o 2º lugar!\nAmy VENCEU O JIMMY JABS!")
    else:
        print(f"{finalista} ficou com o 2º lugar!\n{ganhador} VENCEU O JIMMY JABS!")
