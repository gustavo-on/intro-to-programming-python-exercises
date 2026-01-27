def possibilidades(
    valor_restante, lista_total_notas, indice_da_nota_atual
):  # Função recursiva que callcula o número de possibilidades e a contagem de notas.

    # Criar uma lista de retorno com zeros, com tamanho igual ao número de notas + 1 (para o número de possibilidades)
    num_notas = len(lista_total_notas)  # Tamanho da lista de notas
    tamanho_lista_retorno = 1 + num_notas  # Tamanho da lista de retorno
    lista_retorno_zerada = [0] * tamanho_lista_retorno  # Lista de retorno com zeros

    # Casos base:
    # Se o valor restante for zero...
    if valor_restante == 0:
        # Retorna uma lista com 1 na primeira posição (indicando uma possibilidade de pagamento) e zeros nas demais posições.
        lista_retorno_sucesso = [
            0
        ] * tamanho_lista_retorno  # Lista de retorno com zeros
        lista_retorno_sucesso[0] = 1  # Primeira posição da lista de retorno recebe 1
        return lista_retorno_sucesso
    # Se o valor restante for negativo ou se o índice da nota atual for igual ao número de notas, retorna a lista de retorno zerada.
    if valor_restante < 0:
        return lista_retorno_zerada
    if indice_da_nota_atual == num_notas:
        return lista_retorno_zerada
    # Caso contrário...
    else:
        # Calcula as possibilidades para os dois ramos da árvore de decisão e combina os resultados.
        nota_atual = lista_total_notas[indice_da_nota_atual]
        # Ramo 1: Usa a nota atual e reduz o valor restante.
        lista_resultado_ramo_1 = possibilidades(
            valor_restante - nota_atual, lista_total_notas, indice_da_nota_atual
        )
        # Ramo 2: Usa a próxima nota e mantém o valor restante.
        lista_resultado_ramo_2 = possibilidades(
            valor_restante, lista_total_notas, indice_da_nota_atual + 1
        )

        # Combinação de resultados:
        lista_retorno_combinada = [
            0
        ] * tamanho_lista_retorno  # Lista de resultados zerada
        possibilidades_ramo_1 = lista_resultado_ramo_1[
            0
        ]  # Primeira posição da lista de resultados do ramo 1 é o número de possibilidades
        possibilidades_ramo_2 = lista_resultado_ramo_2[
            0
        ]  # Primeira posição da lista de resultados do ramo 2 é o número de possibilidades
        lista_retorno_combinada[0] = (
            possibilidades_ramo_1 + possibilidades_ramo_2
        )  # Soma das possibilidades dos dois ramos
        # Combinação das contagens de notas:
        for i in range(num_notas):  # Para cada nota na lista de notas...
            indice_na_lista_retorno = (
                i + 1
            )  # Índice da nota na lista de retorno (ignora a primeira que é o número de possibilidades)
            contagem_ramo_1 = lista_resultado_ramo_1[
                indice_na_lista_retorno
            ]  # Contagem de notas do ramo 1
            contagem_ramo_2 = lista_resultado_ramo_2[
                indice_na_lista_retorno
            ]  # Contagem de notas do ramo 2
            lista_retorno_combinada[indice_na_lista_retorno] = (
                contagem_ramo_1 + contagem_ramo_2
            )  # Pega a soma das contagens de cada nota dos dois ramos e coloca na lista de retorno combinada
        numero_de_combinacoes_ramo_1 = possibilidades_ramo_1
        # Se o número de combinações do ramo 1 for maior que zero...
        if numero_de_combinacoes_ramo_1 > 0:
            # Adiciona o número de combinações do ramo 1 à contagem da nota atual na lista de retorno combinada.
            indice_da_nota_na_lista_retorno = indice_da_nota_atual + 1
            lista_retorno_combinada[
                indice_da_nota_na_lista_retorno
            ] += numero_de_combinacoes_ramo_1
        return lista_retorno_combinada


lista = [5, 10, 20, 50, 100]  # Lista de notas
valor_conta = int(input())  # Input
lista_de_resultado_final = possibilidades(
    valor_conta, lista, 0
)  # Chama a função recursiva
numero_possibilidades = lista_de_resultado_final[
    0
]  # Primeira posição da lista de resultados é o número de possibilidades

# Outputs:
print(f"Calculando possibilidades para o valor: {valor_conta}")
if numero_possibilidades == 1:  # Se o número de possibilidades for 1...
    print("\nEssa foi fácil! Só existe 1 possibilidade de pagar essa conta.")
elif numero_possibilidades == 0:  # Senão, se o número de possibilidades for 0...
    print("\nInfelizmente, não há como pagar essa conta com as notas disponíveis.")
print(f"\nTotal de possibilidades: {numero_possibilidades}")

# Imprimir o uso das notas:
print("\nUso das notas:")
tamanho_da_lista_de_notas = len(lista)
for i in range(
    tamanho_da_lista_de_notas - 1, -1, -1
):  # Percorre a lista de notas de trás para frente
    nota_em_reais = lista[i]
    quantidade_usada = lista_de_resultado_final[i + 1]
    print(f"R${nota_em_reais}: usada em {quantidade_usada} combinações")
