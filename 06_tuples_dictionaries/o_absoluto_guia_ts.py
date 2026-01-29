"""
Título: O Absoluto Guia T.S

Resumo do problema:
Implementar um sistema interativo de consultas sobre a vida amorosa e a carreira de
Taylor Swift, respondendo dinamicamente a diferentes tipos de perguntas até que uma
frase de encerramento seja fornecida.

Lógica principal / Regras:
- As informações da vida amorosa são armazenadas em dicionários, relacionando pessoas,
  músicas e anos específicos de relacionamento.
- Os acontecimentos da carreira são armazenados em tuplas, respeitando a imutabilidade
  exigida pelo enunciado.
- Consultas podem alterar o estado do sistema: ataques podem modificar textos ou remover
  eras permanentemente.
- O programa deve processar entradas sequenciais até encontrar a frase de parada.

Entradas:
- Sequência de strings indicando o tipo de consulta.
- Dados complementares (pessoa, música, ano ou era), conforme a consulta.
- Uma frase específica encerra a execução.

Saídas:
- Respostas textuais conforme o tipo de consulta.
- Impressão final das eras removidas, caso existam.
"""

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

# Dicionário que relaciona cada ano ao único relacionamento considerado ativo
relacionamentos_por_ano = {
    "2008": "Joe Jonas",
    "2009": "Taylor Lautner",
    "2010": "Jake Gyllenhaal",
    "2012": "Harry Styles",
    "2016": "Tom Hiddleston",
    "2020": "Joe Alwyn",
    "2023": "Travis Kelce",
}

# Dicionário que armazena acontecimentos da carreira em tuplas (estrutura imutável)
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

# Lista que registra permanentemente as eras removidas do sistema
eras_roubadas = []

frase_parada = "Já chega de fatos sobre a Taylor, vai fazer a lista de IP"
entrada = input()

# Decisão de controle: o programa continua enquanto a frase de parada não for recebida
while entrada != frase_parada:

    # Decisão: consulta sobre status de relacionamento em um ano específico
    if entrada == "Qual a situação de relacionamento?":
        pessoa_input = input()
        ano_input = input()

        # Critério: apenas a pessoa associada ao ano consultado é considerada em relacionamento
        if (ano_input in relacionamentos_por_ano) and (
            relacionamentos_por_ano[ano_input] == pessoa_input
        ):
            print(f"{pessoa_input} e Taylor Swift estão namorando em {ano_input}")
        else:
            print(f"{pessoa_input} e Taylor Swift não estão namorando em {ano_input}")

    # Decisão: consulta reversa, da música para a pessoa associada
    elif entrada == "Qual pessoa está relacionada essa música?":
        musica_input = input()

        # Busca sequencial para identificar a quem a música foi associada
        for homem, lista_musicas in vida_amorosa.items():
            if musica_input in lista_musicas:
                print(
                    f"A pessoa relacionada é {homem}, Taylor nunca erra em suas músicas"
                )

    # Decisão: listagem completa de músicas associadas a uma pessoa
    elif entrada == "Quais são todas as músicas relacionadas a essa pessoa?":
        pessoa_input = input()

        # Operação de composição: transformação da lista em string formatada para saída
        lista_de_musicas = vida_amorosa[pessoa_input]
        musicas = ", ".join(lista_de_musicas)
        print(
            f"Cartas de amor ou indiretas, as músicas dedicadas a {pessoa_input} são: {musicas}"
        )

    # Decisão: consulta direta a um acontecimento de uma era específica
    elif entrada == "O que aconteceu nessa era?":
        era_input = input()

        # Critério: só imprime se a era ainda existir no sistema
        if era_input in acontecimentos_carreira:
            print(acontecimentos_carreira[era_input][0])

    # Decisão: ataque de Wayne Kest, que compromete a informação sem removê-la
    elif (
        entrada
        == "Wayne nunca deixará Taylor vencer! O CIn precisa manter o hate na diva pop, eu vou alterar as informações"
    ):
        era_input = input()
        print("Cuidado, há um impostor no guia... Informações comprometidas")

        # Critério: a frase é estendida, mantendo o texto original e adicionando a acusação
        if era_input in acontecimentos_carreira:
            frase_antiga = acontecimentos_carreira[era_input][0]
            nova_frase = frase_antiga + " Que grande mentira! Taylor Swift só mente"
            acontecimentos_carreira[era_input] = (nova_frase,)

    # Decisão: ataque de Scooter Braun, que remove a era definitivamente
    elif (
        entrada
        == "Scooter não liga que ela comprou todos os álbuns de volta, ele vai roubar tudo dessa era"
    ):
        era_input = input()

        # Registro da remoção para relatório final
        eras_roubadas.append(era_input)

        # Operação destrutiva: exclusão permanente da era do dicionário
        acontecimentos_carreira.pop(era_input)
        print(
            f"Para onde foi a história sobre {era_input}? Parece que alguém roubou tudo e não avisou a Taylor"
        )

    entrada = input()

# Decisão final: só imprime o relatório se ao menos uma era tiver sido roubada
if len(eras_roubadas) > 0:
    print("Big Machine Records roubou:")
    for era in eras_roubadas:
        print(era)
