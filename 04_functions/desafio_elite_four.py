"""
Título: O Desafio da Elite Four!

Resumo do Problema:
Simular batalhas Pokémon no formato 4x4 entre o jogador e um membro da Elite Four,
respeitando regras de vantagem de tipo, cálculo de dano, ordem de ataque por velocidade
e progressão contínua dos Pokémon sobreviventes até a derrota total de um dos times.

Lógica Principal / Regras de Aprovação:
- Cada Pokémon possui apenas um tipo e um ataque.
- O dano depende do poder do ataque, da defesa do defensor e do multiplicador de tipo.
- Ataques super efetivos causam o dobro do dano; não muito efetivos causam metade.
- Todo ataque causa no mínimo 1 de dano.
- O Pokémon mais rápido ataca primeiro; empate favorece o jogador.
- O Pokémon vencedor continua a próxima rodada com o HP restante.
- A batalha termina quando um dos times perde os quatro Pokémon.

Entradas:
- 4 linhas descrevendo os Pokémon do jogador (nome, tipo, HP, defesa, ataque, etc.).
- 1 linha com o nome do oponente da Elite Four ("lorelei", "bruno", "agatha" ou "lance").

Saídas:
- Impressão detalhada da batalha por rodadas e turnos.
- Mensagens de ataques, eficácia, dano causado e HP restante.
- Placar após cada duelo.
- Mensagem final de vitória ou derrota.
"""


# Função para calcular o multiplicador de dano com base no tipo do ataque e do defensor
def calcular_multiplicador(tipo_ataque, tipo_defensor):
    # Ataques normais não sofrem influência de tipo
    if tipo_ataque == "normal":
        return 1.0

    # Casos de vantagem de tipo (super efetivo)
    elif tipo_ataque == "fogo" and tipo_defensor == "grama":
        return 2.0
    elif tipo_ataque == "agua" and tipo_defensor == "fogo":
        return 2.0
    elif tipo_ataque == "grama" and tipo_defensor == "agua":
        return 2.0
    elif tipo_ataque == "eletrico" and tipo_defensor == "agua":
        return 2.0

    # Casos de desvantagem de tipo (não muito efetivo)
    elif tipo_ataque == "fogo" and tipo_defensor == "agua":
        return 0.5
    elif tipo_ataque == "agua" and tipo_defensor == "grama":
        return 0.5
    elif tipo_ataque == "grama" and tipo_defensor == "fogo":
        return 0.5
    elif tipo_ataque == "agua" and tipo_defensor == "eletrico":
        return 0.5

    # Qualquer outro confronto é considerado neutro
    else:
        return 1.0


# Função para calcular o dano final
def calcular_dano_final(poder_ataque, defesa_defensor, tipo_ataque, tipo_defensor):
    # Determina o multiplicador de tipo antes do cálculo do dano
    multiplicador = calcular_multiplicador(tipo_ataque, tipo_defensor)

    # Fórmula oficial do problema: ataque menos metade da defesa, ajustado pelo tipo
    dano_final = (poder_ataque - (defesa_defensor / 2)) * multiplicador

    # Conversão para inteiro conforme especificação do enunciado
    dano_final_int = int(dano_final)

    # Garante que todo ataque cause pelo menos 1 de dano
    if dano_final_int < 1:
        dano_final_int = 1

    return dano_final_int, multiplicador


# Função para o manejo do combate em turnos entre dois pokemons
def batalha_pokemon(poke_jogador, poke_oponente, num_rodada):
    print()
    print(f"--- Rodada {num_rodada} ---")
    print(f"{poke_jogador[0]}, eu escolho você!")
    print(f"{poke_oponente[0]}, vai!")
    print("--------------------")

    turno = 1

    # O combate continua enquanto ambos tiverem HP positivo
    while poke_jogador[2] > 0 and poke_oponente[2] > 0:
        print()
        print(f"-- Turno {turno} --")

        # Define quem ataca primeiro com base na velocidade
        # Empate favorece o jogador conforme regra do problema
        if poke_jogador[8] >= poke_oponente[8]:
            primeiro_a_atacar = "jogador"
            segundo_a_atacar = "oponente"
        else:
            primeiro_a_atacar = "oponente"
            segundo_a_atacar = "jogador"

        ordem = [primeiro_a_atacar, segundo_a_atacar]

        for atacante_atual in ordem:
            # Determina dinamicamente atacante e defensor
            if atacante_atual == "jogador":
                atacante = poke_jogador
                defensor = poke_oponente
                se_oponente = ""
            else:
                atacante = poke_oponente
                defensor = poke_jogador
                se_oponente = " do oponente"

            # Ataque só ocorre se ambos ainda estiverem vivos
            if atacante[2] > 0 and defensor[2] > 0:
                print()
                nome_ataque = atacante[5]
                print(f"{atacante[0]}{se_oponente} usa {nome_ataque}!")

                # Calcula dano considerando ataque, defesa e tipos
                dano, mult = calcular_dano_final(
                    atacante[6], defensor[4], atacante[7], defensor[1]
                )

                # Mensagem contextual baseada na eficácia do ataque
                if mult == 2.0:
                    print(f"{nome_ataque} é super efetivo!")
                elif mult == 0.5:
                    print(f"{nome_ataque} não é muito efetivo...")

                # Aplica o dano ao HP do defensor
                defensor[2] -= dano

                # Evita HP negativo para manter consistência visual
                if defensor[2] < 0:
                    defensor[2] = 0

                print(
                    f"Causou {dano} de dano. HP de {defensor[0]} agora é {defensor[2]}/{defensor[3]}."
                )

        turno += 1

    print()

    # Determina o vencedor do duelo individual
    if poke_jogador[2] <= 0:
        print(f"{poke_jogador[0]} foi derrotado!")
        return "oponente_venceu"
    else:
        print(f"{poke_oponente[0]} do oponente foi derrotado!")
        return "jogador_venceu"


# Função principal que coordena toda a liga Pokémon
def iniciar_liga_pokemon():
    print("Hora de montar seu time Pokémon!")
    time_jogador = []

    # Leitura e montagem do time do jogador
    for i in range(4):
        dados_juntos = input()
        dados = dados_juntos.split(" - ")

        nome = dados[0]
        tipo = dados[1]
        hp = int(dados[2])
        defe = int(dados[3])
        atk_nome = dados[4]
        atk_poder = int(dados[5])
        atk_tipo = dados[6]
        velo = int(dados[7])

        # Estrutura fixa para facilitar acesso por índice durante a batalha
        pokemon_lista = [nome, tipo, hp, hp, defe, atk_nome, atk_poder, atk_tipo, velo]
        time_jogador.append(pokemon_lista)

    print()
    print("Qual membro da Elite Four você deseja enfrentar?")
    nome_oponente = input()
    print()

    # Times pré-definidos da Elite Four
    time_lorelei = [
        ["Lapras", "agua", 220, 220, 50, "Raio de Gelo", 60, "agua", 60],
        ["Blastoise", "agua", 180, 180, 55, "Hidro Bomba", 65, "agua", 78],
        ["Victreebel", "grama", 160, 160, 40, "Folha Navalha", 55, "grama", 70],
        ["Ninetales", "fogo", 170, 170, 45, "Lança-chamas", 60, "fogo", 100],
    ]
    time_bruno = [
        ["Charizard", "fogo", 190, 190, 40, "Presa de Fogo", 70, "fogo", 100],
        ["Arcanine", "fogo", 180, 180, 50, "Velocidade Extrema", 60, "fogo", 95],
        ["Kingler", "agua", 170, 170, 60, "Caranguejo Martelo", 65, "agua", 75],
        ["Jolteon", "eletrico", 150, 150, 35, "Choque do Trovão", 55, "eletrico", 130],
    ]
    time_agatha = [
        ["Venusaur", "grama", 180, 180, 50, "Raio Solar", 70, "grama", 80],
        ["Vileplume", "grama", 160, 160, 45, "Pó do Sono", 50, "grama", 50],
        ["Raichu", "eletrico", 160, 160, 40, "Investida Trovão", 65, "eletrico", 110],
        ["Poliwrath", "agua", 190, 190, 55, "Soco Dinâmico", 60, "agua", 70],
    ]
    time_lance = [
        ["Electabuzz", "eletrico", 180, 180, 45, "Soco de Trovão", 75, "eletrico", 105],
        ["Jolteon", "eletrico", 170, 170, 35, "Onda de Trovão", 60, "eletrico", 130],
        ["Exeggutor", "grama", 160, 160, 40, "Bomba de Semente", 65, "grama", 55],
        ["Magmar", "fogo", 175, 175, 40, "Giro de Fogo", 55, "fogo", 93],
    ]

    # Seleção do time adversário com base na entrada do usuário
    if nome_oponente == "lorelei":
        time_oponente = time_lorelei
    elif nome_oponente == "bruno":
        time_oponente = time_bruno
    elif nome_oponente == "agatha":
        time_oponente = time_agatha
    elif nome_oponente == "lance":
        time_oponente = time_lance

    print("====================")
    print("A BATALHA VAI COMEÇAR!")
    print("====================")

    indice_pokemon_jogador = 0
    indice_pokemon_oponente = 0
    num_rodada = 1

    # A liga continua enquanto ambos ainda tiverem Pokémon disponíveis
    while indice_pokemon_jogador < 4 and indice_pokemon_oponente < 4:
        poke_jogador_atual = time_jogador[indice_pokemon_jogador]
        poke_oponente_atual = time_oponente[indice_pokemon_oponente]

        resultado = batalha_pokemon(poke_jogador_atual, poke_oponente_atual, num_rodada)

        # Atualiza o índice do time derrotado
        if resultado == "jogador_venceu":
            indice_pokemon_oponente += 1
        else:
            indice_pokemon_jogador += 1

        print()
        print("--------------------")
        print()
        print(f"Placar: {indice_pokemon_oponente} X {indice_pokemon_jogador}")

        num_rodada += 1

    print()

    # Condição final de vitória ou derrota
    if indice_pokemon_oponente == 4:
        print("========================================")
        print("Parabéns! Você venceu a batalha Pokémon!")
        print("========================================")
    else:
        print("========================================")
        print("Que pena! Você foi derrotado.")
        print("========================================")


iniciar_liga_pokemon()
