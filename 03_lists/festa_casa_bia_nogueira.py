# Lista de influencers e cantores:
bolha_influencers = ["Sofia Santino", "Doarda", "Ciclopin", "Bruna Pinheiro"]
bolha_cantores = [
    "Thiaguinho",
    "Little Thiago",
    "Neiff",
    "O Diferenciado",
    "Veigh",
    "Mc Loma",
]

convidados_confirmados = []  # Lista de convidados confirmados

primeira_entrada = input()
if primeira_entrada == "WhatsApp: 0 mensagens.":  # Caso não tenha nenhuma mensagem
    print(
        "I hate to tell you this BUT\nBia tava achando que ia fazer um mousse. O mousse virou uma piada, parceira"
    )
    print(
        "\nComo a vida não precisa ser only fechos, a gente vai finalizar minha franja hoje:\nEssa chapinha eu dei literalmente tipo 50 reais nela. Não é a mais potente, não é a mais mais... mas ela é algo. Às vezes a gente só precisa ser algo, não precisa ser tudo.\nE o protetor térmico? Vei, a chapinha sabe que eu tô fazendo de coração, ela nunca queimaria meu cabelo.\nEspera esfriar e você vai barbarizar quando tiver pronto\nÉ isso, tchau meus amores"
    )
else:  # Caso tenha mensagens
    entrada_atual = primeira_entrada
    # Loop para ler todas as mensagens:
    while entrada_atual != "CABOSSE! Bora simbora organizar essa festa.":
        # Adicionar o nome do convidado na lista de convidados confirmados:
        nome_convidado = entrada_atual.split(" acabou de confirmar")[0]
        convidados_confirmados.append(nome_convidado)
        # Caso o convidado seja Mc Loma, adicionar Mirella e Mariely na lista de convidados confirmados:
        if nome_convidado == "Mc Loma":
            convidados_confirmados.append("Mirella Santos")
            convidados_confirmados.append("Mariely Santos")
        # Ler a próxima entrada:
        entrada_atual = input()

    tem_influencer = False
    tem_cantor = False
    # Verificar se tem algum influencer ou cantor na lista de convidados confirmados:
    for convidado in convidados_confirmados:
        if convidado in bolha_influencers:
            tem_influencer = True
        elif convidado in bolha_cantores:
            tem_cantor = True
    if tem_influencer and tem_cantor:
        print("Cachaçaria na minha casa hoje, 21h.")
        print(
            "Todo mundo lá em casa! Tem que ser uma festa que dure muito, tipo 27 anos e 3 meses!!"
        )
    elif tem_cantor:
        print("<PLANOS PARA FESTA>")
        nomes_formatados = ", ".join(convidados_confirmados)
        print(f"Convidados: {nomes_formatados}.")
        print("Tipo de comemoração: Paredão - Show na minha casa!!")
    elif tem_influencer:
        print("<TARDE DE FOFOCAS>")
        nomes_formatados = ", ".join(convidados_confirmados)
        print(f"Convidados: {nomes_formatados}.")
        num_convidados = len(convidados_confirmados)
        lista_pautas = []
        for i in range(num_convidados):
            pauta = input()
            lista_pautas.append(pauta)
        for pauta in lista_pautas:
            if pauta == "Medo de ficar musculosa demais por causa da academia":
                print(
                    "AMIGA, ouça: tem nem o P do PERIGO de você ficar grandona sem querer. Não se preocupe!"
                )
            elif (
                pauta
                == "O cara que eu gosto não me quer, mas eu continuo insistindo. Acha que eu consigo algo?"
            ):
                print(
                    "Claro que consegue, amiga! Consegue virar uma palhaça, consegue perder a autoestima... Consegue várias coisas :)"
                )
            elif (
                pauta == "Meu chefe só me dá um dia de folga, mas eu precisava de dois."
            ):
                print(
                    "Tem que ter pelo menos dois dias de descanso. Se seu chefe tem uma empresa que não pode passar dois dias fechada porque vai quebrar, ele deveria fechar! Isso não é nem uma empresa, é um quiosque!"
                )
            elif pauta == "Pessoas que adoram se fazer de coitadinhas":
                print(
                    "Eu detesto quem gosta de ficar pagando de coitadinho(a). Se for chorar… Na verdade, não chora não, que eu não quero nem ouvir."
                )
            elif pauta == "Essa história de que homem sofre calado":
                print(
                    "Vocês ficam dizendo que homem sofre, que homem sofre calado… E por que eu ainda estou ouvindo? Por que eu ainda ouço???"
                )

        num_amigos_concordam = int(input())  # Número de amigos que concordam
        # Decidir o que fazer com base no número de amigos que concordam:
        if num_amigos_concordam == 0:  # Se ninguém concorda:
            print("Apois me interne, me prenda, me jogue fora que eu tô maluca!")
        else:  # Caso tenha pelo menos um amigo que concorde:
            print(
                "É isso, eu vejo tanta coisa errada nesse mundo… Mas é como dizem, né?! Life snake, a vida cobra em inglês."
            )
