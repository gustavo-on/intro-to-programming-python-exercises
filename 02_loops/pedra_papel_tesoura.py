"""
Título: Pedra, Papel, Tesoura

Resumo:
Simula um jogo de pedra-papel-tesoura estendido, onde dois jogadores disputam doces
em rodadas sucessivas. Cada rodada vale uma quantidade fixa de doces e é composta
por vários turnos até que um jogador perca todas as suas vidas.

Lógica principal:
- O jogo só acontece se Arthur for um dos jogadores.
- Os doces são disputados em rodadas de até 10 unidades.
- Cada rodada começa com ambos os jogadores tendo 10 vidas.
- A cada turno, as jogadas determinam perdas ou ganhos de vida conforme regras fixas.
- A rodada termina quando um jogador atinge 0 de vida.
- O jogo termina quando não há mais doces a serem distribuídos.

Entradas:
- Quantidade total de doces (int)
- Nome do jogador 1 (str)
- Nome do jogador 2 (str)
- Sequência de jogadas ("pedra", "papel" ou "tesoura"), duas por turno

Saídas:
- Mensagens informando início do jogo, rodadas, estados de vida a cada turno,
  empates, vencedor de cada rodada ou encerramento por ausência de Arthur.
"""

doces = int(input())
jogador_1 = input()
jogador_2 = input()
rodadas = 0
jogada_jogador_1 = ""
jogada_jogador_2 = ""

# Verifica se Arthur participa do jogo, condição obrigatória para iniciar
if (jogador_1 != "Arthur") and (jogador_2 != "Arthur"):
    print("Epa!!! E cadê o dono dos doces??")
else:
    print("A batalha vai começar!")

    # Se a quantidade de doces não for múltipla de 10,
    # a primeira rodada vale apenas o resto da divisão
    if doces % 10 != 0:
        x = doces % 10
        print(f"Pra aquecer, essa primeira vale menos, só {x} doces!")

    # Loop principal: continua enquanto ainda houver doces a disputar
    while doces > 0:
        rodadas = rodadas + 1
        vida_jogador_1 = 10
        vida_jogador_2 = 10

        # Imprime o cabeçalho da rodada,
        # exceto quando a primeira rodada já foi anunciada como especial
        if (rodadas != 1) or (doces % 10 == 0):
            print(f"Batalha número {rodadas}!")

        # Cada rodada continua até que um dos jogadores fique sem vidas
        while (vida_jogador_1 > 0) and (vida_jogador_2 > 0):
            jogada_jogador_1 = input()
            jogada_jogador_2 = input()

            # Empate: nenhuma modificação de vida ocorre
            if jogada_jogador_1 == jogada_jogador_2:
                print("Eita, jogaram a mesma coisa dessa vez.")

            # Papel perde para tesoura: penaliza papel e recompensa tesoura
            elif (jogada_jogador_1 == "papel") and (jogada_jogador_2 == "tesoura"):
                vida_jogador_1 = max(0, vida_jogador_1 - 3)  # evita vida negativa
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

            # Pedra perde para papel: penaliza pedra e recompensa papel
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

            # Tesoura perde para pedra: apenas tesoura perde vidas
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

        # Desconta a quantidade correta de doces após a rodada
        if (rodadas == 1) and (doces % 10 != 0):
            doces = doces - x
        else:
            doces = doces - 10

        # O vencedor da rodada é quem terminou com mais vida
        if vida_jogador_1 > vida_jogador_2:
            ganhador_rodada = jogador_1
        else:
            ganhador_rodada = jogador_2

        print(f"A rodada {rodadas} vai para {ganhador_rodada}, que garante seus doces!")
