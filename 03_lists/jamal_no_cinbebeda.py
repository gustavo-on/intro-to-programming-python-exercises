"""
Título: Jamal no CInbebeda

Resumo do problema:
O programa simula a avaliação de uma sequência de passos de dança executados por monitores,
comparando suas movimentações com um passinho fixo definido por Jamal. A partir das notas
iniciais atribuídas, o sistema identifica o monitor com pior desempenho, valida suas tentativas
de execução e decide o desfecho com base no número de erros cometidos.

Lógica principal / Regras de aprovação:
- Apenas quatro monitores específicos são aceitos, sem repetições.
- O monitor com a menor nota é selecionado para tentar reproduzir o passinho de Jamal.
- A comparação é feita pela igualdade exata das strings de comando, não pela matriz visual.
- O desempenho é avaliado pelo número de erros:
    * 0 erros: aprovação direta
    * 1 erro: direito a uma segunda tentativa
    * ≥ 2 erros: reprovação com mensagens específicas
- Apenas se houver sucesso final o convite para o show é oferecido.

Entradas:
- String com nomes dos monitores e suas notas (intercalados).
- String com 7 movimentações no formato E/D + linha + coluna.
- Opcionalmente, uma segunda tentativa de movimentações.
- Resposta ao convite ("Sim" ou "Não").

Saídas:
- Mensagens narrativas conforme o progresso da execução.
- Impressão das matrizes de Jamal e do monitor.
- Mensagens finais indicando sucesso, falha ou recusa do convite.
"""

print("Finalmente Jamal chega no CInbebeda, pronto pra causar, quando de repente…")
print('Jamal - "Que danado é isso?"')

monitores_validos = [
    "Júnior",
    "Henrique",
    "Miguel",
    "Guilherme",
]

nomes_corretos = False
while not nomes_corretos:
    entrada = input()
    lista_entrada = entrada.split(", ")

    nomes_entradas = lista_entrada[0::2]
    notas = lista_entrada[1::2]

    validacao_ok = True
    for nome in nomes_entradas:
        # Decisão: garante que apenas monitores permitidos e sem duplicação participem
        if nome not in monitores_validos:
            validacao_ok = False
        if nomes_entradas.count(nome) > 1:
            validacao_ok = False

    if validacao_ok:
        nomes_corretos = True
    else:
        print("Insira nomes válidos.")

# Conversão necessária para permitir comparações numéricas e cálculo de mínimo
notas_int = [int(n) for n in notas]

for i in range(len(notas_int)):
    # Decisão: identifica monitores com nota máxima para mensagem especial
    if notas_int[i] == 10:
        print(
            f"O monitor {nomes_entradas[i]} é diferenciado! Teve a aprovação do próprio Jamal."
        )

# Cálculo: identifica a menor nota para selecionar o monitor mais necessitado
menor_nota = min(notas_int)
indice_menor_nota = notas_int.index(menor_nota)
monitor_menor_nota = nomes_entradas[indice_menor_nota]

print(
    f"Jamal avaliou a situação dos monitores e viu que {monitor_menor_nota} é o mais necessitado."
)

# Matrizes fixas representam o passinho correto de Jamal
jamal_matriz_0 = [[".", ".", "."], [".", ".", "."], ["E", ".", "D"]]
jamal_matriz_1 = [[".", "1", "."], [".", ".", "."], ["E", ".", "."]]
jamal_matriz_2 = [[".", ".", "."], [".", ".", "."], ["E", ".", "2"]]
jamal_matriz_3 = [[".", "3", "."], [".", ".", "."], [".", ".", "D"]]
jamal_matriz_4 = [[".", ".", "."], [".", ".", "."], ["4", ".", "D"]]
jamal_matriz_5 = [[".", "5", "."], [".", ".", "."], ["E", ".", "."]]
jamal_matriz_6 = [[".", "D", "."], [".", ".", "."], ["6", ".", "."]]
jamal_matriz_7 = [[".", "7", "."], [".", ".", "."], ["E", ".", "."]]

jamal_matrizes = [
    jamal_matriz_0,
    jamal_matriz_1,
    jamal_matriz_2,
    jamal_matriz_3,
    jamal_matriz_4,
    jamal_matriz_5,
    jamal_matriz_6,
    jamal_matriz_7,
]

print('Jamal - "Vou ensinar apenas uma vez, então preste atenção."')

for i in range(len(jamal_matrizes)):
    print()
    print(f"Jamal - Movimentação {i}:")
    matriz_atual = jamal_matrizes[i]
    for linha in matriz_atual:
        print(" ".join(linha))

print()

movimento_valido = False
imprimiu_invalido_alguma_vez = False

while not movimento_valido:
    monitor_moves = input().split(", ")
    invalido_encontrado = False

    # Decisão: valida quantidade exata de movimentos exigida pelo problema
    if len(monitor_moves) != 7:
        invalido_encontrado = True
    else:
        for move in monitor_moves:
            # Decisões: validam formato e limites da matriz 3x3
            if len(move) != 3:
                invalido_encontrado = True
            if move[0] not in ["E", "D"]:
                invalido_encontrado = True
            if move[1] not in ["1", "2", "3"]:
                invalido_encontrado = True
            if move[2] not in ["1", "2", "3"]:
                invalido_encontrado = True

    if invalido_encontrado:
        print("Movimento inválido! Por favor, insira outro.")
        imprimiu_invalido_alguma_vez = True
    else:
        movimento_valido = True

if imprimiu_invalido_alguma_vez:
    print()

# Passinho correto usado como referência para comparação direta
jamal_correto = ["D12", "D33", "E12", "E31", "D12", "E31", "D12"]

erros = 0
for i in range(7):
    # Cálculo: erro é contado quando o comando não coincide exatamente
    if monitor_moves[i] != jamal_correto[i]:
        erros += 1

print(f"{monitor_menor_nota} - Movimentação 0:")
for linha in jamal_matriz_0:
    print(" ".join(linha))

pos_e = [2, 0]
pos_d = [2, 2]

for i in range(7):
    matriz_passo = [[".", ".", "."], [".", ".", "."], [".", ".", "."]]
    move = monitor_moves[i]

    pe = move[0]
    linha = int(move[1]) - 1
    coluna = int(move[2]) - 1

    # Decisão: atualiza a matriz conforme o pé que se moveu
    if pe == "E":
        matriz_passo[linha][coluna] = str(i + 1)
        pos_e = [linha, coluna]
        matriz_passo[pos_d[0]][pos_d[1]] = "D"
    elif pe == "D":
        matriz_passo[linha][coluna] = str(i + 1)
        pos_d = [linha, coluna]
        matriz_passo[pos_e[0]][pos_e[1]] = "E"

    print()
    print(f"{monitor_menor_nota} - Movimentação {i+1}:")
    for linha in matriz_passo:
        print(" ".join(linha))

print()

sucesso = False

# Decisão: classificação do desempenho com base no número de erros
if erros == 0:
    sucesso = True
    if monitor_menor_nota == "Júnior":
        print(
            "Uma máquina! Depois de horas vendo o passinho no Instagram ele conseguiu pegar mais rápido."
        )
    elif monitor_menor_nota == "Henrique":
        print("O maldito talento ataca novamente! Tinha que ser o desenrolado.")
    elif monitor_menor_nota == "Miguel":
        print("O cara veio do interior pra mostrar como que se faz!")
    elif monitor_menor_nota == "Guilherme":
        print(
            "Ninguém nunca tinha visto ele dançar! Sabíamos que ele estava escondendo um dom."
        )

elif erros == 1:
    print("Foi quase! O monitor merece uma nova chance!")
    print()

    entrada_str_2 = input()
    monitor_moves_2 = entrada_str_2.split(", ")

    erros_2 = 0
    for i in range(7):
        if monitor_moves_2[i] != jamal_correto[i]:
            erros_2 += 1

    print(f"{monitor_menor_nota} - Movimentação 0:")
    for linha in jamal_matriz_0:
        print(" ".join(linha))

    pos_e = [2, 0]
    pos_d = [2, 2]

    for i in range(7):
        matriz_passo = [[".", ".", "."], [".", ".", "."], [".", ".", "."]]
        move = monitor_moves_2[i]

        pe = move[0]
        linha = int(move[1]) - 1
        coluna = int(move[2]) - 1

        if pe == "E":
            matriz_passo[linha][coluna] = str(i + 1)
            pos_e = [linha, coluna]
            matriz_passo[pos_d[0]][pos_d[1]] = "D"
        elif pe == "D":
            matriz_passo[linha][coluna] = str(i + 1)
            pos_d = [linha, coluna]
            matriz_passo[pos_e[0]][pos_e[1]] = "E"

        print()
        print(f"{monitor_menor_nota} - Movimentação {i+1}:")
        for linha in matriz_passo:
            print(" ".join(linha))

    print()

    if erros_2 == 0:
        sucesso = True
        print(
            f"Era isso! {monitor_menor_nota} só estava precisando de um empurrãozinho."
        )
    else:
        print(f"Nem com outra tentativa {monitor_menor_nota} conseguiu ajeitar isso.")

elif erros == 2:
    print(f"Melhor o monitor {monitor_menor_nota} deixar esse negócio de dança pra lá.")
elif erros == 3:
    print("Isso tá horrível!")
else:
    print(f"O monitor {monitor_menor_nota} foi expulso da festa por não saber dançar.")

if sucesso:
    print(
        'Jamal - "Vocês aprendem rápido! Quero que vocês dancem no meu próximo show!"'
    )
    resposta_convite = input()

    # Decisão: mensagem final depende da aceitação ou recusa do convite
    if resposta_convite == "Sim":
        print(
            f"Óbvio que o monitor {monitor_menor_nota} não perderia essa oportunidade por nada!"
        )
    elif resposta_convite == "Não":
        print(
            f"Infelizmente o monitor {monitor_menor_nota} jogou essa oportunidade fora. "
            "Todos sabem que lá na frente ele vai se arrepender disso."
        )
else:
    print(
        "Jamal desistiu de ensinar pra quem não aprende. Ele saiu em grande estilo, mandando o passinho e andando."
    )
