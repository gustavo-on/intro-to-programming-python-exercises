# Inputs:
num_sessoes_treino = int(input())
total_partidas = num_sessoes_treino
habilidade_inicial_luva = int(input())
sequencia_treinos_goleiros = input().split("-")
goleiros_especiais = [
    "Rokenedy",
    "IShowSpeed",
    "Sérgio Soares",
    "Neymar Jr",
    "Gabriel Vasconcelos",
]

meta_sessao = (
    100 - habilidade_inicial_luva
) / num_sessoes_treino  # Meta de evolução por treino
# Output:
print("RECEBA! É hoje que eu me torno o melhor dos melhores.")
# Habilidade inicial do Luva:
if 0 <= habilidade_inicial_luva <= 5:
    print("A gente tem que começar de algum lugar, né? RECEBA!")
elif 6 <= habilidade_inicial_luva <= 15:
    print("Não tem jeito, vou ser o melhor do mundo!")
elif 16 <= habilidade_inicial_luva:
    print("O Pai tá estourado! RECEBA!")

# Meta por partida:
print(f"Meta por Partida: {meta_sessao}")

num_partida = 1
indice_lista = 0
while habilidade_inicial_luva <= 100 and num_sessoes_treino > 0:
    tipo_partida = sequencia_treinos_goleiros[indice_lista]
    goleiro_atual = sequencia_treinos_goleiros[indice_lista + 1]
    print(f"TIPO DE PARTIDA: {tipo_partida}")
    print(f"Nome do Goleiro: {goleiro_atual}")
    if goleiro_atual not in goleiros_especiais:
        habilidade_goleiro = int(input())

    if tipo_partida == "Batida de Falta":
        matriz_falta = eval(input())
        x = int(input())
        y = int(input())
        if matriz_falta[x][y] == 1:  # Foi gol
            foi_gol = True
            if goleiro_atual == "Rokenedy":
                pontos_ganhos = 0
                print("Aí não dá, impossível de fazer gol no maior do mundo.")
                foi_gol = False
            elif goleiro_atual == "IShowSpeed":
                pontos_ganhos = 1.5 * meta_sessao
                print("REBECA? Is that you?")
                print("Ispidi mai friand, recieve!")
            elif goleiro_atual == "Sérgio Soares":
                pontos_ganhos = 0
                print(
                    "DALE DALE, PROFESSOR! Quero ver se esse tal de Python é bom mesmo…"
                )
                foi_gol = False
            elif goleiro_atual == "Neymar Jr":
                pontos_ganhos = 0.5 * meta_sessao
                print("Ele nem sabe agarrar! A arma dele é a sua fragilidade…")
            elif goleiro_atual == "Gabriel Vasconcelos":
                pontos_ganhos = 2 * meta_sessao
                print("HAHAHA! Eu pedi um desafio, não uma barra sem goleiro…")
            else:
                if habilidade_inicial_luva > habilidade_goleiro:
                    pontos_ganhos = habilidade_inicial_luva - habilidade_goleiro
                else:
                    pontos_ganhos = 0

            if foi_gol:
                print("RECEBA! GOLAÇO! É O MELHOR DO MUNDO!")
            else:
                print("A jornada ainda não acabou!")
        else:
            pontos_ganhos = 0
            print("A jornada ainda não acabou!")

    # Se o tipo de partida for batida de pênalti:
    elif tipo_partida == "Batida de Pênalti":
        matriz_penalti = eval(input())
        x = int(input())
        y = int(input())
        if matriz_penalti[x][y] == 1:  # Foi gol
            foi_gol = True
            if goleiro_atual == "Rokenedy":
                pontos_ganhos = 0
                print("Aí não dá, impossível de fazer gol no maior do mundo.")
                foi_gol = False
            elif goleiro_atual == "IShowSpeed":
                pontos_ganhos = 1.5 * meta_sessao
                print("REBECA? Is that you?")
                print("Ispidi mai friand, recieve!")
            elif goleiro_atual == "Sérgio Soares":
                pontos_ganhos = meta_sessao
                print(
                    "DALE DALE, PROFESSOR! Quero ver se esse tal de Python é bom mesmo…"
                )
            elif goleiro_atual == "Neymar Jr":
                pontos_ganhos = 0.5 * meta_sessao
                print("Ele nem sabe agarrar! A arma dele é a sua fragilidade…")
            elif goleiro_atual == "Gabriel Vasconcelos":
                pontos_ganhos = 2 * meta_sessao
                print("HAHAHA! Eu pedi um desafio, não uma barra sem goleiro…")
            else:
                if habilidade_inicial_luva > habilidade_goleiro:
                    pontos_ganhos = habilidade_inicial_luva - habilidade_goleiro
                else:
                    pontos_ganhos = 0

            if foi_gol:
                print("RECEBA! GOLAÇO! É O MELHOR DO MUNDO!")
            else:
                print("A jornada ainda não acabou!")
        else:
            pontos_ganhos = 0
            print("A jornada ainda não acabou!")

    # Se o tipo de partida for batida de ataque:
    elif tipo_partida == "Batida de Ataque":
        matriz_ataque = eval(input())
        x = int(input())
        y = int(input())
        if matriz_ataque[x][y] == 1:  # Foi gol
            foi_gol = True
            if goleiro_atual == "Rokenedy":
                pontos_ganhos = 0
                print("Aí não dá, impossível de fazer gol no maior do mundo.")
                foi_gol = False
            elif goleiro_atual == "IShowSpeed":
                pontos_ganhos = 1.5 * meta_sessao
                print("REBECA? Is that you?")
                print("Ispidi mai friand, recieve!")
            elif goleiro_atual == "Sérgio Soares":
                pontos_ganhos = 0
                print(
                    "DALE DALE, PROFESSOR! Quero ver se esse tal de Python é bom mesmo…"
                )
                foi_gol = False
            elif goleiro_atual == "Neymar Jr":
                pontos_ganhos = 0.5 * meta_sessao
                print("Ele nem sabe agarrar! A arma dele é a sua fragilidade…")
            elif goleiro_atual == "Gabriel Vasconcelos":
                pontos_ganhos = 2 * meta_sessao
                print("HAHAHA! Eu pedi um desafio, não uma barra sem goleiro…")
            else:
                if habilidade_inicial_luva > habilidade_goleiro:
                    pontos_ganhos = habilidade_inicial_luva - habilidade_goleiro
                else:
                    pontos_ganhos = 0

            if foi_gol:
                print("RECEBA! GOLAÇO! É O MELHOR DO MUNDO!")
            else:
                print("A jornada ainda não acabou!")
        else:
            pontos_ganhos = 0
            print("A jornada ainda não acabou!")

    if (habilidade_inicial_luva + pontos_ganhos) <= 100:
        if pontos_ganhos >= meta_sessao:
            print(f"VAMO! PARTIDA {num_partida} DE {total_partidas}!")
        else:
            print("Dá pra recuperar depois! Vamo seguindo!")

    habilidade_inicial_luva += pontos_ganhos
    num_sessoes_treino -= 1
    num_partida += 1
    indice_lista += 2

# Resultado final:
# Se Luva passou de 100 de habilidade
if habilidade_inicial_luva > 100:
    print("NÃO TEM JEITO! EU SEMPRE SOUBE QUE IA SER O MELHOR DO MUNDO! RECEBA!")
elif habilidade_inicial_luva == 100:
    print(
        "O trono do futebol hoje tem dois reis. Eu e Pelé! Não podia estar com alguém melhor!"
    )
else:
    print("Ano que vem tem InterCIn de novo! É só eu treinar mais…")
