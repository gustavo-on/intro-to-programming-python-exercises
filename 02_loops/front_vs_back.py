print(
    "Serão 12 desenvolvedores defendendo a honra de seus lados do código! Que vença a melhor stack!"
)

back_campo = 6
front_campo = 6

back_morto = 0
front_morto = 0

# Pedir time que começa com a bola
time_atacante = input()
while time_atacante != "Front-End" and time_atacante != "Back-End":
    print("Entrada inválida!")
    time_atacante = input()

# Variável para controlar se está atacando do morto
atacando_do_morto = False

# Loop principal do jogo
while back_campo > 0 and front_campo > 0:
    # Determinar time defensor
    if time_atacante == "Front-End":
        time_defensor = "Back-End"
    else:
        time_defensor = "Front-End"

    # Pedir resultado do ataque
    resultado_ataque = input()
    while resultado_ataque != "acertou" and resultado_ataque != "errou":
        print("Entrada inválida!")
        resultado_ataque = input()

    if resultado_ataque == "acertou":
        # Jogador acertado vai para o morto
        if time_defensor == "Back-End":
            back_campo -= 1
            back_morto += 1
        else:
            front_campo -= 1
            front_morto += 1

        # Se estava atacando do morto, jogador volta para o campo
        if atacando_do_morto:
            if time_atacante == "Back-End":
                back_campo += 1
                back_morto -= 1
            else:
                front_campo += 1
                front_morto -= 1
            print(f"O morto do {time_atacante} acertou um jogador!")
        else:
            print(f"{time_atacante} acertou um jogador!")

        print(
            f"Back-End: {back_campo} dev(s) em campo. | Front-End: {front_campo} dev(s) em campo."
        )

        # Bola passa para o morto do time defensor
        time_atacante = time_defensor
        atacando_do_morto = True

    else:  # errou
        # Verificar se há jogadores no morto do time atacante
        tem_morto = False
        if time_atacante == "Back-End" and back_morto > 0:
            tem_morto = True
        elif time_atacante == "Front-End" and front_morto > 0:
            tem_morto = True

        if tem_morto:
            # Pedir resultado da defesa
            resultado_defesa = input()
            while resultado_defesa != "pegou" and resultado_defesa != "deixou":
                print("Entrada inválida!")
                resultado_defesa = input()

            if resultado_defesa == "pegou":
                # Turno passa para o outro time
                time_atacante = time_defensor
                atacando_do_morto = False
            else:  # deixou
                # Bola vai para o morto, mesmo time ataca novamente
                if atacando_do_morto:
                    # Se já estava no morto, volta para o campo
                    atacando_do_morto = False
                else:
                    # Se estava no campo, vai para o morto
                    atacando_do_morto = True
        else:
            # Não há morto, turno passa normalmente
            time_atacante = time_defensor
            atacando_do_morto = False

# Mensagem de vitória
if back_campo > 0:
    print(
        f"Vitória do Back-End! Restaram {back_campo} devs ainda mantendo o servidor de pé!"
    )
else:
    print(
        f"Vitória do Front-End! Restaram {front_campo} devs ainda segurando o layout!"
    )
