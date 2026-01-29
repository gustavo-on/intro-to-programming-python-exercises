"""
Questão: Esconde-Esconde na UFPE

Resumo:
O programa simula uma competição de esconde-esconde entre três buscadores.
Cada buscador percorre três prédios da UFPE (CFCH, CTG e CIN) e ganha pontos
sempre que encontra uma pessoa durante a busca.

Lógica principal:
- Os buscadores jogam em ordem fixa definida pela entrada.
- Em cada prédio, o buscador continua procurando até receber o comando
  de fim da busca naquele prédio.
- Cada ocorrência de "Achou uma pessoa!" soma um ponto ao buscador.
- Ao final, vence quem obtiver a maior pontuação.
- Caso todos terminem com zero pontos, não há vencedor.

Entradas:
- Nome dos três buscadores.
- Sequência de entradas indicando se encontrou alguém ou se terminou a busca
  em cada prédio, seguindo a ordem CFCH → CTG → CIN para cada buscador.

Saídas:
- Mensagens indicando o início do jogo e das buscas.
- Mensagens para cada pessoa encontrada.
- Mensagem final indicando o melhor buscador ou ausência de vencedor.
"""

# Mensagem inicial obrigatória
print("Vai começar o esconde-esconde UFPE 2025!")

# Leitura dos nomes dos buscadores
buscador_1 = input()
buscador_2 = input()
buscador_3 = input()

# Pontuação acumulada de cada buscador
pontuacao_1 = 0
pontuacao_2 = 0
pontuacao_3 = 0

# Variável usada para controlar o fluxo de leitura em cada prédio
achou_ou_fim = ""
predio = 1

# ---------- BUSCADOR 1 ----------
if predio == 1:
    print(f"\nProntos ou não, lá vai {buscador_1}.")
    print(f"Agora {buscador_1} procurará no CFCH.")

    # Enquanto não finalizar a busca no prédio, continua lendo entradas
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


# ---------- BUSCADOR 2 ----------
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


# ---------- BUSCADOR 3 ----------
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


# ---------- RESULTADO FINAL ----------
# Caso ninguém tenha pontuado
if pontuacao_1 == 0 and pontuacao_2 == 0 and pontuacao_3 == 0:
    print("\nNinguém foi encontrado, nenhum dos buscadores ganhou a disputa.")
else:
    # Comparação direta das pontuações para definir o campeão
    if pontuacao_1 > pontuacao_2 and pontuacao_1 > pontuacao_3:
        campeao = buscador_1
    elif pontuacao_2 > pontuacao_1 and pontuacao_2 > pontuacao_3:
        campeao = buscador_2
    else:
        campeao = buscador_3

    print(f"\n{campeao} é o(a) melhor no esconde-esconde da UFPE!")
