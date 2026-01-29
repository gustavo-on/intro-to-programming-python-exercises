"""
Questão: Campeonato Mundial de Cabo de Guerra!

Enunciado:
Simulação de um torneio entre Arthur e João.
O torneio consiste em N partidas (ímpar).
Cada partida consiste em várias rodadas até a resistência de um zerar.

Regras da Rodada (Input N):
1. Se N é Quadrado Perfeito: Arthur vence a rodada.
2. Se N é Primo: João vence a rodada.
3. Se N não é nenhum dos dois: Vence quem tiver maior Força bruta.

Mecânica:
- Vencedor da rodada: +1 Resistência.
- Perdedor da rodada: -1 Resistência.
- Fim da partida: Resistência de alguém chega a 0.
- Fim do torneio: Fim das N partidas OU um jogador atinge a maioria absoluta de vitórias.

Output:
- Mensagens de narrador passo a passo e placar final.
"""

print("Começa agora o treinamento para grande final mundial de cabo de guerra!")

# --- 1. CONFIGURAÇÃO INICIAL E VALIDAÇÃO ---

# Input de quantidade de partidas (Deve ser Ímpar)
qnt_partidas = int(input())
while qnt_partidas % 2 == 0:
    print("Não deverá haver empates! O número de partidas deverá ser ímpar.")
    qnt_partidas = int(input())

print(f"Eles batalharão em {qnt_partidas} longas partidas.")

# Inputs de Atributos
forca_arthur = int(input())
forca_joao = int(input())
resistencia_inicial = int(input())

# Define quem é o mais forte para o caso de desempate (else)
# Isso evita checar if/else a cada rodada desnecessariamente
if forca_arthur > forca_joao:
    mais_forte_nome = "Arthur"
    mais_fraco_nome = "João"
else:
    mais_forte_nome = "João"
    mais_fraco_nome = "Arthur"

# Contadores do Placar Geral
vitorias_arthur = 0
vitorias_joao = 0
partida_atual = 1

# Critério de "Melhor de N": Metade + 1 para vencer
numero_para_vencer = (qnt_partidas // 2) + 1

# --- 2. LOOP DO TORNEIO (PARTIDAS) ---
while partida_atual <= qnt_partidas:
    print(f"Começa a {partida_atual}ª partida!")
    print(f"Placar geral: {vitorias_arthur} X {vitorias_joao}")

    # Reseta a resistência para a nova partida
    res_arthur = resistencia_inicial
    res_joao = resistencia_inicial

    # --- 3. LOOP DA PARTIDA (RODADAS) ---
    # Roda enquanto ambos tiverem resistência
    while res_arthur > 0 and res_joao > 0:
        numero = int(input())

        # A. Verifica Quadrado Perfeito (Arthur)
        # Se a raiz quadrada inteira ao quadrado for igual ao número original
        raiz = int(numero**0.5)
        if raiz * raiz == numero:
            print("O número é um quadrado perfeito! Arthur consegue puxar mais forte.")
            res_arthur += 1
            res_joao -= 1

        else:
            # B. Verifica Primo (João)
            # Conta divisores de 1 até N
            divisores = 0
            for i in range(1, numero + 1):
                if numero % i == 0:
                    divisores += 1

            if (
                divisores == 2
            ):  # Número primo tem exatamente 2 divisores (1 e ele mesmo)
                print("O primo do primo é primo do primo? João puxa mais forte!")
                res_joao += 1
                res_arthur -= 1

            # C. Força Bruta (Nenhum dos dois)
            else:
                print(
                    f"{mais_forte_nome} é o mais forte! {mais_fraco_nome} não consegue segurar."
                )
                if mais_forte_nome == "Arthur":
                    res_arthur += 1
                    res_joao -= 1
                else:
                    res_joao += 1
                    res_arthur -= 1

    # --- FIM DA PARTIDA ---
    if res_arthur > 0:
        print("Arthur dá orgulho para Maceió e ganha a partida!")
        vitorias_arthur += 1
    else:
        print("João usa seus talentos de mangueboy e leva essa para casa!")
        vitorias_joao += 1

    # Verificação de Encerramento Antecipado (Chance de Virada)
    # Se alguém já atingiu a maioria absoluta, paramos o loop
    if vitorias_arthur == numero_para_vencer or vitorias_joao == numero_para_vencer:
        break

    partida_atual += 1

# --- 4. RESULTADO FINAL ---
print("\nAgora eles estão prontos para o mundial!")
print(f"Placar final: {vitorias_arthur} X {vitorias_joao}")

if vitorias_arthur > vitorias_joao:
    ganhador = "Arthur"
    perdedor = "João"
    vitorias_ganhador = vitorias_arthur
    vitorias_perdedor = vitorias_joao
else:
    ganhador = "João"
    perdedor = "Arthur"
    vitorias_ganhador = vitorias_joao
    vitorias_perdedor = vitorias_arthur

# Verifica se foi uma vitória invicta (perdedor zerado)
if vitorias_perdedor == 0:
    print(f"{perdedor} não teve chance! {ganhador} venceu todas as partidas.")
else:
    diferenca = vitorias_ganhador - vitorias_perdedor
    print(f"O ganhador foi {ganhador} com uma diferença de {diferenca} partidas.")
