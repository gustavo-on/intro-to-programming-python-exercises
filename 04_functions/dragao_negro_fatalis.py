vida_fatalis = 1800
vida_great_sword = 200
vida_glaive_inseto = 200
vida_fuzi_arco = 200
turnos = 0
jogo_ativo = True


# Função para Great Sword
def great_sword(atk):
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
    if atk == "Corte Aéreo":
        dano = 100
    elif atk == "Descida Carregada":
        dano = 120
    elif atk == "Kinseto":
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


# Loop do jogo: Enquanto o jogo estiver ativo e os turnos forem menores que 4, o loop continua rodando.
while turnos < 4 and jogo_ativo:
    if vida_great_sword > 0 and vida_fatalis > 0:
        acao_cacador_great_sword = input()
        vida_fatalis -= great_sword(acao_cacador_great_sword)

    if vida_glaive_inseto > 0 and vida_fatalis > 0:
        extrato_do_kinseto = ""
        acao_cacador_glaive_inseto = input()
        if acao_cacador_glaive_inseto == "Kinseto":
            extrato_do_kinseto = input()
        dano_glaive_inseto, cura_glaive_inseto = glaive_inseto(
            acao_cacador_glaive_inseto, extrato_do_kinseto
        )
        vida_fatalis -= dano_glaive_inseto
        vida_glaive_inseto += cura_glaive_inseto
        if vida_glaive_inseto > 200:
            vida_glaive_inseto = 200

    if vida_fuzi_arco > 0 and vida_fatalis > 0:
        acao_cacador_fuzi_arco = input()
        vida_fatalis -= fuzi_arco(acao_cacador_fuzi_arco)

    if vida_fuzi_arco <= 0 and vida_glaive_inseto <= 0 and vida_great_sword <= 0:
        jogo_ativo = False
    if vida_fatalis <= 0:
        jogo_ativo = False
    else:
        acao_fatalis = input()
        if acao_fatalis == "Ataque com Cauda":
            if vida_great_sword > 0:
                vida_great_sword -= 55
            if vida_glaive_inseto > 0:
                vida_glaive_inseto -= 55
            if vida_fuzi_arco > 0:
                vida_fuzi_arco -= 55
        elif acao_fatalis == "Bola de Fogo":
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
            if status_great_sword == "Desprotegido":
                vida_great_sword = 0
            if status_glaive_inseto == "Desprotegido":
                vida_glaive_inseto = 0
            if status_fuzi_arco == "Desprotegido":
                vida_fuzi_arco = 0
        if vida_great_sword <= 0 and vida_glaive_inseto <= 0 and vida_fuzi_arco <= 0:
            jogo_ativo = False
    turnos += 1

# Output:
print("Hora de Lutar contra a Historia!\n")

# Caso o fatalis sobreviva aos 4 turnos:
if vida_fatalis > 0:
    print("O Fatalis conseguiu sobreviver ao combate...\nO mundo corre perigo!")

# Caso a quinta frota consiga eliminar o fatalis:
if vida_fatalis <= 0:
    print(
        "Eu não acredito, vocês conseguiram!\nObrigado caçadores! O mundo está salvo."
    )
