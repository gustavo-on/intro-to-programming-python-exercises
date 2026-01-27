def calcular_dano(poder_base, atk_usuario):
    dano = int(((poder_base * 15) ** 0.5) * (atk_usuario / 2))
    return dano


def get_poder_base(nome_golpe):
    if (
        nome_golpe == "Zio"
        or nome_golpe == "Garu"
        or nome_golpe == "Bufu"
        or nome_golpe == "Agi"
    ):
        return 3
    elif nome_golpe == "Corte" or nome_golpe == "Perfuração" or nome_golpe == "Pancada":
        return 4
    elif (
        nome_golpe == "Zionga"
        or nome_golpe == "Garula"
        or nome_golpe == "Agilao"
        or nome_golpe == "Bufula"
    ):
        return 5
    elif nome_golpe == "AtaqueFisico":
        return 2
    return 0


def contar_trocas_bubble(lista_original, ordem_crescente):
    lista = lista_original.copy()
    trocas = 0
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if ordem_crescente:
                if lista[j] > lista[j + 1]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]
                    trocas += 1
            else:
                if lista[j] < lista[j + 1]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]
                    trocas += 1
    return trocas


def analisar_golpe_bubble(input_lista_str):
    lista_str = input_lista_str.split()
    lista_int = []
    for item in lista_str:
        lista_int.append(int(item))
    ordenada_crescente = True
    ordenada_decrescente = True
    for i in range(len(lista_int) - 1):
        if lista_int[i] > lista_int[i + 1]:
            ordenada_crescente = False
        if lista_int[i] < lista_int[i + 1]:
            ordenada_decrescente = False
    if ordenada_crescente or ordenada_decrescente:
        return "fraqueza"
    trocas_crescente = contar_trocas_bubble(lista_int, True)
    trocas_decrescente = contar_trocas_bubble(lista_int, False)
    trocas_finais = min(trocas_crescente, trocas_decrescente)
    if trocas_finais <= 5:
        return "acerto"
    else:
        return "erro"


def checar_status_combate(sombras_info):
    todas_derrotadas = True
    todas_derrubadas_ou_derrotadas = True
    for sombra in sombras_info:
        estado_sombra = sombra[4]
        if estado_sombra != "Derrotado":
            todas_derrotadas = False
        if estado_sombra == "Ativo":
            todas_derrubadas_ou_derrotadas = False
    if todas_derrotadas:
        return "vitoria_total"
    if todas_derrubadas_ou_derrotadas:
        print("Mitsuru: Todos os inimigos cairam! Avancem com tudo!")
        print("MASS DESTRUCTION!")
        return "vitoria_conjunta"
    return "continua"


def turno_sombra(sombra, vida_makoto):
    if sombra[4] == "Derrubado":
        sombra[4] = "Ativo"
    if sombra[4] == "Ativo":
        poder_base = get_poder_base(sombra[3])
        ataque_sombra = sombra[2]
        dano = calcular_dano(poder_base, ataque_sombra)
        vida_makoto -= dano
        print(f"Mitsuru: Makoto foi atacado por {sombra[0]} e recebeu {dano} de dano!")
    return vida_makoto


def achar_alvo(sombras_info):
    for i in range(len(sombras_info)):
        if sombras_info[i][4] == "Ativo":
            return i
    return -1


def turno_makoto(
    vida_makoto,
    mana_makoto,
    sombras_info,
    usos_yukari,
    usos_junpei,
    persona_atual,
    vida_max_makoto,
):
    print("Makoto: O que fazer...")
    flag_mais_um = False
    flag_vitoria = False
    acao_valida = False
    while not acao_valida:
        acao = input()
        if acao not in ["yukari", "junpei", "atacar", "persona"]:
            acao_valida = False
        elif acao == "yukari":
            if usos_yukari > 0:
                acao_valida = True
                usos_yukari -= 1
                vida_makoto = min(vida_makoto + 100, vida_max_makoto)
                print("Yukari: Aguenta ai, líder!")
                print("Mitsuru: Bom trabalho, Yukari! Makoto se sente mais revigorado")
            else:
                print("Yukari: Estou exausta, foi mal!")
        elif acao == "junpei":
            if usos_junpei > 0:
                acao_valida = True
                alvo_idx = achar_alvo(sombras_info)
                if alvo_idx != -1:
                    usos_junpei -= 1
                    sombra_alvo = sombras_info[alvo_idx]
                    sombra_alvo[1] -= 100
                    sombra_alvo[4] = "Derrubado"
                    print("Junpei: HOOOOOME RUUUUN!!")
                    print(
                        f"Mitsuru: Acerto CRÍTICO de Junpei! {sombra_alvo[0]} sofreu 100 de dano!"
                    )
                    if sombra_alvo[1] <= 0:
                        sombra_alvo[4] = "Derrotado"
                        print(f"Mitsuru: {sombra_alvo[0]} foi derrotado!")
                    status_combate = checar_status_combate(sombras_info)
                    if (
                        status_combate == "vitoria_total"
                        or status_combate == "vitoria_conjunta"
                    ):
                        flag_vitoria = True
                    else:
                        flag_mais_um = True
                        print("MAIS UM!")
                        print("Mitsuru: Você acertou uma fraqueza! Continue no ataque!")
                else:
                    flag_vitoria = True
            else:
                print("Junpei: Cara, tô cansado!")
        elif acao == "atacar":
            acao_valida = True
            alvo_idx = achar_alvo(sombras_info)
            if alvo_idx != -1:
                sombra_alvo = sombras_info[alvo_idx]
                poder = get_poder_base("AtaqueFisico")
                atk_makoto = int(persona_atual[1])
                dano = calcular_dano(poder, atk_makoto)
                sombra_alvo[1] -= dano
                print(
                    f"Mitsuru: Makoto acertou {sombra_alvo[0]} causando {dano} de dano!"
                )
                if sombra_alvo[1] <= 0:
                    sombra_alvo[4] = "Derrotado"
                    print(f"Mitsuru: {sombra_alvo[0]} foi derrotado!")
                status_combate = checar_status_combate(sombras_info)
                if status_combate != "continua":
                    flag_vitoria = True
            else:
                flag_vitoria = True
        elif acao == "persona":
            custo_mana = int(persona_atual[3])
            if mana_makoto >= custo_mana:
                acao_valida = True
                mana_makoto -= custo_mana
                alvo_idx = achar_alvo(sombras_info)
                if alvo_idx != -1:
                    sombra_alvo = sombras_info[alvo_idx]
                    input_bubble_str = input()
                    resultado = analisar_golpe_bubble(input_bubble_str)
                    if resultado == "erro":
                        print("Makoto: O quê?!")
                        print("Mitsuru: Mais foco, Makoto!")
                    elif resultado == "acerto":
                        print("Makoto: Persona!")
                        poder = get_poder_base(persona_atual[2])
                        atk_makoto = int(persona_atual[1])
                        dano = calcular_dano(poder, atk_makoto)
                        sombra_alvo[1] -= dano
                        print(
                            f"Mitsuru: Makoto acertou {sombra_alvo[0]} causando {dano} de dano!"
                        )
                        if sombra_alvo[1] <= 0:
                            sombra_alvo[4] = "Derrotado"
                            print(f"Mitsuru: {sombra_alvo[0]} foi derrotado!")
                        status_combate = checar_status_combate(sombras_info)
                        if status_combate != "continua":
                            flag_vitoria = True
                    elif resultado == "fraqueza":
                        print(f"Makoto: Venha {persona_atual[0]}!")
                        poder = get_poder_base(persona_atual[2])
                        atk_makoto = int(persona_atual[1])
                        dano_base_float = ((poder * 15) ** 0.5) * (atk_makoto / 2)
                        dano = int(dano_base_float * 1.5)
                        sombra_alvo[1] -= dano
                        sombra_alvo[4] = "Derrubado"
                        print(
                            f"Mitsuru: Makoto acertou {sombra_alvo[0]} causando {dano} de dano!"
                        )
                        if sombra_alvo[1] <= 0:
                            sombra_alvo[4] = "Derrotado"
                            print(f"Mitsuru: {sombra_alvo[0]} foi derrotado!")
                        status_combate = checar_status_combate(sombras_info)
                        if (
                            status_combate == "vitoria_total"
                            or status_combate == "vitoria_conjunta"
                        ):
                            flag_vitoria = True
                        else:
                            flag_mais_um = True
                            print("MAIS UM!")
                            print(
                                "Mitsuru: Você acertou uma fraqueza! Continue no ataque!"
                            )
                else:
                    flag_vitoria = True
            else:
                print("Makoto: Estou cansado...")
    return [
        vida_makoto,
        mana_makoto,
        usos_yukari,
        usos_junpei,
        flag_mais_um,
        flag_vitoria,
    ]


def funcao_de_combate(
    vida_makoto,
    mana_makoto,
    sombras_info,
    persona_atual,
    vida_max_makoto,
    mana_max_makoto,
):
    usos_yukari = 2
    usos_junpei = 1
    n_turno = 1
    vitoria_combate = False
    indice_sombra_turno = 0
    while vida_makoto > 0 and not vitoria_combate:
        (
            vida_makoto,
            mana_makoto,
            usos_yukari,
            usos_junpei,
            flag_mais_um,
            vitoria_combate,
        ) = turno_makoto(
            vida_makoto,
            mana_makoto,
            sombras_info,
            usos_yukari,
            usos_junpei,
            persona_atual,
            vida_max_makoto,
        )

        if not vitoria_combate and vida_makoto > 0:
            if not flag_mais_um:
                sombra_atacou = False
                tentativas_turno = 0
                while not sombra_atacou and tentativas_turno < len(sombras_info):
                    sombra_da_vez = sombras_info[indice_sombra_turno]
                    if sombra_da_vez[4] != "Derrotado":
                        vida_makoto = turno_sombra(sombra_da_vez, vida_makoto)
                        sombra_atacou = True
                        indice_sombra_turno = (indice_sombra_turno + 1) % len(
                            sombras_info
                        )
                    else:
                        indice_sombra_turno = (indice_sombra_turno + 1) % len(
                            sombras_info
                        )
                    tentativas_turno += 1

            if vida_makoto > 0:
                print(f"TURNO {n_turno}:")
                print(f"HP Makoto: {vida_makoto} / {vida_max_makoto}")
                for sombra in sombras_info:
                    if sombra[4] != "Derrotado":
                        print(
                            f"HP {sombra[0]}: {max(sombra[1], 0)} pontos de vida restantes"
                        )
                n_turno += 1
    return (vida_makoto, mana_makoto, vitoria_combate)


def iniciar_exploracao():
    print("Mitsuru: Vamos iniciar nossa exploração, tomem cuidado.")
    vida_max_makoto = 300
    mana_max_makoto = 70
    vida_atual_makoto = 300
    mana_atual_makoto = 70
    andares_explorados = 0
    while vida_atual_makoto > 0:
        if andares_explorados > 0:
            vida_atual_makoto += 50
            if vida_atual_makoto > vida_max_makoto:
                vida_atual_makoto = vida_max_makoto
            mana_atual_makoto += 15
            if mana_atual_makoto > mana_max_makoto:
                mana_atual_makoto = mana_max_makoto
        input_persona_str = input()
        persona_atual = input_persona_str.split(" - ")
        print(f"{persona_atual[0]}: Eu sou tu e tu és eu...")
        n_sombras = int(input())
        sombras_do_andar = []
        for i in range(n_sombras):
            input_sombra_str = input()
            dados_sombra = input_sombra_str.split(" - ")
            sombras_do_andar.append(
                [
                    dados_sombra[0],
                    int(dados_sombra[1]),
                    int(dados_sombra[2]),
                    dados_sombra[3],
                    "Ativo",
                ]
            )
        print("Mitsuru: Inimigos detectados, se preparem!")
        (vida_atual_makoto, mana_atual_makoto, vitoria_combate) = funcao_de_combate(
            vida_atual_makoto,
            mana_atual_makoto,
            sombras_do_andar,
            persona_atual,
            vida_max_makoto,
            mana_max_makoto,
        )

        if vitoria_combate:
            print("Mitsuru: Muito bem! Continuem a exploração.")
            andares_explorados += 1
        else:
            print("Makoto: Argh...")
            print("Mitsuru: Líder? Aconteceu algo? Responda!")
            print()
            print("FIM DE JOGO")
            print(f"Andares explorados: {andares_explorados}")
            return


iniciar_exploracao()
