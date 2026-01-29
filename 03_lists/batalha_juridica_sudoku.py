"""
Título: A Grande Batalha Jurídica do Sudoku

Resumo do problema:
Resolver um tabuleiro de Sudoku 9x9 incompleto, preenchendo todas as células vazias (".")
de forma que as regras clássicas do Sudoku sejam respeitadas: unicidade de números
de 1 a 9 em linhas, colunas e blocos 3x3.

Lógica principal / Regras de aprovação:
- Identificar todas as células vazias do tabuleiro.
- Preencher essas células usando backtracking iterativo.
- Para cada célula vazia, tentar números de 1 a 9.
- Um número é válido se não viola linha, coluna ou bloco 3x3.
- Caso nenhuma opção seja válida, desfaz-se a tentativa anterior (retrocesso).
- O processo termina quando todas as células vazias forem preenchidas corretamente.

Entradas:
- 9 linhas, cada uma contendo 9 valores separados por espaço.
- Cada valor é um número de "1" a "9" ou "." indicando célula vazia.

Saídas:
- Mensagem final de encerramento do caso.
- Tabuleiro completo, com todos os "." substituídos pelos números corretos.
"""

board = []  # Matriz que representa o tabuleiro do Sudoku

# Leitura do tabuleiro do Sudoku
for i in range(9):
    linha = input()
    linha = linha.split()
    board.append(linha)

celulas_vazias = []  # Armazena as posições que precisam ser preenchidas

# Identificação das células vazias para orientar o backtracking
for linha in range(9):
    for coluna in range(9):
        if board[linha][coluna] == ".":  # Decisão: detectar células não preenchidas
            celulas_vazias.append([linha, coluna])

k = 0  # Índice que controla qual célula vazia está sendo processada

# Backtracking iterativo: avança ao acertar, retrocede ao errar
while k < len(celulas_vazias):
    linha, coluna = celulas_vazias[k]
    valor_atual_str = board[linha][coluna]

    numero_inicial = 1
    if (
        valor_atual_str != "."
    ):  # Decisão: continuar tentativa a partir do último valor usado
        numero_inicial = int(valor_atual_str) + 1

    numero_valido_encontrado = False
    numero = numero_inicial

    # Testa números possíveis de 1 a 9
    while numero <= 9 and not numero_valido_encontrado:
        numero_str = str(numero)
        valido = True

        # Verificação da linha
        for i in range(9):
            if board[linha][i] == numero_str:  # Decisão: violação de unicidade na linha
                valido = False

        # Verificação da coluna
        for i in range(9):
            if (
                board[i][coluna] == numero_str
            ):  # Decisão: violação de unicidade na coluna
                valido = False

        # Cálculo do início do bloco 3x3
        inicio_linha = (linha // 3) * 3
        inicio_coluna = (coluna // 3) * 3

        # Verificação do bloco 3x3
        for lin in range(inicio_linha, inicio_linha + 3):
            for col in range(inicio_coluna, inicio_coluna + 3):
                if board[lin][col] == numero_str:  # Decisão: violação no bloco
                    valido = False

        if valido:  # Decisão: número respeita todas as regras
            board[linha][coluna] = numero_str
            numero_valido_encontrado = True

        numero = numero + 1  # Avança para o próximo candidato

    if numero_valido_encontrado:  # Decisão: segue para a próxima célula vazia
        k = k + 1
    else:
        board[linha][coluna] = "."  # Retrocesso: desfaz tentativa atual
        k = k - 1  # Volta para a célula anterior

print("Caso encerrado! Mizael provou sua inocência lógica e o Sudoku foi resolvido!")
for linha in board:
    print(" ".join(linha))
