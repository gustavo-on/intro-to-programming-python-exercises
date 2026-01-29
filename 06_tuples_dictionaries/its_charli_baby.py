"""
Título: it's charli baby ;)

Resumo do problema:
O programa monta automaticamente a setlist de um show da Charli XCX dividida em três atos,
respeitando restrições de gênero musical e limite máximo de duração por ato. Cada música
recebida é validada quanto a nome proibido, gênero permitido e tempo disponível no ato,
sendo aprovada ou descartada conforme as regras.

Regras de aprovação / lógica principal:
- O show é dividido em 3 atos, cada um com gêneros permitidos e limite máximo de duração.
- Músicas são analisadas sequencialmente conforme o ato atual.
- A música "Actually Romantic" é sempre descartada.
- Músicas com gênero incompatível com o ato são descartadas.
- Músicas que excedem o tempo máximo do ato são descartadas.
- Músicas válidas são armazenadas em tuplas dentro de um dicionário principal.
- Ao final, o programa avalia se algum ato ficou abaixo de 70% do tempo máximo e gera
  um relatório completo da setlist e um resumo de aprovadas e descartadas.

Entradas:
- Linhas com músicas no formato: nome, gênero, duração (mm:ss).
- Marcadores de controle: FIM_ATO_1, FIM_ATO_2 e FIM_SHOW.

Saídas:
- Mensagens de análise e validação durante a montagem da setlist.
- Relatório final com músicas por ato, duração total e avisos.
- Resumo final com total de músicas aprovadas e descartadas.
"""

print("Don't sleep, don't eat, just do it on repeat! Keep bumpin' that!!!\n")

# Dicionário de atos com nome, gêneros permitidos e duração máxima
dicionario_atos = {
    1: ("Abertura", ("Hyperpop", "Pop"), 600),
    2: ("Sentimental", ("Sentimental", "Ballad"), 480),
    3: ("Encerramento", ("Hyperpop", "Banger"), 720),
}

setlist_final = {1: [], 2: [], 3: []}

num_aprovadas = 0
num_descartadas = 0
ato_atual = 1
duracao_total_ato = 0
primeira_iteracao_ato = True
fim_do_show = False


def converte_para_segundos(string):
    partes = string.split(":")
    minutos = int(partes[0])
    segundos = int(partes[1])
    # Cálculo: conversão de minutos para segundos e soma com os segundos restantes
    total_segundos = (minutos * 60) + segundos
    return total_segundos


def analise_musica(entrada, ato_atual, duracao_total, aprovadas, descartadas, setlist):
    nova_duracao = duracao_total
    novas_aprovadas = aprovadas
    novas_descartadas = descartadas

    partes_musica = entrada.split(",")
    nome_musica = partes_musica[0].strip()
    genero_musica = partes_musica[1].strip()
    duracao_str = partes_musica[2].strip()

    print(f"Música em análise: {nome_musica}")

    musica_aprovada_para_ato = True

    # Decisão: música explicitamente proibida deve ser descartada imediatamente
    if nome_musica == "Actually Romantic":
        print(
            "Já não basta ter exposto a Charli nessa música, agora a Taylor quer que a própria cante? GOLPE BAIXÍSSIMO!!!"
        )
        novas_descartadas += 1
        musica_aprovada_para_ato = False

    # Decisões: mensagens especiais para músicas específicas (não afetam aprovação)
    elif nome_musica == "Talk Talk featuring troye sivan":
        print(
            "A MAIOR AMIZADE DO POP NO PALCO? Talk to them in your own made-up language!"
        )
    elif nome_musica == "Von dutch a. g. cook remix featuring addison rae":
        print(
            "‘CAUSE THEY’RE JUST LIVING THAT LIFE! Addison Rae, a maior revelação do pop desde Britney Spears, no palco ao lado da sua amiga Charli XCX!"
        )
    elif nome_musica == "Guess featuring billie eilish":
        print("Hey, Billie, you there?")

    if musica_aprovada_para_ato:
        generos_permitidos = dicionario_atos[ato_atual][1]
        # Decisão: garante que o gênero respeita a proposta artística do ato
        if genero_musica not in generos_permitidos:
            print(
                "Gênero errado para esse ato! Cuidado, uma música deslocada mata a vibe de um show…"
            )
            novas_descartadas += 1
            musica_aprovada_para_ato = False

    if musica_aprovada_para_ato:
        duracao_musica_seg = converte_para_segundos(duracao_str)
        limite_segundos_ato = dicionario_atos[ato_atual][2]
        # Decisão: impede que o tempo total do ato ultrapasse o limite máximo
        if nova_duracao + duracao_musica_seg > limite_segundos_ato:
            print(
                f"Muito longa! O Ato {ato_atual} já está com {nova_duracao} segundos e essa música tem {duracao_musica_seg} segundos."
            )
            novas_descartadas += 1
            musica_aprovada_para_ato = False

    if musica_aprovada_para_ato:
        duracao_musica_seg = converte_para_segundos(duracao_str)
        dados_musica = (nome_musica, genero_musica, duracao_musica_seg)
        setlist[ato_atual].append(dados_musica)
        # Cálculo: acumula a duração total do ato apenas com músicas aprovadas
        nova_duracao += duracao_musica_seg
        novas_aprovadas += 1
        print(f"{nome_musica} adicionada ao Ato {ato_atual} ;).")

    return nova_duracao, novas_aprovadas, novas_descartadas


# Loop principal de leitura e controle de atos
while not fim_do_show:
    entrada = input()

    # Decisão: encerra completamente o processamento
    if entrada == "FIM_SHOW":
        fim_do_show = True
        print()

    # Decisão: transição controlada entre atos
    elif entrada == "FIM_ATO_1":
        print()
        ato_atual = 2
        duracao_total_ato = 0
        primeira_iteracao_ato = True

    elif entrada == "FIM_ATO_2":
        print()
        ato_atual = 3
        duracao_total_ato = 0
        primeira_iteracao_ato = True

    else:
        if primeira_iteracao_ato:
            config_ato = dicionario_atos[ato_atual]
            genero_1 = config_ato[1][0]
            genero_2 = config_ato[1][1]
            print(f"Iniciando montagem do Ato {ato_atual} ({genero_1} e {genero_2}):\n")
            primeira_iteracao_ato = False

        duracao_total_ato, num_aprovadas, num_descartadas = analise_musica(
            entrada,
            ato_atual,
            duracao_total_ato,
            num_aprovadas,
            num_descartadas,
            setlist_final,
        )

# Relatório final
avisos_doces_backstage = False

for num_ato in range(1, 4):
    limites_segundos = dicionario_atos[num_ato][2]
    lista_musicas = setlist_final[num_ato]
    duracao_total = 0

    for musica in lista_musicas:
        # Cálculo: soma acumulada da duração real do ato
        duracao_total += musica[2]

    # Cálculo: definição do limite mínimo aceitável (70% do tempo máximo)
    limite_70 = limites_segundos * 0.7

    # Decisão: identifica atos curtos demais para um show adequado
    if duracao_total < limite_70:
        avisos_doces_backstage = True

if avisos_doces_backstage:
    print(
        "Tem certeza que isso é um show? Rápido desse jeito, a Charli XCX deve estar pensando nos doces do backstage…\n"
    )

for num_ato in range(1, 4):
    nome_ato = dicionario_atos[num_ato][0]
    lista_musicas = setlist_final[num_ato]

    print(f"--- Ato {num_ato} ({nome_ato}) ---")
    duracao_total_print = 0

    # Decisão: tratamento explícito para atos sem músicas aprovadas
    if not lista_musicas:
        print("Nenhuma música adicionada a este Ato.")
    else:
        for musica in lista_musicas:
            nome = musica[0]
            genero = musica[1]
            tempo = musica[2]
            duracao_total_print += tempo
            print(f"{nome} ({genero})")

    print(f"Duração total do ato: {duracao_total_print} segundos.\n")

print("=== RESUMO DO SHOW (BRAT APPROVED) ===")
print(f"Total de músicas na setlist: {num_aprovadas}")
print(f"Total de músicas barradas: {num_descartadas}")
