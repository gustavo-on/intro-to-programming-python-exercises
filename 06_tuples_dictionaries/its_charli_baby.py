print("Don't sleep, don't eat, just do it on repeat! Keep bumpin' that!!!\n")

# Dicionário de atos com nome, gêneros permitidos e duração máxima
dicionario_atos = {
    1: ("Abertura", ("Hyperpop", "Pop"), 600),
    2: ("Sentimental", ("Sentimental", "Ballad"), 480),
    3: ("Encerramento", ("Hyperpop", "Banger"), 720),
}

setlist_final = {1: [], 2: [], 3: []}  # Dicionário de setlist final

num_aprovadas = 0  # Contador de músicas aprovadas
num_descartadas = 0  # Contador de músicas descartadas
ato_atual = 1  # Ato atual
duracao_total_ato = 0  # Duração total do ato atual
primeira_iteracao_ato = True  # Flag para primeira iteração do ato
fim_do_show = False  # Flag para fim do show


def converte_para_segundos(string):  # Função para converter string de tempo em segundos
    partes = string.split(":")  # Divide a string em minutos e segundos
    minutos = int(partes[0])  # Converte minutos para inteiro
    segundos = int(partes[1])  # Converte segundos para inteiro
    total_segundos = (minutos * 60) + segundos  # Calcula o total de segundos e retorna
    return total_segundos


def analise_musica(
    entrada, ato_atual, duracao_total, aprovadas, descartadas, setlist
):  # Função para analisar a música
    nova_duracao = duracao_total  # Inicializa a nova duração com a duração total atual
    novas_aprovadas = aprovadas  # Inicializa o contador de músicas aprovadas
    novas_descartadas = descartadas  # Inicializa o contador de músicas descartadas

    partes_musica = entrada.split(
        ","
    )  # Divide a entrada em partes (nome, gênero, duração)
    # Extrai o nome, gênero e duração da música e remove espaços em branco
    nome_musica = partes_musica[0].strip()
    genero_musica = partes_musica[1].strip()
    duracao_str = partes_musica[2].strip()
    print(f"Música em análise: {nome_musica}")
    musica_aprovada_para_ato = True  # Flag para música aprovada para o ato
    if nome_musica == "Actually Romantic":  # Se a música for "Acutally Romantic"...
        print(
            "Já não basta ter exposto a Charli nessa música, agora a Taylor quer que a própria cante? GOLPE BAIXÍSSIMO!!!"
        )
        novas_descartadas += 1  # Incrementa o contador de músicas descartadas
        musica_aprovada_para_ato = False  # Define a flag como False
    elif (
        nome_musica == "Talk Talk featuring troye sivan"
    ):  # Caso contrário, se a música for "Talk Talk featuring Troye Sivan"...
        print(
            "A MAIOR AMIZADE DO POP NO PALCO? Talk to them in your own made-up language!"
        )
    elif (
        nome_musica == "Von dutch a. g. cook remix featuring addison rae"
    ):  # Caso contrário, se a música for "Von Dutch A.G. Cook Remix featuring Addison Rae"...
        print(
            "‘CAUSE THEY’RE JUST LIVING THAT LIFE! Addison Rae, a maior revelação do pop desde Britney Spears, no palco ao lado da sua amiga Charli XCX!"
        )
    elif (
        nome_musica == "Guess featuring billie eilish"
    ):  # Caso contrário, se a música for "Guess featuring Billie Eilish"...
        print("Hey, Billie, you there?")
    if musica_aprovada_para_ato:  # Se a música foi aprovada para o ato...
        generos_permitidos = dicionario_atos[ato_atual][
            1
        ]  # Obtém os gêneros permitidos para o ato atual
        if (
            genero_musica not in generos_permitidos
        ):  # Se o gênero da música não estiver entre os gêneros permitidos...
            print(
                "Gênero errado para esse ato! Cuidado, uma música deslocada mata a vibe de um show…"
            )
            novas_descartadas += 1  # Incrementa o contador de músicas descartadas
            musica_aprovada_para_ato = False
    if musica_aprovada_para_ato:  # Se a música foi aprovada para o ato...
        duracao_musica_seg = converte_para_segundos(
            duracao_str
        )  # Converte a duração da música para segundos
        limite_segundos_ato = dicionario_atos[ato_atual][
            2
        ]  # Obtém o limite de segundos para o ato atual
        if (
            nova_duracao + duracao_musica_seg
        ) > limite_segundos_ato:  # Se a duração total do ato mais a duração da música for maior que o limite de segundos para o ato...
            print(
                f"Muito longa! O Ato {ato_atual} já está com {nova_duracao} segundos e essa música tem {duracao_musica_seg} segundos."
            )
            novas_descartadas += 1  # Incrementa o contador de músicas descartadas
            musica_aprovada_para_ato = False
    if musica_aprovada_para_ato:  # Se a música foi aprovada para o ato...
        duracao_musica_seg = converte_para_segundos(
            duracao_str
        )  # Converte a duração da música para segundos
        dados_musica = (
            nome_musica,
            genero_musica,
            duracao_musica_seg,
        )  # Cria uma tupla com os dados da música
        setlist[ato_atual].append(
            dados_musica
        )  # Adiciona a tupla à lista de setlist do ato atual
        nova_duracao += duracao_musica_seg  # Incrementa a duração total do ato com a duração da música
        novas_aprovadas += 1  # Incrementa o contador de músicas aprovadas
        print(f"{nome_musica} adicionada ao Ato {ato_atual} ;).")
    return (
        nova_duracao,
        novas_aprovadas,
        novas_descartadas,
    )  # Retorna a nova duração total, o contador de músicas aprovadas e o contador de músicas descartadas


# Enquanto não for o fim do show... (loop principal)
while not fim_do_show:
    entrada = input()  # Lê a entrada do usuário
    if entrada == "FIM_SHOW":  # Se a entrada for "FIM_SHOW"...
        fim_do_show = True
        print()
    elif entrada == "FIM_ATO_1":  # Se a entrada for "FIM_ATO_1"...
        print()
        ato_atual = 2  # Define o ato atual como 2
        duracao_total_ato = 0  # Zera a duração total do ato
        primeira_iteracao_ato = (
            True  # Define a flag de primeira iteração do ato como True
        )
    elif entrada == "FIM_ATO_2":  # Se a entrada for "FIM_ATO_2"...
        print()
        ato_atual = 3  # Define o ato atual como 3
        duracao_total_ato = 0  # Zera a duração total do ato
        primeira_iteracao_ato = (
            True  # Define a flag de primeira iteração do ato como True
        )
    else:  # Caso contrário...
        if primeira_iteracao_ato:  # Se for a primeira iteração do ato...
            config_ato = dicionario_atos[ato_atual]  # Obtém a configuração do ato atual
            # Obtém os gêneros permitidos para o ato atual
            genero_1 = config_ato[1][0]
            genero_2 = config_ato[1][1]
            print(f"Iniciando montagem do Ato {ato_atual} ({genero_1} e {genero_2}):\n")
            primeira_iteracao_ato = (
                False  # Define a flag de primeira iteração do ato como False
            )
        duracao_total_ato, num_aprovadas, num_descartadas = analise_musica(
            entrada,
            ato_atual,
            duracao_total_ato,
            num_aprovadas,
            num_descartadas,
            setlist_final,
        )  # Chama a função para analisar a música

# Relatório final
avisos_doces_backstage = False  # Flag para avisos de doces no backstage
for num_ato in range(1, 4):  # Para cada ato...
    limites_segundos = dicionario_atos[num_ato][
        2
    ]  # Obtém o limite de segundos para o ato atual
    lista_musicas = setlist_final[num_ato]  # Obtém a lista de músicas do ato atual
    duracao_total = 0  # Inicializa a duração total do ato com 0
    for musica in lista_musicas:  # Para cada música na lista de músicas do ato atual...
        duracao_total += musica[
            2
        ]  # Incrementa a duração total do ato com a duração da música
    limite_70 = (
        limites_segundos * 0.7
    )  # Calcula 70% do limite de segundos para o ato atual
    if (
        duracao_total < limite_70
    ):  # Se a duração total do ato for menor que 70% do limite de segundos para o ato atual...
        avisos_doces_backstage = (
            True  # Define a flag de avisos de doces no backstage como True
        )
if (
    avisos_doces_backstage
):  # Se a flag de avisos de doces no backstage for True, imprime a mensagem de aviso
    print(
        "Tem certeza que isso é um show? Rápido desse jeito, a Charli XCX deve estar pensando nos doces do backstage…\n"
    )
for num_ato in range(1, 4):  # Para cada ato...
    nome_ato = dicionario_atos[num_ato][0]  # Obtém o nome do ato atual
    lista_musicas = setlist_final[num_ato]  # Obtém a lista de músicas do ato atual

    print(f"--- Ato {num_ato} ({nome_ato}) ---")
    duracao_total_print = 0  # Inicializa a duração total do ato com 0
    if not lista_musicas:  # Se a lista de músicas do ato atual estiver vazia...
        print("Nenhuma música adicionada a este Ato.")
    else:  # Caso contrário...
        for (
            musica
        ) in lista_musicas:  # Para cada música na lista de músicas do ato atual...
            # Obtém o nome, gênero e duração da música e imprime os outputs
            nome = musica[0]
            genero = musica[1]
            tempo = musica[2]
            duracao_total_print += tempo
            print(f"{nome} ({genero})")
    print(f"Duração total do ato: {duracao_total_print} segundos.\n")
print("=== RESUMO DO SHOW (BRAT APPROVED) ===")
print(f"Total de músicas na setlist: {num_aprovadas}")
print(f"Total de músicas barradas: {num_descartadas}")
