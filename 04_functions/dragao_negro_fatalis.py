"""
Título: O Dragão Negro: Fatalis

Resumo do problema:
Simula um combate em turnos contra o Dragão Ancião Fatalis, no qual três caçadores,
cada um com uma arma distinta, executam ações ofensivas ou de suporte enquanto o
Fatalis responde com ataques de área ou eliminação direta baseada em status.

Regras de aprovação / lógica principal:
- O combate dura no máximo 4 turnos.
- Cada ação só ocorre se o personagem e o Fatalis estiverem vivos.
- O Fatalis perde vida conforme os ataques dos caçadores.
- Caçadores podem ser eliminados por dano direto ou instantaneamente pelo ataque
  "Mar de Chamas Negras", dependendo do status.
- Se o Fatalis chegar a 0 de vida antes do fim dos turnos, os caçadores vencem.
- Caso contrário, o Fatalis sobrevive.

Entradas:
- Ações dos três caçadores por turno (strings).
- Cor do extrato do Kinseto, quando aplicável.
- Ação do Fatalis por turno.
- Status dos caçadores caso o Fatalis use "Mar de Chamas Negras".

Saídas:
- Mensagens iniciais de início do combate.
- Mensagem final indicando vitória dos caçadores ou sobrevivência do Fatalis.
"""

vida_fatalis = 1800
vida_great_sword = 200
vida_glaive_inseto = 200
vida_fuzi_arco = 200
turnos = 0
jogo_ativo = True


# Função para Great Sword
def great_sword(atk):
    # Decisão: cada string de ataque mapeia um valor fixo de dano
    # permitindo isolar a lógica da arma do fluxo principal do combate
    if atk == "Golpe Carregado":
        return 165
    elif atk == "Corte Largo":
        return 120
    elif atk == "Divisor de Mundos":
        return 200
    else:
        return 0


# Função para Fuzi Arco
def fuzi_arco(atk):
    # Decisão: escolha do dano conforme o tipo de munição disparada
    # abstrai a variação de poder sem espalhar condicionais pelo código
    if atk == "Tiro Carregado":
        return 90
    elif atk == "Bala de Penetração":
        return 120
    elif atk == "Tiro Devastador":
        return 150
    else:
        return 0


# Função para Glaive Inseto
def glaive_inseto(atk, extrato):
    dano = 0
    cura = 0

    # Decisão: diferencia ataques diretos de ações condicionais ao extrato
    if atk == "Corte Aéreo":
        dano = 100
    elif atk == "Descida Carregada":
        dano = 120
    elif atk == "Kinseto":
        # Decisão dependente do estado externo (cor do extrato),
        # permitindo que a mesma ação gere dano ou cura
        if extrato_do_kinseto == "Vermelho":
            dano = 40
        elif extrato_do_kinseto == "Amarelo":
            dano = 15
        elif extrato_do_kinseto == "Verde":
            cura = 40
        else:
            dano = 0
    else:
        dano = 0

    return dano, cura


# Loop principal do combate
while turnos < 4 and jogo_ativo:
    # Decisão: o caçador só age se estiver vivo e se o Fatalis ainda não foi derrotado
    if vida_great_sword > 0 and vida_fatalis > 0:
        acao_cacador_great_sword = input()
        # Cálculo: subtração direta do dano causado pela arma na vida do Fatalis
        vida_fatalis -= great_sword(acao_cacador_great_sword)

    if vida_glaive_inseto > 0 and vida_fatalis > 0:
        extrato_do_kinseto = ""
        acao_cacador_glaive_inseto = input()

        # Decisão: só solicita o extrato se a ação exigir essa informação
        if acao_cacador_glaive_inseto == "Kinseto":
            extrato_do_kinseto = input()

        dano_glaive_inseto, cura_glaive_inseto = glaive_inseto(
            acao_cacador_glaive_inseto, extrato_do_kinseto
        )

        # Cálculo: dano reduz a vida do Fatalis
        vida_fatalis -= dano_glaive_inseto
        # Cálculo: cura restaura vida do caçador
        vida_glaive_inseto += cura_glaive_inseto

        # Decisão: vida máxima é limitada para evitar ultrapassar o valor inicial
        if vida_glaive_inseto > 200:
            vida_glaive_inseto = 200

    if vida_fuzi_arco > 0 and vida_fatalis > 0:
        acao_cacador_fuzi_arco = input()
        # Cálculo: aplicação direta do dano da arma de longo alcance
        vida_fatalis -= fuzi_arco(acao_cacador_fuzi_arco)

    # Decisão: se todos os caçadores morrerem, o combate termina
    if vida_fuzi_arco <= 0 and vida_glaive_inseto <= 0 and vida_great_sword <= 0:
        jogo_ativo = False

    # Decisão: se o Fatalis morrer, não executa ataque
    if vida_fatalis <= 0:
        jogo_ativo = False
    else:
        acao_fatalis = input()

        # Decisão: cada ataque do Fatalis define um padrão diferente de dano
        if acao_fatalis == "Ataque com Cauda":
            # Cálculo: dano em área aplicado apenas a caçadores vivos
            if vida_great_sword > 0:
                vida_great_sword -= 55
            if vida_glaive_inseto > 0:
                vida_glaive_inseto -= 55
            if vida_fuzi_arco > 0:
                vida_fuzi_arco -= 55

        elif acao_fatalis == "Bola de Fogo":
            # Cálculo: dano maior em área, reforçando o risco coletivo
            if vida_great_sword > 0:
                vida_great_sword -= 65
            if vida_glaive_inseto > 0:
                vida_glaive_inseto -= 65
            if vida_fuzi_arco > 0:
                vida_fuzi_arco -= 65

        elif acao_fatalis == "Mar de Chamas Negras":
            status_great_sword = input()
            status_glaive_inseto = input()
            status_fuzi_arco = input()

            # Decisão: eliminação instantânea depende exclusivamente do status
            if status_great_sword == "Desprotegido":
                vida_great_sword = 0
            if status_glaive_inseto == "Desprotegido":
                vida_glaive_inseto = 0
            if status_fuzi_arco == "Desprotegido":
                vida_fuzi_arco = 0

        # Decisão: encerra o jogo se não restar nenhum caçador vivo
        if vida_great_sword <= 0 and vida_glaive_inseto <= 0 and vida_fuzi_arco <= 0:
            jogo_ativo = False

    # Cálculo: avanço controlado do tempo do combate
    turnos += 1


# Output inicial do cenário
print("Hora de Lutar contra a Historia!\n")

# Decisão final: sobrevivência do Fatalis implica falha da missão
if vida_fatalis > 0:
    print("O Fatalis conseguiu sobreviver ao combate...\nO mundo corre perigo!")

# Decisão final: derrota do Fatalis implica sucesso da quinta frota
if vida_fatalis <= 0:
    print(
        "Eu não acredito, vocês conseguiram!\nObrigado caçadores! O mundo está salvo."
    )
