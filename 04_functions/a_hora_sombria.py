"""
Título da questão: A Hora Sombria

Resumo do problema:
    Simulação de um sistema de combate RPG por turnos baseado em 'Persona 3'.
    O jogador (Makoto) explora andares infinitos da torre Tartarus, enfrentando
    sequências de sombras. O objetivo é sobreviver o máximo de andares possível,
    gerenciando Vida (HP), Mana (SP) e o uso de aliados (Yukari/Junpei).

Regras de aprovação ou lógica principal:
    1. Turnos: A ordem é Circular (Makoto -> Sombra 1 -> Makoto -> Sombra 2...).
       Sombras derrotadas são puladas.
    2. Mecânica de Ataque (Bubble Sort):
       - O jogador insere uma lista de números ao usar Persona.
       - Lista já ordenada (crescente ou decrescente): Acerta fraqueza (Dano x1.5 + Turno Extra "Mais Um").
       - Lista não ordenada: Conta-se o número de trocas necessárias para ordenar.
         - Se trocas <= 5: Acerto normal.
         - Se trocas > 5: Erro (0 dano).
    3. Condições de Vitória/Derrota:
       - Vitória Batalha: Todas as sombras derrotadas.
       - Ataque Total (Mass Destruction): Se todas as sombras ativas forem derrubadas, vitória imediata.
       - Derrota: Vida de Makoto chega a 0.
    4. Recuperação: +50 HP e +15 Mana ao fim de cada andar (respeitando o máximo).

Descrição de entradas e saídas:
    Entradas:
    - Dados iniciais: Persona atual (Nome-Atk-Golpe-Custo), Qtd Sombras, Dados Sombras (Nome-HP-Atk-Golpe).
    - Turno: Ação ('persona', 'atacar', 'yukari', 'junpei').
    - Se ação = 'persona': Lista de números inteiros para mecânica do Bubble Sort.

    Saídas:
    - Diálogos dos personagens (Mitsuru, Makoto, Aliados).
    - Logs de dano causado/recebido.
    - Relatório de status (HP) ao final de cada turno.
    - Estatísticas finais de andares explorados em caso de Game Over.
"""


def calcular_dano(poder_base, atk_usuario):
    # Aplica a fórmula de dano: raiz quadrada do (poder base * 15) multiplicado pela metade do ataque do usuário
    dano = int(((poder_base * 15) ** 0.5) * (atk_usuario / 2))
    return dano


def get_poder_base(nome_golpe):
    # Verifica se o golpe é do tipo mágico leve (Zio, Garu, Bufu, Agi) para definir poder base 3
    if (
        nome_golpe == "Zio"
        or nome_golpe == "Garu"
        or nome_golpe == "Bufu"
        or nome_golpe == "Agi"
    ):
        return 3
    # Verifica se o golpe é físico leve (Corte, Perfuração, Pancada) para definir poder base 4
    elif nome_golpe == "Corte" or nome_golpe == "Perfuração" or nome_golpe == "Pancada":
        return 4
    # Verifica se o golpe é mágico médio (Zionga, Garula, Agilao, Bufula) para definir poder base 5
    elif (
        nome_golpe == "Zionga"
        or nome_golpe == "Garula"
        or nome_golpe == "Agilao"
        or nome_golpe == "Bufula"
    ):
        return 5
    # Define poder base 2 para o ataque físico padrão de Makoto
    elif nome_golpe == "AtaqueFisico":
        return 2
    return 0


def contar_trocas_bubble(lista_original, ordem_crescente):
    lista = lista_original.copy()
    trocas = 0
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            # Decide a lógica de troca baseada na direção da ordenação (crescente vs decrescente)
            if ordem_crescente:
                # Se o elemento atual for maior que o próximo, realiza a troca (ordenação crescente)
                if lista[j] > lista[j + 1]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]
                    trocas += 1
            else:
                # Se o elemento atual for menor que o próximo, realiza a troca (ordenação decrescente)
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
        # Verifica se a lista quebra a ordem crescente
        if lista_int[i] > lista_int[i + 1]:
            ordenada_crescente = False
        # Verifica se a lista quebra a ordem decrescente
        if lista_int[i] < lista_int[i + 1]:
            ordenada_decrescente = False
    # Se a lista já estiver perfeitamente ordenada (em qualquer direção), define como ponto fraco
    if ordenada_crescente or ordenada_decrescente:
        return "fraqueza"

    # Calcula trocas necessárias para ambas as ordenações para encontrar o caminho mais curto
    trocas_crescente = contar_trocas_bubble(lista_int, True)
    trocas_decrescente = contar_trocas_bubble(lista_int, False)
    # Seleciona o menor número de trocas entre as duas possibilidades
    trocas_finais = min(trocas_crescente, trocas_decrescente)

    # Define o sucesso do golpe baseado no limite de 5 trocas
    if trocas_finais <= 5:
        return "acerto"
    else:
        return "erro"


def checar_status_combate(sombras_info):
    todas_derrotadas = True
    todas_derrubadas_ou_derrotadas = True
    for sombra in sombras_info:
        estado_sombra = sombra[4]
        # Verifica se ainda existe alguma sombra viva para continuar o combate
        if estado_sombra != "Derrotado":
            todas_derrotadas = False
        # Verifica se existe alguma sombra ativa (em pé) para impedir o ataque em conjunto
        if estado_sombra == "Ativo":
            todas_derrubadas_ou_derrotadas = False

    # Retorna vitória padrão se não houver inimigos
    if todas_derrotadas:
        return "vitoria_total"
    # Retorna vitória especial (Mass Destruction) se todos os inimigos vivos estiverem derrubados
    if todas_derrubadas_ou_derrotadas:
        print("Mitsuru: Todos os inimigos cairam! Avancem com tudo!")
        print("MASS DESTRUCTION!")
        return "vitoria_conjunta"
    return "continua"


def turno_sombra(sombra, vida_makoto):
    # Se a sombra estava derrubada, ela perde o turno apenas para se levantar
    if sombra[4] == "Derrubado":
        sombra[4] = "Ativo"
    # Se a sombra está ativa, ela calcula o dano e ataca Makoto
    if sombra[4] == "Ativo":
        poder_base = get_poder_base(sombra[3])
        ataque_sombra = sombra[2]
        dano = calcular_dano(poder_base, ataque_sombra)
        # Subtrai o dano calculado da vida atual de Makoto
        vida_makoto -= dano
        print(f"Mitsuru: Makoto foi atacado por {sombra[0]} e recebeu {dano} de dano!")
    return vida_makoto


def achar_alvo(sombras_info):
    for i in range(len(sombras_info)):
        # Retorna o índice da primeira sombra encontrada que ainda esteja ativa (não derrotada/derrubada)
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
        # Validação de entrada: garante que a ação esteja no conjunto permitido
        if acao not in ["yukari", "junpei", "atacar", "persona"]:
            acao_valida = False
        elif acao == "yukari":
            # Verifica disponibilidade de usos da cura da Yukari
            if usos_yukari > 0:
                acao_valida = True
                usos_yukari -= 1
                # Recupera 100 de vida, limitando-se ao valor máximo permitido (clamp)
                vida_makoto = min(vida_makoto + 100, vida_max_makoto)
                print("Yukari: Aguenta ai, líder!")
                print("Mitsuru: Bom trabalho, Yukari! Makoto se sente mais revigorado")
            else:
                print("Yukari: Estou exausta, foi mal!")
        elif acao == "junpei":
            # Verifica disponibilidade do ataque crítico do Junpei
            if usos_junpei > 0:
                acao_valida = True
                alvo_idx = achar_alvo(sombras_info)
                # Só executa se houver um alvo válido
                if alvo_idx != -1:
                    usos_junpei -= 1
                    sombra_alvo = sombras_info[alvo_idx]
                    # Aplica dano fixo de 100 e altera estado para Derrubado
                    sombra_alvo[1] -= 100
                    sombra_alvo[4] = "Derrubado"
                    print("Junpei: HOOOOOME RUUUUN!!")
                    print(
                        f"Mitsuru: Acerto CRÍTICO de Junpei! {sombra_alvo[0]} sofreu 100 de dano!"
                    )
                    # Verifica se a sombra morreu após o ataque
                    if sombra_alvo[1] <= 0:
                        sombra_alvo[4] = "Derrotado"
                        print(f"Mitsuru: {sombra_alvo[0]} foi derrotado!")

                    status_combate = checar_status_combate(sombras_info)
                    # Se o combate terminou com este ataque, define vitória
                    if (
                        status_combate == "vitoria_total"
                        or status_combate == "vitoria_conjunta"
                    ):
                        flag_vitoria = True
                    # Se o combate continua, Junpei garante um turno extra (Mais Um) para Makoto
                    else:
                        flag_mais_um = True
                        print("MAIS UM!")
                        print("Mitsuru: Você acertou uma fraqueza! Continue no ataque!")
                else:
                    # Se não há alvos ativos, considera vitória automática para evitar loop
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
                # Calcula dano físico padrão
                dano = calcular_dano(poder, atk_makoto)
                sombra_alvo[1] -= dano
                print(
                    f"Mitsuru: Makoto acertou {sombra_alvo[0]} causando {dano} de dano!"
                )
                # Verifica derrota da sombra
                if sombra_alvo[1] <= 0:
                    sombra_alvo[4] = "Derrotado"
                    print(f"Mitsuru: {sombra_alvo[0]} foi derrotado!")

                status_combate = checar_status_combate(sombras_info)
                # Se o status mudou para vitória, encerra o combate
                if status_combate != "continua":
                    flag_vitoria = True
            else:
                flag_vitoria = True
        elif acao == "persona":
            custo_mana = int(persona_atual[3])
            # Verifica se Makoto possui mana suficiente para o custo do golpe
            if mana_makoto >= custo_mana:
                acao_valida = True
                mana_makoto -= custo_mana
                alvo_idx = achar_alvo(sombras_info)
                if alvo_idx != -1:
                    sombra_alvo = sombras_info[alvo_idx]
                    input_bubble_str = input()
                    resultado = analisar_golpe_bubble(input_bubble_str)

                    # Lógica para erro no Bubble Sort (muitas trocas)
                    if resultado == "erro":
                        print("Makoto: O quê?!")
                        print("Mitsuru: Mais foco, Makoto!")

                    # Lógica para acerto normal (poucas trocas)
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

                    # Lógica para fraqueza (lista ordenada)
                    elif resultado == "fraqueza":
                        print(f"Makoto: Venha {persona_atual[0]}!")
                        poder = get_poder_base(persona_atual[2])
                        atk_makoto = int(persona_atual[1])
                        dano_base_float = ((poder * 15) ** 0.5) * (atk_makoto / 2)
                        # Aplica multiplicador de 1.5x por atingir fraqueza
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

                        # Se não venceu, concede turno extra (Mais Um)
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

    # Loop principal do combate: continua enquanto Makoto vive e as sombras não forem derrotadas
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
            # Se Makoto não ganhou turno extra (Mais Um), as sombras agem
            if not flag_mais_um:
                sombra_atacou = False
                tentativas_turno = 0
                # Loop para encontrar a próxima sombra viva na fila circular
                while not sombra_atacou and tentativas_turno < len(sombras_info):
                    sombra_da_vez = sombras_info[indice_sombra_turno]
                    # Apenas sombras não derrotadas podem agir
                    if sombra_da_vez[4] != "Derrotado":
                        vida_makoto = turno_sombra(sombra_da_vez, vida_makoto)
                        sombra_atacou = True
                        # Avança índice circularmente
                        indice_sombra_turno = (indice_sombra_turno + 1) % len(
                            sombras_info
                        )
                    else:
                        # Pula sombra derrotada e avança índice circularmente
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
    # Loop infinito de exploração: para apenas se a vida de Makoto chegar a 0
    while vida_atual_makoto > 0:
        if andares_explorados > 0:
            # Recupera status ao avançar de andar, respeitando os máximos
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
