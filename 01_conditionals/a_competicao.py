"""
Questão: A Competição

Enunciado:
Simulação de uma competição com 3 fases: Bocatona, Corrida Volumosa e Grande Circuito.
Participam 4 detetives.

Regras:
1. Se "Terry" ou "Holt" estiverem entre os participantes, a competição é cancelada imediatamente.
2. Fase 1 (Bocatona): Se "Scully" participa, ele vence automaticamente. Caso contrário, lê-se vencedor e perdedor. O perdedor é eliminado.
3. Fase 2 (Corrida): Os 3 restantes informam tempos. O menor tempo vence a prova, o maior tempo é eliminado.
4. Fase 3 (Final): Disputa entre os 2 restantes.
   - Caso especial: Se finalistas forem "Jake" e "Amy", Amy vence automaticamente.
   - Caso contrário, lê-se o vencedor.

Entrada:
- 4 nomes de participantes.
- Dados da Bocatona (perdedor ou vencedor+perdedor).
- 3 tempos (int) para a Corrida.
- Vencedor final (se necessário).

Saída:
- Narrativa passo a passo da competição, indicando vencedores de etapas e eliminados.
"""

# Inputs iniciais dos participantes
participante_1 = input()
participante_2 = input()
participante_3 = input()
participante_4 = input()

# A mensagem de boas-vindas aparece em qualquer cenário
print("Bem-vindos ao Jimmy Jab!")

# Verificação de Cancelamento (Terry ou Holt)
# Usamos parênteses para organizar a leitura visual das condições
condicao_cancelamento = (
    (participante_1 == "Terry" or participante_1 == "Holt")
    or (participante_2 == "Terry" or participante_2 == "Holt")
    or (participante_3 == "Terry" or participante_3 == "Holt")
    or (participante_4 == "Terry" or participante_4 == "Holt")
)

if condicao_cancelamento:
    print("Jimmy Jab CANCELADO!")

else:
    # --- FASE 1: BOCATONA ---

    # Verifica se Scully está participando (Vitória automática)
    scully_participa = (
        participante_1 == "Scully"
        or participante_2 == "Scully"
        or participante_3 == "Scully"
        or participante_4 == "Scully"
    )

    if scully_participa:
        vencedor_bocatona = "Scully"
        perdedor_bocatona = input()
    else:
        vencedor_bocatona = input()
        perdedor_bocatona = input()

    # Definindo quem avança para a Fase 2 (Os "Terceiristas")
    # A ordem deve ser mantida, pulando apenas o eliminado
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

    # --- FASE 2: CORRIDA VOLUMOSA ---

    # Inputs dos tempos na ordem dos sobreviventes
    tempo_participante1 = int(input())
    tempo_participante2 = int(input())
    tempo_participante3 = int(input())

    tempo_maximo = max(tempo_participante1, tempo_participante2, tempo_participante3)
    tempo_minimo = min(tempo_participante1, tempo_participante2, tempo_participante3)

    # Identificando o perdedor da corrida (maior tempo)
    if tempo_maximo == tempo_participante1:
        perdedor_corrida = terceirista_1
    elif tempo_maximo == tempo_participante2:
        perdedor_corrida = terceirista_2
    else:
        perdedor_corrida = terceirista_3

    # Identificando o vencedor da corrida (menor tempo)
    if tempo_minimo == tempo_participante1:
        vencedor_corrida = terceirista_1
    elif tempo_minimo == tempo_participante2:
        vencedor_corrida = terceirista_2
    else:
        vencedor_corrida = terceirista_3

    # Definindo quem avança para a Fase 3 (Os Finalistas)
    if perdedor_corrida == terceirista_1:
        finalista_1, finalista_2 = terceirista_2, terceirista_3
    elif perdedor_corrida == terceirista_2:
        finalista_1, finalista_2 = terceirista_1, terceirista_3
    else:
        finalista_1, finalista_2 = terceirista_1, terceirista_2

    # --- FASE 3: GRANDE FINAL ---

    # Caso especial Jake vs Amy
    caso_jake_amy = (finalista_1 == "Amy" and finalista_2 == "Jake") or (
        finalista_1 == "Jake" and finalista_2 == "Amy"
    )

    if caso_jake_amy:
        empate_tecnico = True
        ganhador = "Amy"
    else:
        empate_tecnico = False
        ganhador = input()

    # Define quem ficou em segundo lugar
    if ganhador == finalista_1:
        segundo_lugar = finalista_2
    else:
        segundo_lugar = finalista_1

    # --- OUTPUTS DA COMPETIÇÃO ---
    print("Nosso primeiro evento é...\nA Bocatona!")

    if vencedor_bocatona == "Scully":
        print("Scully leva a melhor, não tem como competir com ele.")
    else:
        print(f"{vencedor_bocatona} levou a melhor na Bocatona!")

    print(f"{perdedor_bocatona} não avançou para a próxima fase!")

    print("O segundo evento é A corrida volumosa!")
    print(f"{vencedor_corrida} levou a melhor na Corrida Volumosa!")
    print(f"{perdedor_corrida} não avançou para a próxima fase!")

    if empate_tecnico:
        print("Jake ficou com o 2º lugar!")
        print("Amy VENCEU O JIMMY JABS!")
    else:
        print(f"{segundo_lugar} ficou com o 2º lugar!")
        print(f"{ganhador} VENCEU O JIMMY JABS!")
