board = []  # Matriz que representa o tabuleiro do Sudoku
# Leitura do tabuleiro do Sudoku
for i in range(9):
    linha = input()
    linha = linha.split()
    board.append(linha)

celulas_vazias = []  # Lista de células vazias do tabuleiro
# Preenchimento da lista de células vazias
for linha in range(9):
    for coluna in range(9):
        if board[linha][coluna] == ".":
            celulas_vazias.append([linha, coluna])

# Resolução do Sudoku
k = 0
# Enquanto houver células vazias, o algoritmo continua a preencher o tabuleiro
while k < len(celulas_vazias):
    linha, coluna = celulas_vazias[k]
    valor_atual_str = board[linha][coluna]
    numero_inicial = 1
    if valor_atual_str != ".":
        numero_inicial = int(valor_atual_str) + 1

    numero_valido_encontrado = False
    numero = numero_inicial
    while numero <= 9 and not numero_valido_encontrado:
        numero_str = str(numero)
        valido = True
        for i in range(9):
            if board[linha][i] == numero_str:
                valido = False
        for i in range(9):
            if board[i][coluna] == numero_str:
                valido = False
        inicio_linha = (linha // 3) * 3
        inicio_coluna = (coluna // 3) * 3
        for lin in range(inicio_linha, inicio_linha + 3):
            for col in range(inicio_coluna, inicio_coluna + 3):
                if board[lin][col] == numero_str:
                    valido = False
        if valido:
            board[linha][coluna] = numero_str
            numero_valido_encontrado = True
        numero = numero + 1

    if numero_valido_encontrado:
        k = k + 1
    else:
        board[linha][coluna] = "."
        k = k - 1


print("Caso encerrado! Mizael provou sua inocência lógica e o Sudoku foi resolvido!")
for linha in board:
    print(" ".join(linha))
