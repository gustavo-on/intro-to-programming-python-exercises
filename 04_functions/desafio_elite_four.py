# Função para calcular o multiplicador de dano com base no tipo do ataque e do defensor
def calcular_multiplicador(tipo_ataque, tipo_defensor):
    if tipo_ataque == "normal":
        return 1.0
    elif tipo_ataque == "fogo" and tipo_defensor == "grama":
        return 2.0
    elif tipo_ataque == "agua" and tipo_defensor == "fogo":
        return 2.0
    elif tipo_ataque == "grama" and tipo_defensor == "agua":
        return 2.0
    elif tipo_ataque == "eletrico" and tipo_defensor == "agua":
        return 2.0
    elif tipo_ataque == "fogo" and tipo_defensor == "agua":
        return 0.5
    elif tipo_ataque == "agua" and tipo_defensor == "grama":
        return 0.5
    elif tipo_ataque == "grama" and tipo_defensor == "fogo":
        return 0.5
    elif tipo_ataque == "agua" and tipo_defensor == "eletrico":
        return 0.5
    else:
        return 1.0


# Função para calcular o dano final
def calcular_dano_final(poder_ataque, defesa_defensor, tipo_ataque, tipo_defensor):
    multiplicador = calcular_multiplicador(tipo_ataque, tipo_defensor)
    dano_final = (poder_ataque - (defesa_defensor / 2)) * multiplicador
    dano_final_int = int(dano_final)
    # Se o dano final for menor que 1, ele será igual a 1
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
    # Enquanto ambos os pokemons estiverem vivos (HP maior que 0)
    while poke_jogador[2] > 0 and poke_oponente[2] > 0:
        print()
        print(f"-- Turno {turno} --")
        # Se a velocidade do pokemon do jogador for maior ou igual a do oponente, ele ataca primeiro...
        if poke_jogador[8] >= poke_oponente[8]:
            primeiro_a_atacar = "jogador"
            segundo_a_atacar = "oponente"
        # Caso contrário, o oponente ataca primeiro...
        else:
            primeiro_a_atacar = "oponente"
            segundo_a_atacar = "jogador"
        ordem = [primeiro_a_atacar, segundo_a_atacar]
        # Para cada atacante na ordem de ataque...
        for atacante_atual in ordem:
            # Se o atacante for o jogador, o defensor será o oponente...
            if atacante_atual == "jogador":
                atacante = poke_jogador
                defensor = poke_oponente
                se_oponente = ""
            # Caso contrário, o defensor será o jogador...
            else:
                atacante = poke_oponente
                defensor = poke_jogador
                se_oponente = " do oponente"
            # Se ambos os pokemons estiverem vivos (HP maior que 0)...
            if atacante[2] > 0 and defensor[2] > 0:
                print()
                # O atacante ataca o defensor...
                nome_ataque = atacante[5]
                print(f"{atacante[0]}{se_oponente} usa {nome_ataque}!")
                dano, mult = calcular_dano_final(
                    atacante[6], defensor[4], atacante[7], defensor[1]
                )
                # Se o multiplicador for 2, o ataque é super efetivo...
                if mult == 2.0:
                    print(f"{nome_ataque} é super efetivo!")
                # Se o multiplicador for 0.5, o ataque não é muito efetivo...
                elif mult == 0.5:
                    print(f"{nome_ataque} não é muito efetivo...")
                defensor[2] -= dano
                # Se o HP do defensor for menor que 0, ele será igual a 0
                if defensor[2] < 0:
                    defensor[2] = 0
                print(
                    f"Causou {dano} de dano. HP de {defensor[0]} agora é {defensor[2]}/{defensor[3]}."
                )
        turno += 1
    print()
    # Se o HP do pokemon do jogador for menor ou igual a 0, ele foi derrotado...
    if poke_jogador[2] <= 0:
        print(f"{poke_jogador[0]} foi derrotado!")
        return "oponente_venceu"
    # Caso contrário, o pokemon do oponente foi derrotado...
    else:
        print(f"{poke_oponente[0]} do oponente foi derrotado!")
        return "jogador_venceu"


# Função prinicipal em que as batalhas de turnos entre os pokemons irão ocorrer
def iniciar_liga_pokemon():
    print("Hora de montar seu time Pokémon!")
    time_jogador = []  # Lista para armazenar os pokemons do jogador
    # Para cada pokemon no time do jogador...
    for i in range(4):
        # 1. Montagem do Time do Jogador
        # O jogador digita as informações do pokemon...
        dados_juntos = input()  # Recebe os dados do pokemon em uma linha só
        dados = dados_juntos.split(" - ")  # Separa os dados do pokemon em uma lista
        # Cada dado do pokemon é armazenado em uma variável...
        nome = dados[0]
        tipo = dados[1]
        hp = int(dados[2])
        defe = int(dados[3])
        atk_nome = dados[4]
        atk_poder = int(dados[5])
        atk_tipo = dados[6]
        velo = int(dados[7])
        # O pokemon é adicionado ao time do jogador...
        pokemon_lista = [nome, tipo, hp, hp, defe, atk_nome, atk_poder, atk_tipo, velo]
        time_jogador.append(pokemon_lista)
    # 2. Escolha do Oponente da Elite Four:
    print()
    print("Qual membro da Elite Four você deseja enfrentar?")
    nome_oponente = input()
    print()
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
    # Enquanto os dois times tiverem pokemons vivos...
    while indice_pokemon_jogador < 4 and indice_pokemon_oponente < 4:
        poke_jogador_atual = time_jogador[indice_pokemon_jogador]
        poke_oponente_atual = time_oponente[indice_pokemon_oponente]
        resultado = batalha_pokemon(poke_jogador_atual, poke_oponente_atual, num_rodada)
        # Se o jogador vencer, o indice do pokemon do oponente aumenta...
        if resultado == "jogador_venceu":
            indice_pokemon_oponente += 1
        # Caso contrário, o indice do pokemon do jogador aumenta...
        else:
            indice_pokemon_jogador += 1
        print()
        print("--------------------")
        print()
        print(f"Placar: {indice_pokemon_oponente} X {indice_pokemon_jogador}")
        num_rodada += 1
    print()
    # Se o indice do pokemon do oponente for 4, o jogador venceu a liga...
    if indice_pokemon_oponente == 4:
        print("========================================")
        print("Parabéns! Você venceu a batalha Pokémon!")
        print("========================================")
    # Caso contrário, o jogador foi derrotado...
    else:
        print("========================================")
        print("Que pena! Você foi derrotado.")
        print("========================================")


iniciar_liga_pokemon()
