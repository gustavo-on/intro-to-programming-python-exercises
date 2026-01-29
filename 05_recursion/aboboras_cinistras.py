"""
Título: Abóboras CInistras

Resumo do problema:
Determinar se Byte consegue escapar de um labirinto quadrado antes da meia-noite,
encontrando o menor caminho até a saída sem atravessar obstáculos, respeitando
o limite de tempo disponível.

Lógica principal / Regras:
- O labirinto é representado por uma matriz NxN.
- Byte pode se mover apenas em quatro direções (cima, baixo, esquerda, direita).
- Cada movimento consome exatamente 1 minuto.
- Abóboras e células já visitadas bloqueiam o caminho.
- A solução utiliza backtracking recursivo para buscar o menor caminho possível,
  interrompendo explorações que excedem o tempo limite ou caminhos já conhecidos como piores.

Entradas:
- Horário atual (HH:MM), sempre após 23:00.
- Inteiro N representando o tamanho do mapa.
- Matriz NxN contendo:
  '0' (livre), 'A' (abóbora), 'S' (saída), 'B' (posição inicial).

Saídas:
- Mensagens informando o tempo disponível.
- Resultado da tentativa de fuga conforme o número de passos necessários.
"""


def buscar_caminho(
    mapa, linha_atual, coluna_atual, passos_atuais, n, menores_passos, tempo_limite
):
    # Decisão: caminhos que excedem o tempo limite são descartados
    if passos_atuais > tempo_limite:
        return 9999999999

    # Decisão: impedir acesso fora dos limites do mapa
    if linha_atual < 0 or linha_atual >= n or coluna_atual < 0 or coluna_atual >= n:
        return 9999999999

    # Decisão: abóboras e posições já visitadas tornam o caminho inválido
    if mapa[linha_atual][coluna_atual] == "A" or mapa[linha_atual][coluna_atual] == ".":
        return 9999999999

    # Decisão: poda de busca — se já se chegou aqui com menos passos, não há ganho em continuar
    if passos_atuais >= menores_passos[linha_atual][coluna_atual]:
        return 9999999999

    # Registro do menor custo conhecido para esta célula
    menores_passos[linha_atual][coluna_atual] = passos_atuais

    # Decisão: alcançar a saída encerra o caminho com sucesso
    if mapa[linha_atual][coluna_atual] == "S":
        return passos_atuais

    caractere_original = mapa[linha_atual][coluna_atual]
    mapa[linha_atual][coluna_atual] = "."

    # Cálculo: exploração recursiva em todas as direções possíveis
    resultado_cima = buscar_caminho(
        mapa,
        linha_atual - 1,
        coluna_atual,
        passos_atuais + 1,
        n,
        menores_passos,
        tempo_limite,
    )
    resultado_baixo = buscar_caminho(
        mapa,
        linha_atual + 1,
        coluna_atual,
        passos_atuais + 1,
        n,
        menores_passos,
        tempo_limite,
    )
    resultado_esquerda = buscar_caminho(
        mapa,
        linha_atual,
        coluna_atual - 1,
        passos_atuais + 1,
        n,
        menores_passos,
        tempo_limite,
    )
    resultado_direita = buscar_caminho(
        mapa,
        linha_atual,
        coluna_atual + 1,
        passos_atuais + 1,
        n,
        menores_passos,
        tempo_limite,
    )

    mapa[linha_atual][coluna_atual] = caractere_original

    # Cálculo: escolha do menor caminho válido entre as possibilidades
    return min(resultado_cima, resultado_baixo, resultado_esquerda, resultado_direita)


# Entrada: horário atual
horario = input()
horas, minutos = horario.split(":")
minutos = int(minutos)

# Cálculo: tempo restante até meia-noite
tempo_restante = 60 - minutos

n = int(input())
mapa = []
linha_inicial, coluna_inicial = -1, -1

for i in range(n):
    linha = input()
    linha_lista = list(linha)
    mapa.append(linha_lista)

    for j in range(n):
        # Decisão: identificação da posição inicial de Byte
        if linha_lista[j] == "B":
            linha_inicial, coluna_inicial = i, j

menores_passos = []
for i in range(n):
    linha_memoria = []
    for j in range(n):
        # Inicialização com valor alto permite comparação de mínimos
        linha_memoria.append(9999999999)
    menores_passos.append(linha_memoria)

print(
    f"O relógio marca 23 horas e {minutos} minuto(s)! Byte tem apenas {tempo_restante} minuto(s) para escapar!"
)

passos_necessarios = buscar_caminho(
    mapa, linha_inicial, coluna_inicial, 0, n, menores_passos, tempo_restante
)

# Decisão: verificar se existe caminho viável dentro do tempo
if passos_necessarios <= tempo_restante:
    print(
        f"CONSEGUIMOS!! Byte precisou de {passos_necessarios} minuto(s) para conseguir escapar!"
    )

    # Decisão: classificação do sucesso conforme folga de tempo
    if tempo_restante - passos_necessarios > 10:
        print(
            f"Abóboras CInistras que nada! Byte mostrou quem é que manda e conseguiu sair faltando {tempo_restante - passos_necessarios} minutos para elas acordarem"
        )
    else:
        print(
            "Ufa! Essa foi por pouco! Mas com ajuda dos alunos de IP essas abóboras nem pareciam tão sinistras assim."
        )
else:
    print(
        "NÃÃÃÃO! Tudo isso por causa de um docinho! Você estará para sempre conosco, Byte!"
    )
