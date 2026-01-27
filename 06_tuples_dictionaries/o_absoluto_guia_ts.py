# Dicionário que armazena os sete homens e as respectivas músicas dedicadas
vida_amorosa = {
    "Jake Gyllenhaal": [
        "All too Well",
        "We are never ever getting back together",
        "Red",
    ],
    "Joe Jonas": ["Forever & Always", "Holy Ground"],
    "Taylor Lautner": ["Back to December", "I can see you", "Midnight rain"],
    "Tom Hiddleston": ["Getaway Car"],
    "Joe Alwyn": ["Paper Rings", "Lover", "So Long London"],
    "Harry Styles": ["Style", "Out of the Woods", "All You Had to Do Was Stay"],
    "Travis Kelce": ["The Fate of Ophelia", "The Alchemy", "Wi$h Li$t"],
}

# Dicionário que relaciona os anos e os respectivos homens
relacionamentos_por_ano = {
    "2008": "Joe Jonas",
    "2009": "Taylor Lautner",
    "2010": "Jake Gyllenhaal",
    "2012": "Harry Styles",
    "2016": "Tom Hiddleston",
    "2020": "Joe Alwyn",
    "2023": "Travis Kelce",
}

# Dicionário que armazena acontecimentos da carreira em tuplas
# Atenção: Os textos foram limpos de aspas extras para garantir o output correto
acontecimentos_carreira = {
    "Fearless": (
        "Ganhou o VMA 2009, porém Kanye West interrompeu seu discurso de vitória. Também ganhou o Grammy de Álbum do Ano (2010), sendo a artista mais jovem da história (na época) a receber esse prêmio.",
    ),
    "Speak Now": (
        "Teve uma turnê mundial massiva que consolidou seu status de superestrela global, o albúm Speak Now vendeu mais de 1 milhão de cópias na primeira semana, superando qualquer outro álbum dos últimos dois anos.",
    ),
    "1989": (
        '"1989" tornou-se o primeiro álbum de Taylor exclusivamente pop; a artista emplacou dois hits mundiais: Blank Space e Bad Blood. Fun Fact: Taylor nasceu em 13 de dezembro de 1989.',
    ),
    "Reputation": (
        "O álbum foi uma resposta à mídia, às traições públicas e ao controle da narrativa sobre sua imagem. Além disso, em 2019, Taylor tem os direitos autorais de seus álbuns roubados.",
    ),
    "The Eras Tour": (
        "The Eras Tour é uma turnê comemorativa, com detalhes que buscam fazer jus á tudo que Taylor Swift fez e alcançou em seus anos de carreira. No Brasil, aconteceram seis apresentações em novembro de 2023 em São Paulo e no Rio de Janeiro.",
    ),
}

# Lista para armazenar eras roubadas por Scooter Braun
eras_roubadas = []

frase_parada = "Já chega de fatos sobre a Taylor, vai fazer a lista de IP"
entrada = input()
# Enquanto a entrada não for a frase de parada...
while entrada != frase_parada:
    # Se a entrada for "Qual a situação de relacionamento?"...
    if entrada == "Qual a situação de relacionamento?":
        # Receber a pessoa e o ano de entrada
        pessoa_input = input()
        ano_input = input()

        # Se o ano e a pessoa estiverem no dicionário de relacionamentos, imprimir que estão namorando
        if (ano_input in relacionamentos_por_ano) and (
            relacionamentos_por_ano[ano_input] == pessoa_input
        ):
            print(f"{pessoa_input} e Taylor Swift estão namorando em {ano_input}")
        # Caso contrário, imprimir que não estão namorando
        else:
            print(f"{pessoa_input} e Taylor Swift não estão namorando em {ano_input}")

    # Se a entrada for "Qual pessoa está relacionada essa música?"...
    elif entrada == "Qual pessoa está relacionada essa música?":
        # Receber a música de entrada
        musica_input = input()

        # Para cada homem e lista de músicas no dicionário de vida amorosa...
        for homem, lista_musicas in vida_amorosa.items():
            # Se a música estiver na lista de músicas do homem, imprimir o homem relacionado
            if musica_input in lista_musicas:
                print(
                    f"A pessoa relacionada é {homem}, Taylor nunca erra em suas músicas"
                )

    # Se a entrada for "Quais são todas as músicas relacionadas a essa pessoa?"...
    elif entrada == "Quais são todas as músicas relacionadas a essa pessoa?":
        # Receber o nome da pessoa de entrada
        pessoa_input = input()

        # Listar as músicas relacionadas à pessoa:
        lista_de_musicas = vida_amorosa[pessoa_input]
        musicas = ", ".join(lista_de_musicas)
        print(
            f"Cartas de amor ou indiretas, as músicas dedicadas a {pessoa_input} são: {musicas}"
        )

    # Se a entrada for "O que aconteceu nessa era?"...
    elif entrada == "O que aconteceu nessa era?":
        # Receber a era de entrada e imprimir o acontecimento da carreira
        era_input = input()
        if era_input in acontecimentos_carreira:
            print(acontecimentos_carreira[era_input][0])

    # Se a entrada for "Wayne nunca deixará Taylor vencer! O CIn precisa manter o hate na diva pop, eu vou alterar as informações"...
    elif (
        entrada
        == "Wayne nunca deixará Taylor vencer! O CIn precisa manter o hate na diva pop, eu vou alterar as informações"
    ):
        # Receber a era de entrada
        era_input = input()
        print("Cuidado, há um impostor no guia... Informações comprometidas")
        if (
            era_input in acontecimentos_carreira
        ):  # Se a era estiver no dicionário de acontecimentos da carreira...
            frase_antiga = acontecimentos_carreira[era_input][0]  # Obter a frase antiga
            nova_frase = (
                frase_antiga + " Que grande mentira! Taylor Swift só mente"
            )  # Criar a nova frase
            acontecimentos_carreira[era_input] = (
                nova_frase,
            )  # Atualizar a frase no dicionário

    # Se a entrada for "Scooter não liga que ela comprou todos os álbuns de volta, ele vai roubar tudo dessa era"...
    elif (
        entrada
        == "Scooter não liga que ela comprou todos os álbuns de volta, ele vai roubar tudo dessa era"
    ):
        # Receber a era de entrada
        era_input = input()

        eras_roubadas.append(era_input)  # Adicionar a era à lista de eras roubadas
        acontecimentos_carreira.pop(
            era_input
        )  # Remover a era do dicionário de acontecimentos da carreira
        print(
            f"Para onde foi a história sobre {era_input}? Parece que alguém roubou tudo e não avisou a Taylor"
        )

    entrada = input()

# Imprimir as eras roubadas
if (
    len(eras_roubadas) > 0
):  # Se a lista de eras roubadas não estiver vazia, ou seja, se houver eras roubadas...
    print("Big Machine Records roubou:")
    for era in eras_roubadas:  # Para cada era na lista de eras roubadas...
        print(era)  # Imprimir a era
