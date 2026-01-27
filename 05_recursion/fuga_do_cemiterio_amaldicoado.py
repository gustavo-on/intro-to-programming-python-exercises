# Função para verificar se é possível colocar uma alma em uma posição específica do tabuleiro
def pode_colocar(tabuleiro, ala_atual, lote_atual):
    for ala_anterior in range(ala_atual):  # Para cada ala anterior à atual...
        lote_anterior = tabuleiro[ala_anterior]  # Obtém o lote da alma na ala anterior
        if (
            lote_anterior == lote_atual
        ):  # Se o lote atual é o mesmo que o lote anterior, não é possível colocar a alma
            return False

        # Verifica se a alma atual está na mesma diagonal que alguma alma anterior
        distancia_ala = abs(
            ala_atual - ala_anterior
        )  # Calcula a distância entre as alas atual e anterior
        distancia_lote = abs(
            lote_atual - lote_anterior
        )  # Calcula a distância entre os lotes atual e anterior
        if (
            distancia_ala == distancia_lote
        ):  # Se a distância entre as alas for igual a distância entre os lotes, as almas estão na mesma diagonal, então não vai ser possível colocar ela.
            return False
    # Se não houver conflitos, é possível colocar a alma
    return True


# Função para posicionar as almas no tabuleiro
def posicionar_almas(n, ala_atual, tabuleiro, ala_proibida, lote_proibido):
    # Caso base: Se todas as almas foram posicionadas...
    if ala_atual == n:
        return 1  # Retorna 1 para indicar que uma configuração válida foi encontrada
    maneiras = 0  # Número de maneiras de posicionar as almas, inicialmente 0
    # Passo recursivo:
    for lote_atual in range(n):  # Para cada lote possível na ala atual...
        local_livre = True  # Assumindo que o local está livre
        if (
            ala_atual == ala_proibida and lote_atual == lote_proibido
        ):  # Se a ala e o lote atual são os proibidos...
            local_livre = False  # O local não está livre
        if local_livre:  # Se o local estiver livre...
            if pode_colocar(
                tabuleiro, ala_atual, lote_atual
            ):  # E se for possível colocar a alma...
                tabuleiro[ala_atual] = lote_atual  # Posiciona a alma no tabuleiro
                maneiras += posicionar_almas(
                    n, ala_atual + 1, tabuleiro, ala_proibida, lote_proibido
                )  # Chama a função recursivamente para a próxima ala e adiciona o número de maneiras retornado ao total de maneiras
    return maneiras  # Retorna o número total de maneiras de posicionar as almas


# Input
n = int(input())  # Número de alas e lotes

ala_ocupada = 0
lote_ocupado = 0
encontrou = False  # Variável para controlar se o túmulo ocupado foi encontrado

while not encontrou:  # Enquanto o túmulo ocupado não for encontrado...
    ala_ocupada = int(input())  # Lê a ala ocupada
    lote_ocupado = int(input())  # Lê o lote ocupado
    # Se a ala e o lote ocupados estiverem dentro dos limites do tabuleiro...
    if 1 <= ala_ocupada <= n and 1 <= lote_ocupado <= n:
        print(
            f"Rogério e Chaguinha conseguiram encontrar o túmulo ocupado em ({ala_ocupada}, {lote_ocupado})!\n"
        )
        encontrou = True
    # Caso contrário... continua o loop
    else:
        print(
            f"Rogério e Chaguinha não encontraram o túmulo ocupado na posição ({ala_ocupada}, {lote_ocupado}). Assim eles nunca vão conseguir sair do cemitério!"
        )

# Ajusta os índices para começar do 0
ala_index = ala_ocupada - 1
lote_index = lote_ocupado - 1

tabuleiro = [
    -1
] * n  # Inicializa o tabuleiro com -1 para indicar que nenhuma alma foi posicionada ainda

# Calcula o número total de possibilidades de posicionar as almas
total_possibilidades = posicionar_almas(n, 0, tabuleiro, ala_index, lote_index)
print(
    f"Rogério e Chaguinha conseguiram encontrar {total_possibilidades} possíveis posições para as almas se posicionarem sem conflitos!"
)
if (
    total_possibilidades == 0
):  # Se não houver nenhuma possibilidade de posicionar as almas...
    print(
        "Não existe nenhuma configuração segura para as almas... Rogério e Chaguinha estão presos no meio da guerra das almas!"
    )
elif (
    total_possibilidades <= 10
):  # Se o número de possibilidades for menor ou igual a 10...
    print(
        "Os amigos vão precisar tomar muito cuidado para não pegar um caminho errado!"
    )
elif (
    total_possibilidades <= 50
):  # Se o número de possibilidades for menor ou igual a 50...
    print("Uau! São tantas opções que eles até se perderam contando!")
else:  # Caso contrário... (Se o número de possibilidades for maior que 50)
    print(
        "Em pleno Halloween e as almas descansando em paz! Rogério e Chaguinha vão conseguir sair logo do cemitério."
    )
