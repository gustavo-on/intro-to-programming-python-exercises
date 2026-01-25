# FRASE DE ENTRADA
print("Vai começar o esconde-esconde UFPE 2025!")

buscador_1 = input()
buscador_2 = input()
buscador_3 = input()
pontuacao_1 = 0
pontuacao_2 = 0
pontuacao_3 = 0

# Ordem: CFCH → CTG → CIN
achou_ou_fim = ""
predio = 1
if predio == 1:
    print(f"\nProntos ou não, lá vai {buscador_1}.")
    print(f"Agora {buscador_1} procurará no CFCH.")
    while achou_ou_fim != "Fim da busca nesse prédio.":
        achou_ou_fim = input()
        if achou_ou_fim == "Achou uma pessoa!":
            print(f"{buscador_1} achou uma pessoa!")
            pontuacao_1 = pontuacao_1 + 1
    print(f"Agora {buscador_1} procurará no CTG.")
    achou_ou_fim = ""
    while achou_ou_fim != "Fim da busca nesse prédio.":
        achou_ou_fim = input()
        if achou_ou_fim == "Achou uma pessoa!":
            print(f"{buscador_1} achou uma pessoa!")
            pontuacao_1 = pontuacao_1 + 1
    print(f"Agora {buscador_1} procurará no CIN.")
    achou_ou_fim = ""
    while achou_ou_fim != "Fim da busca nesse prédio.":
        achou_ou_fim = input()
        if achou_ou_fim == "Achou uma pessoa!":
            print(f"{buscador_1} achou uma pessoa!")
            pontuacao_1 = pontuacao_1 + 1
    predio = predio + 1


achou_ou_fim = ""
if predio == 2:
    print(f"\nProntos ou não, lá vai {buscador_2}.")
    print(f"Agora {buscador_2} procurará no CFCH.")
    while achou_ou_fim != "Fim da busca nesse prédio.":
        achou_ou_fim = input()
        if achou_ou_fim == "Achou uma pessoa!":
            print(f"{buscador_2} achou uma pessoa!")
            pontuacao_2 = pontuacao_2 + 1
    print(f"Agora {buscador_2} procurará no CTG.")
    achou_ou_fim = ""
    while achou_ou_fim != "Fim da busca nesse prédio.":
        achou_ou_fim = input()
        if achou_ou_fim == "Achou uma pessoa!":
            print(f"{buscador_2} achou uma pessoa!")
            pontuacao_2 = pontuacao_2 + 1
    print(f"Agora {buscador_2} procurará no CIN.")
    achou_ou_fim = ""
    while achou_ou_fim != "Fim da busca nesse prédio.":
        achou_ou_fim = input()
        if achou_ou_fim == "Achou uma pessoa!":
            print(f"{buscador_2} achou uma pessoa!")
            pontuacao_2 = pontuacao_2 + 1
    predio = predio + 1

achou_ou_fim = ""
if predio == 3:
    print(f"\nProntos ou não, lá vai {buscador_3}.")
    print(f"Agora {buscador_3} procurará no CFCH.")
    while achou_ou_fim != "Fim da busca nesse prédio.":
        achou_ou_fim = input()
        if achou_ou_fim == "Achou uma pessoa!":
            print(f"{buscador_3} achou uma pessoa!")
            pontuacao_3 = pontuacao_3 + 1

    print(f"Agora {buscador_3} procurará no CTG.")
    achou_ou_fim = ""
    while achou_ou_fim != "Fim da busca nesse prédio.":
        achou_ou_fim = input()
        if achou_ou_fim == "Achou uma pessoa!":
            print(f"{buscador_3} achou uma pessoa!")
            pontuacao_3 = pontuacao_3 + 1

    print(f"Agora {buscador_3} procurará no CIN.")
    achou_ou_fim = ""
    while achou_ou_fim != "Fim da busca nesse prédio.":
        achou_ou_fim = input()
        if achou_ou_fim == "Achou uma pessoa!":
            print(f"{buscador_3} achou uma pessoa!")
            pontuacao_3 = pontuacao_3 + 1

if pontuacao_1 == 0 and pontuacao_2 == 0 and pontuacao_3 == 0:
    print("\nNinguém foi encontrado, nenhum dos buscadores ganhou a disputa.")

else:
    campeao = ""
    if pontuacao_1 > pontuacao_2 and pontuacao_1 > pontuacao_3:
        campeao = buscador_1
    elif pontuacao_2 > pontuacao_1 and pontuacao_2 > pontuacao_3:
        campeao = buscador_2
    else:
        campeao = buscador_3

    print(f"\n{campeao} é o(a) melhor no esconde-esconde da UFPE!")
