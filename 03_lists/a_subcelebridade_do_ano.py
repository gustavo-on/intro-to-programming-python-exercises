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
# Entrada dos Números e Cálculo da Pontuação
for i in range(2):
    numeros = [int(num) for num in input().split()]
    numeros_ordenados = sorted(numeros)
    linha_1 = numeros_ordenados[7:10]
    linha_2 = numeros_ordenados[0:3]
    restantes = numeros_ordenados[3:6]
    linha_3 = [n + 1 for n in restantes]
    desempate = numeros_ordenados[6]
    matriz = [linha_1, linha_2, linha_3]

    # Calcular o determinante da matriz:
    termo1 = matriz[0][0] * (matriz[1][1] * matriz[2][2] - matriz[1][2] * matriz[2][1])
    termo2 = matriz[0][1] * (matriz[1][0] * matriz[2][2] - matriz[1][2] * matriz[2][0])
    termo3 = matriz[0][2] * (matriz[1][0] * matriz[2][1] - matriz[1][1] * matriz[2][0])
    pontuacao = termo1 - termo2 + termo3

    # Salvando e imprimindo resultados parciais
    pontuacoes.append(pontuacao)
    numeros_desempate.append(desempate)
    print(f"{matriz[0][0]} {matriz[0][1]} {matriz[0][2]}")
    print(f"{matriz[1][0]} {matriz[1][1]} {matriz[1][2]}")
    print(f"{matriz[2][0]} {matriz[2][1]} {matriz[2][2]}")
    # Imprimindo a pontuação
    print(f"{participantes[i].capitalize()} está com pontuação {pontuacao} pontos.")

# Decidindo o Vencedor:
nome_ganhador = ""
if pontuacoes[0] > pontuacoes[1]:
    nome_ganhador = participantes[0]
elif pontuacoes[1] > pontuacoes[0]:
    nome_ganhador = participantes[1]
else:
    print("RODADA DESEMPATE!!")
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
        print(
            "Como isso é possível?? Os participantes empataram até na rodada desempate! EU DESISTO!!!"
        )

if nome_ganhador != "":
    print(
        f"Com talento duvidoso e esforço máximo, a vitória é de {nome_ganhador.capitalize()}!"
    )
