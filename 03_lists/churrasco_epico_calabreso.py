"""
Título: O Churrasco Épico do Calabreso

Resumo do problema:
O programa gerencia a entrada de convidados para um churrasco seguindo regras específicas:
proibição de certos convidados, eliminação de pratos repetidos e análise dos preços das comidas
para gerar mensagens e um relatório final ordenado.

Lógica principal / regras de aprovação:
- Convidados chamados "Maicon Kuster" são automaticamente expulsos.
- Não é permitido repetir pratos; convidados com pratos duplicados são removidos.
- Se nenhum convidado válido permanecer, uma mensagem de ausência é exibida.
- O convidado com a comida mais cara recebe um agradecimento especial.
- O convidado com a comida mais barata recebe uma mensagem de crítica (se houver mais de um).
- Empates de preço são resolvidos pelo nome em ordem alfabética.
- A lista final é ordenada por preço crescente e, em caso de empate, por nome.

Entradas:
- Um inteiro representando o número de convidados.
- Para cada convidado:
  - Nome do convidado (string)
  - Nome da comida (string)
  - Valor da comida (int)

Saídas:
- Mensagens de expulsão conforme as regras.
- Mensagem para o convidado da comida mais cara.
- Mensagem para o convidado da comida mais barata (quando aplicável).
- Lista final dos convidados ordenada pelo preço das comidas.
"""

# Número de convidados informados na entrada
num_convidados = int(input())
convidados = []

for i in range(num_convidados):
    nome_convidado = input()
    comida_convidado = input()
    valor_comida = int(input())
    convidados.append([nome_convidado, comida_convidado, valor_comida])

# Remoção do convidado proibido (Maicon Kuster)
convidados_temp = []
for convidado in convidados:
    # Decisão: aplica regra de expulsão imediata baseada no nome
    if convidado[0] == "Maicon Kuster":
        print("você é convidado DE GUÊÊ???, sai da minha festa seu FOFOQUEIRO!!")
    else:
        convidados_temp.append(convidado)
convidados = convidados_temp

# Remoção de convidados com pratos repetidos
pratos_vistos = {}
convidados_temp = []
for convidado in convidados:
    # Decisão: controla pratos já utilizados para garantir diversidade gastronômica
    if convidado[1] not in pratos_vistos:
        pratos_vistos[convidado[1]] = True
        convidados_temp.append(convidado)
    else:
        print(f"Na Festa do Calabreso não pode comida Repetida SAI FORA {convidado[0]}")
convidados = convidados_temp

# Verificação se restou algum convidado válido
if len(convidados) == 0:
    print("Nenhum convidado marcou presença na festa do calabreso!")

else:
    # Identificação da comida mais cara
    maior_valor = -1
    for convidado in convidados:
        # Decisão: atualiza o maior valor encontrado
        if convidado[2] > maior_valor:
            maior_valor = convidado[2]
            nome_maior_convidado = convidado[0]
            comida_maior_convidado = convidado[1]
        # Desempate: escolhe o nome alfabeticamente menor em caso de valores iguais
        elif convidado[2] == maior_valor and convidado[0] < nome_maior_convidado:
            nome_maior_convidado = convidado[0]
            comida_maior_convidado = convidado[1]

    print(
        f"Obrigado para o(a) {nome_maior_convidado} pelo(a) excelente {comida_maior_convidado}"
    )

    if len(convidados) >= 2:
        # Identificação da comida mais barata
        menor_valor = 10000000000
        for convidado in convidados:
            # Decisão: atualiza o menor valor encontrado
            if convidado[2] < menor_valor:
                menor_valor = convidado[2]
                nome_menor_convidado = convidado[0]
                comida_menor_convidado = convidado[1]
            # Desempate: escolhe o nome alfabeticamente menor em caso de valores iguais
            elif convidado[2] == menor_valor and convidado[0] < nome_menor_convidado:
                nome_menor_convidado = convidado[0]
                comida_menor_convidado = convidado[1]

        print(
            f"Rapaz, {nome_menor_convidado} trouxe o(a) {comida_menor_convidado} que estava altamente mais ou menos!!!"
        )

    # Ordenação dos convidados por preço crescente e nome em caso de empate
    for i in range(len(convidados)):
        for j in range(len(convidados) - 1 - i):
            # Decisão: troca elementos para garantir ordenação correta
            if convidados[j][2] > convidados[j + 1][2] or (
                convidados[j][2] == convidados[j + 1][2]
                and convidados[j][0] > convidados[j + 1][0]
            ):
                convidados[j], convidados[j + 1] = convidados[j + 1], convidados[j]

    print("Lista de convidados do Calabreso")
    for i in range(1, len(convidados) + 1):
        print(f"{i}- {convidados[i-1][0]}")
