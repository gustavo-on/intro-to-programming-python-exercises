"""
Título: A Fuga do Cemitério Amaldiçoado

Resumo do problema:
Calcular o número de maneiras distintas de posicionar N almas em um cemitério NxN,
uma por ala (linha), sem conflitos de lote (coluna) ou diagonal, respeitando
a existência de um túmulo ocupado que não pode receber nenhuma alma.

Lógica principal / Regras:
- Cada ala deve conter exatamente uma alma.
- Não é permitido compartilhar o mesmo lote (coluna).
- Não é permitido conflito diagonal: |ala1 - ala2| = |lote1 - lote2|.
- Um lote específico é proibido e deve ser ignorado.
- A solução utiliza backtracking recursivo para explorar configurações válidas.

Entradas:
- Inteiro n: tamanho do cemitério (número de alas e lotes).
- Inteiro ala_ocupada (1-based): ala que contém o túmulo ocupado.
- Inteiro lote_ocupado (1-based): lote que contém o túmulo ocupado.

Saídas:
- Mensagens indicando se o túmulo ocupado foi encontrado.
- Quantidade total de configurações válidas.
- Mensagem adicional conforme a quantidade de possibilidades encontradas.
"""


# Função para verificar se é possível colocar uma alma em uma posição específica do tabuleiro
def pode_colocar(tabuleiro, ala_atual, lote_atual):
    for ala_anterior in range(ala_atual):
        lote_anterior = tabuleiro[ala_anterior]

        # Decisão: impedir duas almas no mesmo lote (coluna)
        if lote_anterior == lote_atual:
            return False

        # Cálculo: distâncias vertical e horizontal para verificação diagonal
        distancia_ala = abs(ala_atual - ala_anterior)
        distancia_lote = abs(lote_atual - lote_anterior)

        # Decisão: conflito diagonal ocorre quando as distâncias são iguais
        if distancia_ala == distancia_lote:
            return False

    # Se nenhuma restrição foi violada, a posição é válida
    return True


# Função recursiva para posicionar as almas no tabuleiro
def posicionar_almas(n, ala_atual, tabuleiro, ala_proibida, lote_proibido):
    # Decisão: todas as alas já foram preenchidas, configuração válida encontrada
    if ala_atual == n:
        return 1

    maneiras = 0

    # Passo recursivo: tentar cada lote possível na ala atual
    for lote_atual in range(n):
        local_livre = True

        # Decisão: impedir uso do túmulo ocupado
        if ala_atual == ala_proibida and lote_atual == lote_proibido:
            local_livre = False

        if local_livre:
            # Decisão: verificar conflitos com almas já posicionadas
            if pode_colocar(tabuleiro, ala_atual, lote_atual):
                tabuleiro[ala_atual] = lote_atual

                # Cálculo: soma das configurações válidas a partir dessa escolha
                maneiras += posicionar_almas(
                    n, ala_atual + 1, tabuleiro, ala_proibida, lote_proibido
                )

    return maneiras


# Entrada: tamanho do cemitério
n = int(input())

ala_ocupada = 0
lote_ocupado = 0
encontrou = False

# Decisão: garantir que o túmulo ocupado esteja dentro dos limites do cemitério
while not encontrou:
    ala_ocupada = int(input())
    lote_ocupado = int(input())

    if 1 <= ala_ocupada <= n and 1 <= lote_ocupado <= n:
        print(
            f"Rogério e Chaguinha conseguiram encontrar o túmulo ocupado em ({ala_ocupada}, {lote_ocupado})!\n"
        )
        encontrou = True
    else:
        print(
            f"Rogério e Chaguinha não encontraram o túmulo ocupado na posição ({ala_ocupada}, {lote_ocupado}). Assim eles nunca vão conseguir sair do cemitério!"
        )

# Ajuste de índices: conversão de 1-based para 0-based
ala_index = ala_ocupada - 1
lote_index = lote_ocupado - 1

tabuleiro = [-1] * n

# Cálculo: contagem total de configurações válidas
total_possibilidades = posicionar_almas(n, 0, tabuleiro, ala_index, lote_index)

print(
    f"Rogério e Chaguinha conseguiram encontrar {total_possibilidades} possíveis posições para as almas se posicionarem sem conflitos!"
)

# Decisão: mensagens condicionais conforme a quantidade de possibilidades
if total_possibilidades == 0:
    print(
        "Não existe nenhuma configuração segura para as almas... Rogério e Chaguinha estão presos no meio da guerra das almas!"
    )
elif total_possibilidades <= 10:
    print(
        "Os amigos vão precisar tomar muito cuidado para não pegar um caminho errado!"
    )
elif total_possibilidades <= 50:
    print("Uau! São tantas opções que eles até se perderam contando!")
else:
    print(
        "Em pleno Halloween e as almas descansando em paz! Rogério e Chaguinha vão conseguir sair logo do cemitério."
    )
