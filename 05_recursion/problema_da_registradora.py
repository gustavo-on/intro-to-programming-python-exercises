"""
Título: O problema da registradora!

Resumo do problema:
Determinar quantas combinações distintas de notas permitem pagar um valor exato,
considerando apenas as notas disponíveis e ignorando a ordem das notas.

Lógica principal / Regras:
- Utiliza recursão para explorar combinações sem permutação (quantidades importam, ordem não).
- Em cada passo, decide entre usar a nota atual ou avançar para a próxima.
- O caso valor_restante == 0 representa uma combinação válida (base conceitual de “não pagar nada”).
- Combina os resultados dos ramos somando o total de possibilidades e o uso de cada nota.

Entradas:
- Um inteiro representando o valor total da conta.

Saídas:
- Mensagens informativas sobre o cálculo.
- Número total de combinações possíveis.
- Quantidade de combinações em que cada nota é utilizada.
"""


def possibilidades(valor_restante, lista_total_notas, indice_da_nota_atual):
    num_notas = len(lista_total_notas)
    tamanho_lista_retorno = 1 + num_notas
    lista_retorno_zerada = [0] * tamanho_lista_retorno

    # Decisão: valor exato atingido representa uma combinação válida
    if valor_restante == 0:
        lista_retorno_sucesso = [0] * tamanho_lista_retorno
        lista_retorno_sucesso[0] = 1  # Marca exatamente uma forma válida
        return lista_retorno_sucesso

    # Decisão: valores negativos ou ausência de notas inviabilizam a combinação
    if valor_restante < 0:
        return lista_retorno_zerada
    if indice_da_nota_atual == num_notas:
        return lista_retorno_zerada
    else:
        nota_atual = lista_total_notas[indice_da_nota_atual]

        # Decisão recursiva (ramo 1): usa a nota atual, mantendo o índice
        lista_resultado_ramo_1 = possibilidades(
            valor_restante - nota_atual, lista_total_notas, indice_da_nota_atual
        )

        # Decisão recursiva (ramo 2): ignora a nota atual e avança para a próxima
        lista_resultado_ramo_2 = possibilidades(
            valor_restante, lista_total_notas, indice_da_nota_atual + 1
        )

        lista_retorno_combinada = [0] * tamanho_lista_retorno

        # Cálculo: total de combinações é a soma independente dos dois ramos
        possibilidades_ramo_1 = lista_resultado_ramo_1[0]
        possibilidades_ramo_2 = lista_resultado_ramo_2[0]
        lista_retorno_combinada[0] = possibilidades_ramo_1 + possibilidades_ramo_2

        # Cálculo: soma das contagens de uso de cada nota vindas dos dois ramos
        for i in range(num_notas):
            indice_na_lista_retorno = i + 1
            contagem_ramo_1 = lista_resultado_ramo_1[indice_na_lista_retorno]
            contagem_ramo_2 = lista_resultado_ramo_2[indice_na_lista_retorno]
            lista_retorno_combinada[indice_na_lista_retorno] = (
                contagem_ramo_1 + contagem_ramo_2
            )

        numero_de_combinacoes_ramo_1 = possibilidades_ramo_1

        # Decisão: se o ramo que usa a nota atual gera combinações,
        # incrementa o uso dessa nota proporcionalmente ao número de combinações
        if numero_de_combinacoes_ramo_1 > 0:
            indice_da_nota_na_lista_retorno = indice_da_nota_atual + 1
            lista_retorno_combinada[
                indice_da_nota_na_lista_retorno
            ] += numero_de_combinacoes_ramo_1

        return lista_retorno_combinada


lista = [5, 10, 20, 50, 100]
valor_conta = int(input())
lista_de_resultado_final = possibilidades(valor_conta, lista, 0)

numero_possibilidades = lista_de_resultado_final[0]

print(f"Calculando possibilidades para o valor: {valor_conta}")

# Decisão: mensagens especiais para casos extremos de quantidade de combinações
if numero_possibilidades == 1:
    print("\nEssa foi fácil! Só existe 1 possibilidade de pagar essa conta.")
elif numero_possibilidades == 0:
    print("\nInfelizmente, não há como pagar essa conta com as notas disponíveis.")

print(f"\nTotal de possibilidades: {numero_possibilidades}")

print("\nUso das notas:")
tamanho_da_lista_de_notas = len(lista)

# Decisão: impressão reversa apenas para atender ao formato exigido pela saída
for i in range(tamanho_da_lista_de_notas - 1, -1, -1):
    nota_em_reais = lista[i]
    quantidade_usada = lista_de_resultado_final[i + 1]
    print(f"R${nota_em_reais}: usada em {quantidade_usada} combinações")
