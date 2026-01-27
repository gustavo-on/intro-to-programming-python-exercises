# Criar Gerenciador de Componentes
componentes_memoria_rom_simples = [
    "Redstone",
    256,
    "Repetidores",
    64,
    "Tochas de Redstone",
    128,
]
componentes_calculadora_4_bits = [
    "Redstone",
    512,
    "Repetidores",
    128,
    "Tochas de Redstone",
    64,
    "Lâmpadas de Redstone",
    256,
]
componentes_sequenciador_musical = [
    "Redstone",
    1024,
    "Repetidores",
    256,
    "Blocos de Notas",
    64,
    "Observadores",
    128,
]
componentes_processador_8_bits = [
    "Redstone",
    4096,
    "Repetidores",
    1024,
    "Lâmpadas de Redstone",
    2048,
    "Pistões Aderentes",
    512,
]
componentes_display_video_8x8 = [
    "Redstone",
    2048,
    "Repetidores",
    512,
    "Comparadores",
    256,
    "Pistões",
    128,
]
componentes_supercomputador_v13 = [
    "Redstone",
    8192,
    "Repetidores",
    2048,
    "Comparadores",
    1024,
    "Pistões Aderentes",
    1024,
]

# Input
nome_projeto = input()

# Componentes coletados e suas respectivas quantidades
componentes_projeto = []
if nome_projeto == "Memória ROM Simples":
    componentes_projeto = componentes_memoria_rom_simples
elif nome_projeto == "Calculadora de 4 bits":
    componentes_projeto = componentes_calculadora_4_bits
elif nome_projeto == "Sequenciador Musical":
    componentes_projeto = componentes_sequenciador_musical
elif nome_projeto == "Processador de 8 Bits":
    componentes_projeto = componentes_processador_8_bits
elif nome_projeto == "Display de Vídeo 8x8":
    componentes_projeto = componentes_display_video_8x8
elif nome_projeto == "Supercomputador V13":
    componentes_projeto = componentes_supercomputador_v13

# Recebimento de componentes e suas quantidades
lista_componentes_e_quantidades = []
ordem_entrada = []

construiu = False

while not construiu:
    # Receber componentes até "Construir!"
    entrada = input()

    while (
        entrada != "Construir!"
    ):  # Recebimento de componentes interrompido quando for digitado "Construir!"
        nome_componente, valor = entrada.rsplit(" ", 1)
        quantidade_item = int(valor)

        # Verificar se o componente já está na lista
        if nome_componente in lista_componentes_e_quantidades:
            index_componente = lista_componentes_e_quantidades.index(nome_componente)
            lista_componentes_e_quantidades[index_componente + 1] += quantidade_item
        else:
            lista_componentes_e_quantidades.append(nome_componente)
            lista_componentes_e_quantidades.append(quantidade_item)
            ordem_entrada.append(nome_componente)

        # Verificar se o componente está na lista de componentes necessários
        if nome_componente not in componentes_projeto:
            print(f"Hmm, {nome_componente} não parece ser útil para este projeto.")
        else:
            if nome_componente == "Redstone":
                print(
                    f"Mais redstone! A energia que move o progresso! (+{quantidade_item} Redstone)"
                )
            elif nome_componente == "Repetidores":
                print(
                    f"Repetidores para garantir que o sinal chegue longe! Perfeito! (+{quantidade_item} Repetidores)"
                )
            elif nome_componente == "Tochas de Redstone":
                print(
                    f"Tochas de Redstone! Ótimo para inverter um sinal ou energizar o sistema. (+{quantidade_item} Tochas de Redstone)"
                )
            elif nome_componente == "Lâmpadas de Redstone":
                print(
                    f"Lâmpadas para o display! O resultado vai ficar bem visível. (+{quantidade_item} Lâmpadas de Redstone)"
                )
            elif nome_componente == "Blocos de Notas":
                print(
                    f"Blocos de Notas! Quem sabe não rola uma musiquinha no final? (+{quantidade_item} Blocos de Notas)"
                )
            elif nome_componente == "Observadores":
                print(
                    f"Observadores a postos! Nenhuma atualização de bloco passará despercebida. (+{quantidade_item} Observadores)"
                )
            elif nome_componente == "Comparadores":
                print(
                    f"Comparadores para a lógica! A precisão é a alma do negócio. (+{quantidade_item} Comparadores)"
                )
            elif nome_componente == "Pistões":
                print(
                    f"Pistões para mover as coisas de lugar. Isso vai ser útil! (+{quantidade_item} Pistões)"
                )
            elif nome_componente == "Pistões Aderentes":
                print(
                    f"Pistões Aderentes! Perfeitos para criar mecanismos retráteis. (+{quantidade_item} Pistões Aderentes)"
                )

        entrada = input()

    # Analisar se ele conseguiu a quantidade necessária de cada componente
    pode_construir = True
    itens_faltantes = []

    for i in range(0, len(componentes_projeto), 2):
        componente_necessario = componentes_projeto[i]
        quantidade_necessaria = componentes_projeto[i + 1]

        quantidade_coletada = 0
        if componente_necessario in lista_componentes_e_quantidades:
            index_componente = lista_componentes_e_quantidades.index(
                componente_necessario
            )
            quantidade_coletada = lista_componentes_e_quantidades[index_componente + 1]

        if quantidade_coletada < quantidade_necessaria:
            pode_construir = False
            falta = quantidade_necessaria - quantidade_coletada
            packs_faltantes = falta // 64
            if packs_faltantes == 0:
                packs_faltantes = 1
            itens_faltantes.append(componente_necessario)
            itens_faltantes.append(packs_faltantes)

    # Prints
    if pode_construir:
        print(
            f"\nViniccius13 conseguiu construir o {nome_projeto}! Partiu programar!\n"
        )
        print(f"Para construirmos a(o) {nome_projeto}, utilizamos:\n")

        # Imprimir os componentes utilizados
        for componente in ordem_entrada:
            if componente in componentes_projeto:
                index_componente = lista_componentes_e_quantidades.index(componente)
                quantidade_componente = lista_componentes_e_quantidades[
                    index_componente + 1
                ]
                print(f"{componente} : {quantidade_componente}")

        # Verificar se existem componentes que não são necessários
        componentes_nao_uteis = False
        for componente in ordem_entrada:
            if componente not in componentes_projeto:
                componentes_nao_uteis = True

        # Imprimir os componentes que não são necessários
        if componentes_nao_uteis:
            print("\nMas, em nossa jornada, também coletamos:\n")
            for componente in ordem_entrada:
                if componente not in componentes_projeto:
                    index_componente = lista_componentes_e_quantidades.index(componente)
                    quantidade_componente = lista_componentes_e_quantidades[
                        index_componente + 1
                    ]
                    print(f"{componente} : {quantidade_componente}")

        construiu = True
    else:
        # Componentes faltantes
        print(f"\nAinda não é possível construir o {nome_projeto}! Faltam:\n")
        for i in range(0, len(itens_faltantes), 2):
            nome_componente = itens_faltantes[i]
            packs = itens_faltantes[i + 1]
            print(f"{packs} pack(s) de {nome_componente}")
        print("")
