"""
Título: Conflagração

Resumo do problema:
Simula um combate tático entre Sam Porter Bridges e o inimigo Neil em uma matriz 6x6,
considerando movimentação, armas com alcance condicional, dano ambiental, ataques
automáticos do inimigo e mecânica de teletransporte baseada em distância de Chebyshev.

Lógica principal / critérios de aprovação:
- Sam e Neil iniciam com 100 de HP.
- O combate ocorre em uma matriz 6x6 com pisos livres, fogo e obstáculos.
- A cada 4 ações de Sam, Neil ataca automaticamente.
- O dano causado depende da arma equipada e da distância de Chebyshev.
- Após 3 acertos sofridos, Neil se teletransporta para a posição mais distante possível.
- Sam sofre dano contínuo ao permanecer em áreas incendiadas.
- Likes finais são calculados com base no dano recebido de Neil e exposição ao fogo.
- A missão termina com vitória se Neil for derrotado ou falha se Sam morrer.

Entradas:
- Matriz 6x6 representando o mapa inicial.
- Sequência de comandos: movimentação (W/A/S/D), troca de arma ou ação "Atirar".

Saídas:
- Mensagens narrativas e de feedback do combate.
- Impressão da matriz após teletransporte de Neil.
- Resultado final da missão com cálculo de Likes ou mensagem de falha.
"""


# Função para calcular a distância de Chebyshev:
def distancia_chebyshev(linha_sam, coluna_sam, linha_neil, coluna_neil):
    # Cálculo das diferenças absolutas nas linhas
    diff_linha = abs(linha_sam - linha_neil)
    # Cálculo das diferenças absolutas nas colunas
    diff_coluna = abs(coluna_sam - coluna_neil)
    # Decisão: a distância de Chebyshev é definida pela maior diferença entre linha ou coluna
    return max(diff_linha, diff_coluna)


# Função para a ação de atirar de Sam:
def atirar_Sam(arma_atual, distancia, hp_neil):
    # Decisão: o dano depende da arma equipada e da distância calculada
    if arma_atual == "Espingarda":
        # Curto alcance é privilegiado pela arma
        if distancia <= 2:
            dano = 25
        else:
            dano = 0
    elif arma_atual == "Rifle":
        # Rifle tem pico de eficiência em distância média
        if distancia == 3:
            dano = 15
        else:
            dano = 5
    elif arma_atual == "Metralhadora":
        # Metralhadora é otimizada para longas distâncias
        if distancia >= 4:
            dano = 15
        else:
            dano = 0
    else:
        dano = 0

    # Cálculo: redução direta do HP de Neil conforme o dano causado
    hp_neil -= dano
    return dano, hp_neil


# Função para a mecânica de teletransporte de Neil:
def teletransporte_neil(
    matriz_combate_6x6,
    linha_sam,
    coluna_sam,
    linha_neil_atual,
    coluna_neil_atual,
    piso_anterior_neil,
):
    distancia_maxima = -1
    nova_linha = -1
    nova_coluna = -1

    # Busca exaustiva pela posição mais distante possível de Sam
    for i in range(6):
        for j in range(6):
            # Decisão: Neil não pode ocupar espaços intransponíveis
            if matriz_combate_6x6[i][j] != "I":
                distancia = distancia_chebyshev(linha_sam, coluna_sam, i, j)
                # Decisão: usa >= para garantir escolha do último espaço em caso de empate
                if distancia >= distancia_maxima:
                    distancia_maxima = distancia
                    nova_linha = i
                    nova_coluna = j

    # Atualiza a posição anterior de Neil restaurando o piso original
    matriz_combate_6x6[linha_neil_atual][coluna_neil_atual] = piso_anterior_neil
    # Armazena o piso onde Neil irá se posicionar
    novo_piso_neil = matriz_combate_6x6[nova_linha][nova_coluna]
    # Atualiza a nova posição de Neil
    matriz_combate_6x6[nova_linha][nova_coluna] = "N"

    # Impressão obrigatória da matriz após teletransporte
    for i in range(6):
        for j in range(6):
            if j == 5:
                print(matriz_combate_6x6[i][j], end="")
            else:
                print(matriz_combate_6x6[i][j], end=" ")
        print()

    return nova_linha, nova_coluna, novo_piso_neil


print("Sam: Mas que lugar é esse aqui?")
print("Dollman: WASD... Num exclusivo de PS5? Ah, fala sério!")
print()

# Inicialização do estado do combate
hp_sam = 100
hp_neil = 100
arma_atual = "Rifle"
acoes_sam = 0
hits_neil = 0
dano_neil_total = 0
hits_fogo_total = 0
aviso_40hp_dado = False

coluna_sam = linha_sam = coluna_neil = linha_neil = 0
matriz_combate_6x6 = []

# Leitura da matriz inicial
for i in range(6):
    linha = input().split()
    matriz_combate_6x6.append(linha)

# Localização inicial de Sam e Neil
for i in range(6):
    for j in range(6):
        if matriz_combate_6x6[i][j] == "S":
            linha_sam = i
            coluna_sam = j
        if matriz_combate_6x6[i][j] == "N":
            linha_neil = i
            coluna_neil = j

piso_sam = "P"
piso_neil = "P"

# Loop principal do combate
while hp_sam > 0 and hp_neil > 0:
    entrada = input()

    # Decisão: comando de movimentação
    if entrada in ["W", "A", "S", "D"]:
        acoes_sam += 1
        nova_linha, nova_coluna = linha_sam, coluna_sam

        if entrada == "W":
            nova_linha -= 1
        elif entrada == "A":
            nova_coluna -= 1
        elif entrada == "S":
            nova_linha += 1
        elif entrada == "D":
            nova_coluna += 1

        # Decisão: valida limites da matriz e obstáculos
        if (
            0 <= nova_linha < 6
            and 0 <= nova_coluna < 6
            and matriz_combate_6x6[nova_linha][nova_coluna] != "I"
        ):
            matriz_combate_6x6[linha_sam][coluna_sam] = piso_sam
            piso_sam_novo = matriz_combate_6x6[nova_linha][nova_coluna]
            matriz_combate_6x6[nova_linha][nova_coluna] = "S"
            linha_sam, coluna_sam = nova_linha, nova_coluna
            piso_sam = piso_sam_novo

    # Decisão: troca de arma
    elif entrada in ["Espingarda", "Rifle", "Metralhadora"]:
        acoes_sam += 1
        arma_atual = entrada
        print(f"Arma trocada para {arma_atual}.")

    # Decisão: ação de ataque
    elif entrada == "Atirar":
        acoes_sam += 1
        distancia = distancia_chebyshev(linha_sam, coluna_sam, linha_neil, coluna_neil)
        dano, hp_neil = atirar_Sam(arma_atual, distancia, hp_neil)
        if dano > 0:
            hits_neil += 1

    # Cálculo: dano ambiental por fogo
    if hp_sam > 0 and hp_neil > 0 and piso_sam == "F":
        hp_sam -= 5
        hits_fogo_total += 1

    # Decisão: ataque automático de Neil após 4 ações de Sam
    if hp_sam > 0 and hp_neil > 0 and acoes_sam == 4:
        hp_sam -= 15
        dano_neil_total += 15
        print(">>> Você recebe um disparo de Neil! <<<")
        acoes_sam = 0

    # Decisão: aviso único ao atingir HP crítico
    if hp_sam > 0 and hp_neil > 0 and hp_sam <= 40 and not aviso_40hp_dado:
        print(
            "Dollman: A Fragile comeu todos os criptobiontes da DHV Magalhães... "
            "Se curar não é uma opção. Tome cuidado, Sam."
        )
        aviso_40hp_dado = True

    # Decisão: teletransporte após 3 acertos em Neil
    if hp_sam > 0 and hp_neil > 0 and hits_neil == 3:
        linha_neil, coluna_neil, piso_neil = teletransporte_neil(
            matriz_combate_6x6,
            linha_sam,
            coluna_sam,
            linha_neil,
            coluna_neil,
            piso_neil,
        )
        hits_neil = 0


# Decisão final: vitória ou falha
if hp_neil <= 0:
    # Cálculo final dos Likes com penalizações por dano e fogo
    likes = 1000 - (dano_neil_total * 8) - (hits_fogo_total * 10)
    print()
    print("MISSÃO COMPLETA! - Investigue a Anomalia")
    print("========================================")
    print(f"Likes recebidos: 👍 {likes}")
else:
    print()
    print("MISSÃO FALHOU")
    print("==============")
    print("Sam foi derrotado.")
    print("[Sua alma vaga pela Emenda, buscando reencontrar seu corpo perdido...]")
