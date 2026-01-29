"""
Título: A Festa na Casa de Bia Nogueira

Resumo do problema:
O programa simula a organização de uma festa a partir de confirmações de convidados,
classificados em duas bolhas sociais (influencers e cantores). Com base nas confirmações,
o sistema decide automaticamente o tipo de evento que será realizado ou se a festa será
cancelada, além de gerenciar interações adicionais em caso de "tarde de fofocas".

Lógica principal / Regras de decisão:
- Caso não haja nenhuma confirmação inicial, a festa é cancelada e um roteiro fixo é exibido.
- As confirmações são processadas até uma frase sentinela indicar o fim da entrada.
- Se houver convidados de bolhas diferentes, a festa se torna uma "cachaçaria".
- Se todos forem cantores, ocorre um show com paredão.
- Se todos forem influencers, ocorre uma tarde de fofocas com interações adicionais.
- A presença de Mc Loma implica a adição automática de convidados extras.
- Ao final da tarde de fofocas, a decisão final depende da concordância dos convidados.

Entradas:
- Uma string inicial indicando ausência de mensagens ou confirmação de convidado.
- Sequência de confirmações no formato "{Nome} acabou de confirmar".
- Frase sentinela para encerrar confirmações.
- (Opcional) Pautas de fofoca, uma por convidado.
- Um inteiro representando quantos amigos concordaram com Bia.

Saídas:
- Mensagens textuais que descrevem o plano da festa, cancelamento ou interações,
  conforme as regras do problema.
"""

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

convidados_confirmados = (
    []
)  # Lista que centraliza o estado da confirmação dos convidados

primeira_entrada = input()

# Decisão baseada na ausência total de confirmações iniciais
if primeira_entrada == "WhatsApp: 0 mensagens.":
    print(
        "I hate to tell you this BUT\nBia tava achando que ia fazer um mousse. O mousse virou uma piada, parceira"
    )
    print(
        "\nComo a vida não precisa ser only fechos, a gente vai finalizar minha franja hoje:\nEssa chapinha eu dei literalmente tipo 50 reais nela. Não é a mais potente, não é a mais mais... mas ela é algo. Às vezes a gente só precisa ser algo, não precisa ser tudo.\nE o protetor térmico? Vei, a chapinha sabe que eu tô fazendo de coração, ela nunca queimaria meu cabelo.\nEspera esfriar e você vai barbarizar quando tiver pronto\nÉ isso, tchau meus amores"
    )
else:
    entrada_atual = primeira_entrada

    # Loop controlado por frase sentinela para processar confirmações indefinidas
    while entrada_atual != "CABOSSE! Bora simbora organizar essa festa.":
        nome_convidado = entrada_atual.split(" acabou de confirmar")[0]
        convidados_confirmados.append(nome_convidado)

        # Regra especial: Mc Loma implica a inclusão automática de convidadas associadas
        if nome_convidado == "Mc Loma":
            convidados_confirmados.append("Mirella Santos")
            convidados_confirmados.append("Mariely Santos")

        entrada_atual = input()

    tem_influencer = False
    tem_cantor = False

    # Varredura da lista para identificar presença de cada bolha
    for convidado in convidados_confirmados:
        if convidado in bolha_influencers:
            tem_influencer = True
        elif convidado in bolha_cantores:
            tem_cantor = True

    # Mistura de bolhas invalida a separação e força a escolha da cachaçaria
    if tem_influencer and tem_cantor:
        print("Cachaçaria na minha casa hoje, 21h.")
        print(
            "Todo mundo lá em casa! Tem que ser uma festa que dure muito, tipo 27 anos e 3 meses!!"
        )

    # Exclusividade de cantores direciona para evento musical
    elif tem_cantor:
        print("<PLANOS PARA FESTA>")
        nomes_formatados = ", ".join(convidados_confirmados)
        print(f"Convidados: {nomes_formatados}.")
        print("Tipo de comemoração: Paredão - Show na minha casa!!")

    # Exclusividade de influencers ativa a lógica de interação por pautas
    elif tem_influencer:
        print("<TARDE DE FOFOCAS>")
        nomes_formatados = ", ".join(convidados_confirmados)
        print(f"Convidados: {nomes_formatados}.")

        # Quantidade de pautas depende diretamente do número de convidados confirmados
        num_convidados = len(convidados_confirmados)
        lista_pautas = []

        for i in range(num_convidados):
            pauta = input()
            lista_pautas.append(pauta)

        # Respostas condicionais baseadas em correspondência exata das pautas
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

        num_amigos_concordam = int(input())

        # Decisão final baseada na unanimidade ou não da discordância
        if num_amigos_concordam == 0:
            print("Apois me interne, me prenda, me jogue fora que eu tô maluca!")
        else:
            print(
                "É isso, eu vejo tanta coisa errada nesse mundo… Mas é como dizem, né?! Life snake, a vida cobra em inglês."
            )
