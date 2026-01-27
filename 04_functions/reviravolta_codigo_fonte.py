def checar_modificacao(hora_modificacao, hora_da_morte):
    if hora_modificacao > hora_da_morte:
        return True
    else:
        return False


def verificar_digital(lista_digitais, nome):
    if nome in lista_digitais:
        return True
    else:
        return False


# Cabeçalho de abertura da sessão:
print("TRIBUNAL EM SESSÃO")
print("Juiz: Que comece o julgamento do caso em pauta.")
print()
# Diálogos iniciais dos advogados:
print("Promotor Edgeworth: A promotoria está pronta, Meritíssimo.")
print(
    "Phoenix Wright: (Lá vamos nós... A reputação do escritório está em jogo.) A defesa está pronta."
)
print()
# Cena da sala de visitas:
print("--- SALA DE VISITAS DO TRIBUNAL ---")
print(
    "João Guilherme: Sr. Wright, eu juro, eu não o matei! Eu estive lá, mas... é só isso!"
)
print(
    "Phoenix Wright: (Eu sinto que ele está escondendo algo... Devo pressioná-lo por mais detalhes ou confiar no que ele me disse?)"
)
print()
escolha_inicial = input()

# Julgamento prossegue com a apresentação das evidências:
print("--- DE VOLTA AO TRIBUNAL ---")
print("Juiz: Promotoria, apresente as evidências.")
print("Promotor Edgeworth: A promotoria acusa este homem pelo crime de assassinato...")
print("Promotor Edgeworth: ...João Guilherme!")
print(
    "Promotor Edgeworth: Comecemos com a evidência virtual chave, o registro da última modificação no computador da vítima."
)
hora_modificacao = int(input())  # Hora da modificação do arquivo
print("Promotor Edgeworth: E, de acordo com o legista, a hora exata da morte.")
hora_da_morte = int(input())  # Hora da morte
print(
    "Promotor Edgeworth: Finalmente, a prova irrefutável. O relatório de digitais da arma do crime, o troféu."
)
numero_de_digitais = int(input())  # Número de digitais encontradas na arma
print("Promotor Edgeworth: Que o escrivão leia os nomes encontrados na arma...")
lista_digitais = []
for i in range(numero_de_digitais):  # Loop para coletar as digitais
    lista_digitais.append(input())
print()

# Cabeçalho dos argumentos finais:
print("ARGUMENTOS FINAIS")
print()

# Bifurcação principal:
houve_contradicao_temporal = checar_modificacao(
    hora_modificacao, hora_da_morte
)  # Checa se houve contradição temporal
elisson_na_lista = verificar_digital(
    lista_digitais, "Elisson"
)  # Checa se Elisson está na lista de digitais
joao_na_lista = verificar_digital(
    lista_digitais, "João Guilherme"
)  # Checa se João está na lista de digitais
veredito = "INOCENTE"  # Flag para definir o veredito
elisson_confessou = False  # Flag para definir se Elisson confessou

if escolha_inicial == "pressionar":  # Se a escolha for "pressionar"
    # Flashback com a confissão de João:
    print("--- FLASHBACK: SALA DE VISITAS ---")
    print(
        "Phoenix Wright: HOLD IT! João, não é só isso! Eu não posso te defender se você não me contar tudo. O que realmente aconteceu naquela noite?"
    )
    print(
        "João Guilherme: (soluço)... Certo... Eu vou contar. Não era sobre a rixa... era sobre o 'Ticket Fantasma'."
    )
    print(
        "João Guilherme: Um bug impossível no sistema da faculdade. Eu criei um código que o resolvia. Era a minha chance de conseguir o estágio dos sonhos."
    )
    print(
        "João Guilherme: Eu... eu confiei em Arthur. Mostrei o código a ele para uma revisão. E ele... ele o roubou. Apresentou como se fosse dele, levou todo o crédito."
    )
    print(
        "João Guilherme: E o pior, Sr. Wright... eu cometi o erro de comentar sobre meu progresso com o Elisson, o 'monitor do povo'. Ele era o único, além de mim e de Arthur, que sabia da história toda. Ele observava nossa agilidade com os tickets com um sentimento sombrio! Se houver dedo dele nisso, ele certamente tentará depôr para contar do roubo do meu código por Arthur para me incriminar!"
    )
    print("--- FIM DO FLASHBACK ---")
    print()

    # Argumento inicial da promotoria e objeção da defesa:
    print(
        "Promotor Edgeworth: A lógica é simples. O acusado tinha o motivo, suas digitais estão na arma, e a perícia mostra que o arquivo do 'Ticket Fantasma' foi modificado após a morte, provando que ele permaneceu na cena do crime!"
    )
    print("Phoenix Wright: OBJEÇÃO!")
    print()

    # Sub-bifurcação:
    if houve_contradicao_temporal:  # Se houver contradição temporal:
        # Diálogo da reviravolta do álibi:
        print(
            "Phoenix Wright: A sua lógica tem uma falha fatal, promotor! É impossível que meu cliente tenha modificado aquele arquivo!"
        )
        print(
            "Phoenix Wright: Pois a defesa pode provar que, no exato momento da modificação, João Guilherme estava a quilômetros de distância, comprando um café na 'Cafeteria Byte'! Temos o registro da transação e uma testemunha ocular!"
        )
        print(
            "Phoenix Wright: A contradição temporal, combinada com este álibi, prova apenas uma coisa: a existência de uma terceira pessoa na cena do crime!"
        )
        if not elisson_na_lista:
            print()
        elif elisson_na_lista:  # Se elisson estiver na lista de digitais:
            print(
                "Phoenix Wright: Se meu cliente tem um álibi, quem poderia ser? Quem alteraria o arquivo do 'Ticket Fantasma' para incriminar João Guilherme?"
            )
            print(
                "Phoenix Wright: Só poderia ser alguém que conhecia a história... alguém que meu cliente confessou ter contado!"
            )
            print(
                "Phoenix Wright: A defesa descobriu que apenas UMA outra pessoa sabia da história do código... uma pessoa cujas digitais, convenientemente, também estão na arma do crime!"
            )
            print(
                "Phoenix Wright: A pessoa que matou Arthur Sean para eliminar um rival e incriminar o outro foi você..."
            )
            print("Phoenix Wright: ELISSON!!!")
            print()
            print(
                "Elisson: N-NÃÃÃÃÃOOOOO! COMO... ELE TE CONTOU?! MEU PLANO ERA PERFEITO!"
            )
            print()
            elisson_confessou = True
    # SENÃO, SE as digitais de João não estiverem na lista:
    elif not joao_na_lista:
        # Diálogo da falta de provas:
        print(
            "Phoenix Wright: A promotoria não pode sequer provar que meu cliente tocou na arma do crime! Não há digitais dele!"
        )
        print()
    else:
        print(
            "Phoenix Wright: (Droga... As digitais estão na arma e a linha do tempo da promotoria é sólida... Não tenho objeções...)"
        )
        veredito = "CULPADO"
        print()
else:  # Escolha foi confiar
    # Reflexão de Phoenix:
    print(
        "(Voz da Consciência de Phoenix: Eu confiei em João... mas agora, essa 'hora da modificação' não faz sentido para mim. Não tenho como usar essa evidência!)"
    )
    print()
    # Argumento inicial da promotoria e objeção da defesa:
    print(
        "Promotor Edgeworth: A lógica é simples. O acusado tinha o motivo, e suas digitais estão na arma. O caso está encerrado."
    )
    print("Phoenix Wright: OBJEÇÃO!")
    print()
    # Sub-bifurcação:
    # Se as digitais de João não estiverem na arma:
    if not joao_na_lista:
        print(
            "Phoenix Wright: A promotoria não pode provar que meu cliente tocou na arma do crime! Não há digitais dele!"
        )
        print()
    else:
        print(
            "Phoenix Wright: (Droga... As digitais estão na arma e a linha do tempo da promotoria é sólida... Estou sem argumentos!)"
        )
        print()
        veredito = "CULPADO"

#
print("Juiz: ...Compreendo. Após analisar todas as evidências e os argumentos...")
print(f"Juiz: O veredito para o caso de João Guilherme é: {veredito}!")
print()
if veredito == "INOCENTE":  # Se o veredito for "INOCENTE"
    if elisson_confessou:  # Se Elisson confessou
        print(
            "Juiz: Que esta corte jamais esqueça o dia em que a verdade foi revelada contra todas as probabilidades."
        )
    print("A reputação do escritório Fey & Co. continua impecável.")
else:
    print("Edgeworth... Você ainda não venceu o debate final.")
