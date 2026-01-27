print("Finalmente Jamal chega no CInbebeda, pronto pra causar, quando de repente…")
print('Jamal - "Que danado é isso?"')

monitores_validos = [
    "Júnior",
    "Henrique",
    "Miguel",
    "Guilherme",
]  # Lista de monitores válidos
nomes_corretos = False  # Flag para controlar o loop de validação
while not nomes_corretos:  # Loop de validação
    entrada = input()  # Receber entrada
    lista_entrada = entrada.split(", ")  # Dividir entrada
    # Separar nomes e notas:
    nomes_entradas = lista_entrada[0::2]  # Nomes
    notas = lista_entrada[1::2]  # Notas
    # Validação:
    validacao_ok = True
    for nome in nomes_entradas:  # Loop para verificar se os nomes são válidos
        if nome not in monitores_validos:  # Se o nome não for válido
            validacao_ok = False  # Muda a flag para False
        if nomes_entradas.count(nome) > 1:  # Se houver nomes duplicados
            validacao_ok = False  # Muda a flag para False
    # Saída da Validação:
    if validacao_ok:  # Se a validação estiver ok
        nomes_corretos = True
    else:  # Se a validação não estiver ok
        print("Insira nomes válidos.")  # Imprime mensagem de erro
# Conversão de Notas:
notas_int = [int(n) for n in notas]

# Notas 10:
for i in range(len(notas_int)):
    if notas_int[i] == 10:  # Se a nota for 10
        print(
            f"O monitor {nomes_entradas[i]} é diferenciado! Teve a aprovação do próprio Jamal."
        )
# Encontrar menor nota:
menor_nota = min(notas_int)  # Encontra a menor nota
indice_menor_nota = notas_int.index(menor_nota)
monitor_menor_nota = nomes_entradas[indice_menor_nota]
# Imprimir saída:
print(
    f"Jamal avaliou a situação dos monitores e viu que {monitor_menor_nota} é o mais necessitado."
)

# Armazenar Matrizes:
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
# Imprimir Ensino:
print('Jamal - "Vou ensinar apenas uma vez, então preste atenção."')
for i in range(len(jamal_matrizes)):
    print()
    print(f"Jamal - Movimentação {i}:")
    # Imprimir a matriz formatada:
    matriz_atual = jamal_matrizes[i]
    for linha in matriz_atual:
        print(" ".join(linha))
print()

movimento_valido = False  # Flag para controlar o loop de validação
imprimiu_invalido_alguma_vez = False
while not movimento_valido:  # Loop de validação
    monitor_moves = input().split(", ")  # Receber entrada e dividir
    invalido_encontrado = False  # Flag para controlar a validação
    if len(monitor_moves) != 7:  # Se o número de movimentos for diferente de 7
        invalido_encontrado = True
    else:  # Se o número de movimentos for 7
        for move in monitor_moves:  # Para cada movimento
            if len(move) != 3:  # Se o movimento não tiver 3 caracteres
                invalido_encontrado = True
            if move[0] not in ["E", "D"]:  # Se o primeiro caractere não for E ou D
                invalido_encontrado = True
            if move[1] not in [
                "1",
                "2",
                "3",
            ]:  # Se o segundo caractere não for 1, 2 ou 3
                invalido_encontrado = True
            if move[2] not in [
                "1",
                "2",
                "3",
            ]:  # Se o terceiro caractere não for 1, 2 ou 3
                invalido_encontrado = True
    if invalido_encontrado:
        print("Movimento inválido! Por favor, insira outro.")
        imprimiu_invalido_alguma_vez = True
    else:
        movimento_valido = True

if imprimiu_invalido_alguma_vez:
    print()

# Passos Corretos:
jamal_correto = ["D12", "D33", "E12", "E31", "D12", "E31", "D12"]
# Contar Erros:
erros = 0
for i in range(7):
    if monitor_moves[i] != jamal_correto[i]:
        erros += 1
# Imprimir Matrizes do Monitor:
print(f"{monitor_menor_nota} - Movimentação 0:")
for linha in jamal_matriz_0:
    print(" ".join(linha))
pos_e = [2, 0]
pos_d = [2, 2]
for i in range(7):
    matriz_passo = [[".", ".", "."], [".", ".", "."], [".", ".", "."]]
    move = monitor_moves[i]
    # Extrair posições:
    pe = move[0]
    linha = int(move[1]) - 1
    coluna = int(move[2]) - 1

    # Atualizar matriz e posições:
    if pe == "E":
        matriz_passo[linha][coluna] = str(i + 1)
        pos_e = [linha, coluna]
        # Põe o pé D onde ele estava
        matriz_passo[pos_d[0]][pos_d[1]] = "D"
    elif pe == "D":
        matriz_passo[linha][coluna] = str(i + 1)
        pos_d = [linha, coluna]
        # Põe o pé E onde ele estava
        matriz_passo[pos_e[0]][pos_e[1]] = "E"
    # Imprimir título do movimento:
    print()
    print(f"{monitor_menor_nota} - Movimentação {i+1}:")
    # Imprimir matriz_passo:
    for linha in matriz_passo:
        print(" ".join(linha))
print()
sucesso = False
# Verificar Erros:
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
    # Recontar Erros:
    erros_2 = 0
    for i in range(7):
        if monitor_moves_2[i] != jamal_correto[i]:
            erros_2 += 1
    # Imprimir Matrizes (Repetir):
    print(f"{monitor_menor_nota} - Movimentação 0:")
    for linha in jamal_matriz_0:
        print(" ".join(linha))
    pos_e = [2, 0]
    pos_d = [2, 2]
    for i in range(7):
        matriz_passo = [[".", ".", "."], [".", ".", "."], [".", ".", "."]]
        move = monitor_moves_2[i]
        # Extrair posições:
        pe = move[0]
        linha = int(move[1]) - 1
        coluna = int(move[2]) - 1
        # Atualizar matriz e posições:
        if pe == "E":
            matriz_passo[linha][coluna] = str(i + 1)
            pos_e = [linha, coluna]
            # Põe o pé D onde ele estava
            matriz_passo[pos_d[0]][pos_d[1]] = "D"
        elif pe == "D":
            matriz_passo[linha][coluna] = str(i + 1)
            pos_d = [linha, coluna]
            # Põe o pé E onde ele estava
            matriz_passo[pos_e[0]][pos_e[1]] = "E"
        # Imprimir título do movimento:
        print()
        print(f"{monitor_menor_nota} - Movimentação {i+1}:")
        # Imprimir matriz_passo:
        for linha in matriz_passo:
            print(" ".join(linha))
    print()
    # Resultado da Segunda Tentativa:
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
    if resposta_convite == "Sim":
        print(
            f"Óbvio que o monitor {monitor_menor_nota} não perderia essa oportunidade por nada!"
        )
    elif resposta_convite == "Não":
        print(
            f"Infelizmente o monitor {monitor_menor_nota} jogou essa oportunidade fora. Todos sabem que lá na frente ele vai se arrepender disso."
        )
else:
    print(
        "Jamal desistiu de ensinar pra quem não aprende. Ele saiu em grande estilo, mandando o passinho e andando."
    )
