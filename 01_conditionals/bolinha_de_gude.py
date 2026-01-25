# SE ACERTAR, PEGA BOLINHA DOS OUTROS E VAI PRO FIM DA FILA.
# SE ERRAR E AINDA TER BOLINHAS, VAI PARA O FIM DA FILA E NÃO GANHA NEM PERDE BOLINHAS.
# ELIMINADO SE NÃO POSSUIR MAIS BOLINHAS.
# ELIMINADO SE ERRAR TRÊS VEZES CONSECUTIVAS.
# NÃO HAREVÁ EMPATES.
# CONSIDERAR ORDEM ALFABÉTICA. André -> Bruno -> Clara -> André...

bolinhas_andre = int(input())
bolinhas_bruno = int(input())
bolinhas_clara = int(input())
num_participantes = 3
erros_consecutivos_andre = 0
erros_consecutivos_bruno = 0
erros_consecutivos_clara = 0
resultado_andre = ""
resultado_bruno = ""
resultado_clara = ""
andre_ativo = True
bruno_ativo = True
clara_ativo = True
turno = 0

while num_participantes > 1:
    if turno % 3 == 0:
        if andre_ativo:
            resultado_andre = input()
            if resultado_andre == "acertou":
                erros_consecutivos_andre = 0
                if bruno_ativo:
                    bolinhas_andre = bolinhas_andre + 1
                    bolinhas_bruno = bolinhas_bruno - 1
                if clara_ativo:
                    bolinhas_andre = bolinhas_andre + 1
                    bolinhas_clara = bolinhas_clara - 1
            else:
                erros_consecutivos_andre = erros_consecutivos_andre + 1

    elif turno % 3 == 1:
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

    if andre_ativo:
        if bolinhas_andre <= 0 or erros_consecutivos_andre >= 3:
            if bolinhas_andre <= 0:
                print("andre saiu do jogo")
                andre_ativo = False
                num_participantes = num_participantes - 1

            if erros_consecutivos_andre >= 3:
                print("andre perdeu feio")
                andre_ativo = False
                num_participantes = num_participantes - 1
    if bruno_ativo:
        if bolinhas_bruno <= 0 or erros_consecutivos_bruno >= 3:
            if bolinhas_bruno <= 0:
                print("bruno saiu do jogo")
                bruno_ativo = False
                num_participantes = num_participantes - 1
            if erros_consecutivos_bruno >= 3:
                print("bruno perdeu feio")
                bruno_ativo = False
                num_participantes = num_participantes - 1
    if clara_ativo:
        if bolinhas_clara <= 0 or erros_consecutivos_clara >= 3:
            if bolinhas_clara <= 0:
                print("clara saiu do jogo")
                clara_ativo = False
                num_participantes = num_participantes - 1
            if erros_consecutivos_clara >= 3:
                print("clara perdeu feio")
                clara_ativo = False
                num_participantes = num_participantes - 1

    turno = turno + 1

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
