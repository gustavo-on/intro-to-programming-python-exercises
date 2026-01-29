"""
Título: A subcelebridade do ano

Resumo do problema:
O programa simula uma prova entre dois participantes do Big Sub Brasil.
Cada participante recebe uma sequência de números, a partir da qual é construída
uma matriz 3x3. O determinante dessa matriz define a pontuação do jogador, e aquele
com maior pontuação vence a disputa.

Regras de aprovação / Lógica principal:
- Os participantes competem em dupla.
- Para cada participante, são geradas três linhas:
  1) Os três maiores números da entrada.
  2) Os três menores números da entrada.
  3) Os três números intermediários incrementados em 1.
- Essas linhas formam uma matriz 3x3 cujo determinante é a pontuação do jogador.
- O jogador com maior determinante vence.
- Em caso de empate, um número reservado da entrada é usado como critério de desempate.
- Persistindo o empate, não há vencedor.

Entradas:
- Uma string contendo dois nomes separados por vírgula.
- Para cada participante, uma linha com 10 números inteiros distintos.

Saídas:
- Mensagens de boas-vindas e anúncio da disputa.
- Impressão da matriz de cada participante e sua pontuação.
- Anúncio do vencedor, incluindo lógica de desempate quando necessário.
"""

# Mensagem de Boas-Vindas e Entrada dos Nomes
print(
    "Sejam bem-vindos à Big Sub Brasil, onde a fama é temporária, os barracos são eternos, e só um vai conquistar o título de maior subcelebridade do país!"
)

participantes = input().split(", ")
participante_1 = participantes[0].capitalize()
participante_2 = participantes[1].capitalize()
print(f"{participante_1} e {participante_2} disputarão entre si.")

pontuacoes = []
numeros_desempate = []

# Entrada dos números e cálculo da pontuação de cada participante
for i in range(2):
    numeros = [int(num) for num in input().split()]
    numeros_ordenados = sorted(numeros)

    # Seleção dos três maiores valores para a primeira linha da matriz
    linha_1 = numeros_ordenados[7:10]

    # Seleção dos três menores valores para a segunda linha da matriz
    linha_2 = numeros_ordenados[0:3]

    # Os valores intermediários são incrementados para criar progressão consecutiva
    restantes = numeros_ordenados[3:6]
    linha_3 = [n + 1 for n in restantes]

    # O número restante é reservado exclusivamente para o critério de desempate
    desempate = numeros_ordenados[6]

    matriz = [linha_1, linha_2, linha_3]

    # Cálculo do determinante da matriz 3x3 como critério de pontuação
    termo1 = matriz[0][0] * (matriz[1][1] * matriz[2][2] - matriz[1][2] * matriz[2][1])
    termo2 = matriz[0][1] * (matriz[1][0] * matriz[2][2] - matriz[1][2] * matriz[2][0])
    termo3 = matriz[0][2] * (matriz[1][0] * matriz[2][1] - matriz[1][1] * matriz[2][0])
    pontuacao = termo1 - termo2 + termo3

    # Armazenamento da pontuação e do número de desempate para comparação posterior
    pontuacoes.append(pontuacao)
    numeros_desempate.append(desempate)

    # Impressão da matriz gerada
    print(f"{matriz[0][0]} {matriz[0][1]} {matriz[0][2]}")
    print(f"{matriz[1][0]} {matriz[1][1]} {matriz[1][2]}")
    print(f"{matriz[2][0]} {matriz[2][1]} {matriz[2][2]}")

    # Exibição da pontuação associada ao participante
    print(f"{participantes[i].capitalize()} está com pontuação {pontuacao} pontos.")

# Decisão do vencedor com base na pontuação principal
nome_ganhador = ""
if pontuacoes[0] > pontuacoes[1]:
    nome_ganhador = participantes[0]
elif pontuacoes[1] > pontuacoes[0]:
    nome_ganhador = participantes[1]
else:
    # Empate na pontuação principal ativa a rodada de desempate
    print("RODADA DESEMPATE!!")

    # Comparação direta do número reservado para desempate
    if numeros_desempate[0] > numeros_desempate[1]:
        nome_ganhador = participantes[0]
        nome_perdedor = participantes[1]
        print(
            f"Contra todas as expectativas (inclusive as nossas), {nome_ganhador.capitalize()} venceu a rodada!"
        )
        print(
            f"Seu momento de brilhar virou eclipse {nome_perdedor.capitalize()}. Melhor sorte no próximo flop!"
        )
    elif numeros_desempate[1] > numeros_desempate[0]:
        nome_ganhador = participantes[1]
        nome_perdedor = participantes[0]
        print(
            f"Contra todas as expectativas (inclusive as nossas), {nome_ganhador.capitalize()} venceu a rodada!"
        )
        print(
            f"Seu momento de brilhar virou eclipse {nome_perdedor.capitalize()}. Melhor sorte no próximo flop!"
        )
    else:
        # Caso extremo: empate total, inclusive no critério de desempate
        print(
            "Como isso é possível?? Os participantes empataram até na rodada desempate! EU DESISTO!!!"
        )

# Impressão final apenas se houver vencedor definido
if nome_ganhador != "":
    print(
        f"Com talento duvidoso e esforço máximo, a vitória é de {nome_ganhador.capitalize()}!"
    )
