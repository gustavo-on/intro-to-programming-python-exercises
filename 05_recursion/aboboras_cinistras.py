def buscar_caminho(
    mapa, linha_atual, coluna_atual, passos_atuais, n, menores_passos, tempo_limite
):  # Função recursiva para buscar o caminho mais curto
    # Casos base
    # Se o tempo limite já foi excedido...
    if passos_atuais > tempo_limite:
        return 9999999999
    # Se a posição atual estiver fora do mapa...
    if linha_atual < 0 or linha_atual >= n or coluna_atual < 0 or coluna_atual >= n:
        return 9999999999  # Retorna um valor muito grande para indicar que o caminho não é válido
    # Se a posição atual for uma parede ou um caminho já visitado...
    if mapa[linha_atual][coluna_atual] == "A" or mapa[linha_atual][coluna_atual] == ".":
        return 9999999999  # Retorna um valor muito grande para indicar que o caminho não é válido
    # Se já chegou nesta célula antes com menos (ou mesmos) passos, não precisa continuar
    if passos_atuais >= menores_passos[linha_atual][coluna_atual]:
        return 9999999999
    menores_passos[linha_atual][coluna_atual] = passos_atuais
    # Se a posição atual for a saída...
    if mapa[linha_atual][coluna_atual] == "S":
        return passos_atuais  # Retorna o número de passos até a saída

    caractere_original = mapa[linha_atual][
        coluna_atual
    ]  # Armazena o caractere original da posição atual
    mapa[linha_atual][coluna_atual] = "."  # Marca a posição atual como visitada
    # Busca o caminho mais curto em todas as direções
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
    mapa[linha_atual][
        coluna_atual
    ] = caractere_original  # Restaura o caractere original da posição atual
    return min(
        resultado_cima, resultado_baixo, resultado_esquerda, resultado_direita
    )  # Retorna o menor número de passos entre as direções


# Input
horario = input()  # Horário que vai estar marcando no relógio de Byte
horas, minutos = horario.split(":")  # Separa as horas dos minutos
minutos = int(minutos)  # Converte os minutos para int
tempo_restante = (
    60 - minutos
)  # Calcula o tempo restante para as abóboras acordarem (tempo até meia noite)

n = int(input())  # Tamanho do mapa (n x n)
mapa = []  # Lista vazia para armazenar o mapa
linha_inicial, coluna_inicial = -1, -1  # Posição inicial de Byte
for i in range(n):  # Para cada linha do mapa...
    linha = input()  # Lê a linha do mapa
    linha_lista = list(linha)  # Converte a linha para uma lista de caracteres
    mapa.append(linha_lista)  # Adiciona a lista de caracteres ao mapa
    for j in range(n):  # Para cada coluna da linha...
        if linha_lista[j] == "B":  # Se o caractere for "B" (posição inicial de Byte)
            linha_inicial, coluna_inicial = i, j  # Atualiza a posição inicial de Byte

menores_passos = []  # Lista vazia para armazenar a memória de passos
for i in range(n):  # Para cada linha do mapa...
    linha_memoria = []  # Lista vazia para armazenar a linha da memória
    for j in range(n):  # Para cada coluna da linha...
        linha_memoria.append(
            9999999999
        )  # Adiciona um valor muito grande para indicar que a posição ainda não foi visitada
    menores_passos.append(
        linha_memoria
    )  # Adiciona a linha da memória à memória de passos

# Output
print(
    f"O relógio marca 23 horas e {minutos} minuto(s)! Byte tem apenas {tempo_restante} minuto(s) para escapar!"
)
passos_necessarios = buscar_caminho(
    mapa, linha_inicial, coluna_inicial, 0, n, menores_passos, tempo_restante
)
# Caso Byte consiga sair a tempo do labirinto...
if passos_necessarios <= tempo_restante:
    print(
        f"CONSEGUIMOS!! Byte precisou de {passos_necessarios} minuto(s) para conseguir escapar!"
    )
    # Caso Byte consiga sair a tempo do labirinto com mais 10 minutos de folga...
    if tempo_restante - passos_necessarios > 10:
        print(
            f"Abóboras CInistras que nada! Byte mostrou quem é que manda e conseguiu sair faltando {tempo_restante - passos_necessarios} minutos para elas acordarem"
        )
    # Caso Byte consiga sair com 10 minutos de folga ou menos...
    else:
        print(
            "Ufa! Essa foi por pouco! Mas com ajuda dos alunos de IP essas abóboras nem pareciam tão sinistras assim."
        )
# Caso Byte não consiga sair a tempo do labirinto...
else:
    print(
        "NÃÃÃÃO! Tudo isso por causa de um docinho! Você estará para sempre conosco, Byte!"
    )
