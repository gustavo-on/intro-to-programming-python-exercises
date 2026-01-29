"""
Questão: Bolinha de Gude

Resumo:
O programa simula uma brincadeira de bolinha de gude entre três jogadores
(André, Bruno e Clara), seguindo uma ordem fixa e circular de jogadas.
Cada jogador tenta acertar um buraco, podendo ganhar bolinhas dos outros
ou ser eliminado conforme as regras.

Lógica principal:
- Os jogadores jogam em ordem alfabética (André → Bruno → Clara).
- Se o jogador acertar, ganha uma bolinha de cada jogador ativo restante.
- Se errar, não ganha nem perde bolinhas.
- Um jogador é eliminado se ficar sem bolinhas ou errar três vezes consecutivas.
- O jogo termina quando resta apenas um jogador ativo, que é o vencedor.

Entradas:
- Quantidade inicial de bolinhas de André, Bruno e Clara.
- Sequência de resultados das jogadas ("acertou" ou "errou"), respeitando a ordem.

Saídas:
- Mensagens indicando eliminação por falta de bolinhas ou por erros consecutivos.
- Mensagem do jogador vencedor.
- Quantidade final de bolinhas de cada jogador.
"""

bolinhas_andre = int(input())
bolinhas_bruno = int(input())
bolinhas_clara = int(input())

num_participantes = 3

# Contadores de erros consecutivos de cada jogador
erros_consecutivos_andre = 0
erros_consecutivos_bruno = 0
erros_consecutivos_clara = 0

# Flags que indicam se o jogador ainda está ativo no jogo
andre_ativo = True
bruno_ativo = True
clara_ativo = True

# Variável que controla a ordem circular das jogadas
turno = 0

while num_participantes > 1:
    if turno % 3 == 0:
        # Turno do André
        if andre_ativo:
            resultado_andre = input()
            if resultado_andre == "acertou":
                erros_consecutivos_andre = 0  # acerto zera a sequência de erros
                if bruno_ativo:
                    bolinhas_andre = bolinhas_andre + 1
                    bolinhas_bruno = bolinhas_bruno - 1
                if clara_ativo:
                    bolinhas_andre = bolinhas_andre + 1
                    bolinhas_clara = bolinhas_clara - 1
            else:
                erros_consecutivos_andre = erros_consecutivos_andre + 1

    elif turno % 3 == 1:
        # Turno do Bruno
        if bruno_ativo:
            resultado_bruno = input()
            if resultado_bruno == "acertou":
                erros_consecutivos_bruno = 0
                if andre_ativo:
                    bolinhas_bruno = bolinhas_bruno + 1
                    bolinhas_andre = bolinhas_andre - 1
                if clara_ativo:
                    bolinhas_bruno = bolinhas_bruno + 1
                    bolinhas_clara = bolinhas_clara - 1
            else:
                erros_consecutivos_bruno = erros_consecutivos_bruno + 1

    else:
        # Turno da Clara
        if clara_ativo:
            resultado_clara = input()
            if resultado_clara == "acertou":
                erros_consecutivos_clara = 0
                if andre_ativo:
                    bolinhas_clara = bolinhas_clara + 1
                    bolinhas_andre = bolinhas_andre - 1
                if bruno_ativo:
                    bolinhas_clara = bolinhas_clara + 1
                    bolinhas_bruno = bolinhas_bruno - 1
            else:
                erros_consecutivos_clara = erros_consecutivos_clara + 1

    # Verificação de eliminação do André
    if andre_ativo:
        if bolinhas_andre <= 0 or erros_consecutivos_andre >= 3:
            if bolinhas_andre <= 0:
                print("andre saiu do jogo")
            if erros_consecutivos_andre >= 3:
                print("andre perdeu feio")
            andre_ativo = False
            num_participantes = num_participantes - 1

    # Verificação de eliminação do Bruno
    if bruno_ativo:
        if bolinhas_bruno <= 0 or erros_consecutivos_bruno >= 3:
            if bolinhas_bruno <= 0:
                print("bruno saiu do jogo")
            if erros_consecutivos_bruno >= 3:
                print("bruno perdeu feio")
            bruno_ativo = False
            num_participantes = num_participantes - 1

    # Verificação de eliminação da Clara
    if clara_ativo:
        if bolinhas_clara <= 0 or erros_consecutivos_clara >= 3:
            if bolinhas_clara <= 0:
                print("clara saiu do jogo")
            if erros_consecutivos_clara >= 3:
                print("clara perdeu feio")
            clara_ativo = False
            num_participantes = num_participantes - 1

    turno = turno + 1  # avança para o próximo jogador na ordem circular

# Determinação do vencedor final
if clara_ativo:
    vencedor = "clara"
elif andre_ativo:
    vencedor = "andre"
else:
    vencedor = "bruno"

print(f"{vencedor} ganhou")
print(
    f"a quantidade final de bolas foi:\nandre: {bolinhas_andre}\nbruno: {bolinhas_bruno}\nclara: {bolinhas_clara}"
)
