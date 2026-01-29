"""
Questão: Front vs Back: O Deploy Decisivo! (Queimada)

Enunciado:
Simulação de uma partida de queimada entre 6 devs de Front-End e 6 de Back-End.
O jogo possui regras específicas para ataques do campo e ataques do "morto",
além de validação de inputs e mensagens de status a cada acerto.

Lógica Principal:
1. Estados:
   - time_atacante: Quem tem a bola.
   - atacando_do_morto: Booleano (False = Campo, True = Morto).

2. Fluxo de Ataque:
   - Acertou:
     - Vítima vai para o morto.
     - Se o ataque veio do morto, o atirador "renasce" (volta pro campo).
     - A bola vai para a vítima (agora no morto).
     - Troca de turno (time_atacante muda, atacando_do_morto vira True).

   - Errou:
     - Verifica se o atacante tem aliados no morto (se atacar do morto, sempre tem).
     - Se NÃO tem ninguém no morto: Turno passa para o oponente (Campo).
     - Se TEM alguém no morto: Pede input da defesa (pegou/deixou).
       - Pegou: Turno passa para o oponente (Campo).
       - Deixou: A bola fica com o mesmo time, mas troca de zona (Campo <-> Morto).

Input:
- Time inicial.
- Sequência de "acertou"/"errou" e "pegou"/"deixou".

Output:
- Status dos times após cada acerto.
- Mensagens de vitória quando um time zerar jogadores em campo.
"""

print(
    "Serão 12 desenvolvedores defendendo a honra de seus lados do código! Que vença a melhor stack!"
)

# --- CONFIGURAÇÃO INICIAL ---
back_campo = 6
front_campo = 6
back_morto = 0
front_morto = 0

# Validação do time inicial
time_atacante = input()
while time_atacante != "Front-End" and time_atacante != "Back-End":
    print("Entrada inválida!")
    time_atacante = input()

# Variável de Estado: Controla se a bola está no campo ou no morto
atacando_do_morto = False

# --- LOOP PRINCIPAL DO JOGO ---
# O jogo roda enquanto ambos os times tiverem jogadores em campo
while back_campo > 0 and front_campo > 0:

    # Define quem defende baseado em quem ataca
    if time_atacante == "Front-End":
        time_defensor = "Back-End"
    else:
        time_defensor = "Front-End"

    # Input do ataque com validação
    resultado_ataque = input()
    while resultado_ataque != "acertou" and resultado_ataque != "errou":
        print("Entrada inválida!")
        resultado_ataque = input()

    # --- CENÁRIO 1: ATAQUE ACERTOU ---
    if resultado_ataque == "acertou":
        # 1. Processa a eliminação do defensor
        if time_defensor == "Back-End":
            back_campo -= 1
            back_morto += 1
        else:
            front_campo -= 1
            front_morto += 1

        # 2. Processa o "Renascimento" (se o ataque veio do morto)
        if atacando_do_morto:
            if time_atacante == "Back-End":
                back_campo += 1
                back_morto -= 1
            else:
                front_campo += 1
                front_morto -= 1
            # Mensagem específica de acerto do morto
            print(f"O morto do {time_atacante} acertou um jogador!")
        else:
            # Mensagem específica de acerto do campo
            print(f"{time_atacante} acertou um jogador!")

        # 3. Imprime placar atualizado
        print(
            f"Back-End: {back_campo} dev(s) em campo. | Front-End: {front_campo} dev(s) em campo."
        )

        # 4. Troca de Turno: A bola vai para a vítima que acabou de ir para o morto
        time_atacante = time_defensor
        atacando_do_morto = True

    # --- CENÁRIO 2: ATAQUE ERROU ---
    else:  # errou

        # Verifica se é necessário perguntar sobre a defesa (se existe morto no time atacante)
        tem_morto = False
        if time_atacante == "Back-End" and back_morto > 0:
            tem_morto = True
        elif time_atacante == "Front-End" and front_morto > 0:
            tem_morto = True

        # Se tem morto (ou está atacando dele), a defesa pode deixar a bola escapar
        if tem_morto:
            resultado_defesa = input()
            while resultado_defesa != "pegou" and resultado_defesa != "deixou":
                print("Entrada inválida!")
                resultado_defesa = input()

            if resultado_defesa == "pegou":
                # Defesa segurou firme: Turno passa para o oponente (começa do campo)
                time_atacante = time_defensor
                atacando_do_morto = False

            else:  # deixou
                # Defesa deixou escapar: Bola fica com o atacante, mas troca de zona
                if atacando_do_morto:
                    # Estava no morto, escapou para o campo -> Ataca do campo
                    atacando_do_morto = False
                else:
                    # Estava no campo, escapou para o morto -> Ataca do morto
                    atacando_do_morto = True

        else:
            # Não tem ninguém no morto para receber a bola: Turno passa direto
            time_atacante = time_defensor
            atacando_do_morto = False

# --- FIM DE JOGO ---
if back_campo > 0:
    print(
        f"Vitória do Back-End! Restaram {back_campo} devs ainda mantendo o servidor de pé!"
    )
else:
    print(
        f"Vitória do Front-End! Restaram {front_campo} devs ainda segurando o layout!"
    )
