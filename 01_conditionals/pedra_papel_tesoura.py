doces = int(input())
jogador_1 = input()
jogador_2 = input()
rodadas = 0
jogada_jogador_1 = ""
jogada_jogador_2 = ""

if (jogador_1 != "Arthur") and (jogador_2 != "Arthur"):
    print("Epa!!! E cadê o dono dos doces??")
else:
    print("A batalha vai começar!")

    if doces % 10 != 0:
        x = doces % 10
        print(f"Pra aquecer, essa primeira vale menos, só {x} doces!")

    # INICIO DA BATALHA
    while doces > 0:
        rodadas = rodadas + 1
        vida_jogador_1 = 10
        vida_jogador_2 = 10
        if (rodadas != 1) or (doces % 10 == 0):
            print(f"Batalha número {rodadas}!")

        while (vida_jogador_1 > 0) and (vida_jogador_2 > 0):
            # PRIMEIRA RODADA COM RESTO DE DOCES
            jogada_jogador_1 = input()
            jogada_jogador_2 = input()
            # EMPATE
            if jogada_jogador_1 == jogada_jogador_2:
                print("Eita, jogaram a mesma coisa dessa vez.")
            # PAPEL E TESOURA
            elif (jogada_jogador_1 == "papel") and (jogada_jogador_2 == "tesoura"):
                vida_jogador_1 = max(0, vida_jogador_1 - 3)
                vida_jogador_2 = vida_jogador_2 + 1
                print(
                    f"Esse turno terminou com {jogador_1} tendo {vida_jogador_1} de vida e {jogador_2} tendo {vida_jogador_2}!"
                )
            elif (jogada_jogador_2 == "papel") and (jogada_jogador_1 == "tesoura"):
                vida_jogador_2 = max(0, vida_jogador_2 - 3)
                vida_jogador_1 = vida_jogador_1 + 1
                print(
                    f"Esse turno terminou com {jogador_1} tendo {vida_jogador_1} de vida e {jogador_2} tendo {vida_jogador_2}!"
                )
            # PEDRA E PAPEL
            elif (jogada_jogador_1 == "papel") and (jogada_jogador_2 == "pedra"):
                vida_jogador_1 = vida_jogador_1 + 2
                vida_jogador_2 = max(0, vida_jogador_2 - 2)
                print(
                    f"Esse turno terminou com {jogador_1} tendo {vida_jogador_1} de vida e {jogador_2} tendo {vida_jogador_2}!"
                )
            elif (jogada_jogador_2 == "papel") and (jogada_jogador_1 == "pedra"):
                vida_jogador_2 = vida_jogador_2 + 2
                vida_jogador_1 = max(0, vida_jogador_1 - 2)
                print(
                    f"Esse turno terminou com {jogador_1} tendo {vida_jogador_1} de vida e {jogador_2} tendo {vida_jogador_2}!"
                )
            # TESOURA E PEDRA
            elif (jogada_jogador_1 == "tesoura") and (jogada_jogador_2 == "pedra"):
                vida_jogador_1 = max(0, vida_jogador_1 - 4)
                print(
                    f"Esse turno terminou com {jogador_1} tendo {vida_jogador_1} de vida e {jogador_2} tendo {vida_jogador_2}!"
                )
            elif (jogada_jogador_2 == "tesoura") and (jogada_jogador_1 == "pedra"):
                vida_jogador_2 = max(0, vida_jogador_2 - 4)
                print(
                    f"Esse turno terminou com {jogador_1} tendo {vida_jogador_1} de vida e {jogador_2} tendo {vida_jogador_2}!"
                )
        if (rodadas == 1) and (doces % 10 != 0):
            doces = doces - x
        else:
            doces = doces - 10
        if vida_jogador_1 > vida_jogador_2:
            ganhador_rodada = jogador_1
        else:
            ganhador_rodada = jogador_2
        print(f"A rodada {rodadas} vai para {ganhador_rodada}, que garante seus doces!")
