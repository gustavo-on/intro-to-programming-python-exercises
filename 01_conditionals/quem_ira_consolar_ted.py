print("Ted se iludiu de novo. Esse é o momento que ele mais precisa dos amigos dele…")
print("Quantos dos amigos dele conseguirão ajudar dessa vez?")
nome1 = ""
nome2 = ""
nome3 = ""
nome4 = ""
quantidade_pessoas = int(input())
quant_total_cervejas = ""
quant_media_cervejas = ""
# SOZINHO
# FAÇA A PARTE QUE ELE VAI SOZINHO
if quantidade_pessoas == 0:
    quant_total_cervejas = int(input())
    print("\nRelatório da situação de Ted:")
    print("Ted foi para o MacLaren’s… Olhe em volta, Ted, você está sozinho.")
    print(f"- Quantidade de cervejas bebidas por Ted: {quant_total_cervejas} cervejas.")

else:
    print("Hora da lista dos amigos da vez!")
    # MENSAGENS
    mensagem_barney = "Barney foi voluntário dessa vez. Tenho certeza que ele vai conseguir transformar toda essa tristeza de Ted em um rolê Legen… espera por isso… DÁRIO."
    mensagem_robin = "Trompa azul na área! A repórter mais amada do Metro News 1 vai tentar ajudar. Tomara que ele não fique mais iludido ainda."
    mensagem_marshall = "O melhor amigo de Ted com certeza estaria com ele em um momento tão difícil. Marshall realmente sabe o valor da irmandade."
    mensagem_lily = "Lily adora fazer o papel da irmã mais velha. Com certeza ela irá consolar ele, mas só depois de dizer “Eu avisei”."
    mensagem_outro = "vai encarar essa com Ted. Às vezes a gente encontra apoio de quem menos espera."

    # NOMES AMIGOS
    if quantidade_pessoas >= 1:
        nome1 = input()
        if nome1 == "Barney":
            print(mensagem_barney)
        elif nome1 == "Robin":
            print(mensagem_robin)
        elif nome1 == "Marshall":
            print(mensagem_marshall)
        elif nome1 == "Lily":
            print(mensagem_lily)
        else:
            print(f"{nome1} {mensagem_outro}")
    if quantidade_pessoas >= 2:
        nome2 = input()
        if nome2 == "Barney":
            print(mensagem_barney)
        elif nome2 == "Robin":
            print(mensagem_robin)
        elif nome2 == "Marshall":
            print(mensagem_marshall)
        elif nome2 == "Lily":
            print(mensagem_lily)
        else:
            print(f"{nome2} {mensagem_outro}")
    if quantidade_pessoas >= 3:
        nome3 = input()
        if nome3 == "Barney":
            print(mensagem_barney)
        elif nome3 == "Robin":
            print(mensagem_robin)
        elif nome3 == "Marshall":
            print(mensagem_marshall)
        elif nome3 == "Lily":
            print(mensagem_lily)
        else:
            print(f"{nome3} {mensagem_outro}")
    if quantidade_pessoas == 4:
        nome4 = input()
        if nome4 == "Barney":
            print(mensagem_barney)
        elif nome4 == "Robin":
            print(mensagem_robin)
        elif nome4 == "Marshall":
            print(mensagem_marshall)
        elif nome4 == "Lily":
            print(mensagem_lily)
        else:
            print(f"{nome4} {mensagem_outro}")

    # DUPLAS E GRUPOS
    if quantidade_pessoas == 2:
        if (nome1 == "Marshall" and nome2 == "Lily") or (
            nome2 == "Marshall" and nome1 == "Lily"
        ):
            print("Nada melhor que um casal para dar conselhos de relacionamento.")

        elif (nome1 == "Barney" and nome2 == "Marshall") or (
            nome2 == "Barney" and nome1 == "Marshall"
        ):
            print(
                "Sem dúvida os melhores amigos de Ted. Mas tomara que Barney não queira implicar com Marshall sobre quem realmente é o melhor amigo dele."
            )
    if quantidade_pessoas == 4 and (
        (
            nome1 == "Barney"
            or nome2 == "Barney"
            or nome3 == "Barney"
            or nome4 == "Barney"
        )
        and (
            nome1 == "Robin" or nome2 == "Robin" or nome3 == "Robin" or nome4 == "Robin"
        )
        and (
            nome1 == "Marshall"
            or nome2 == "Marshall"
            or nome3 == "Marshall"
            or nome4 == "Marshall"
        )
        and (nome1 == "Lily" or nome2 == "Lily" or nome3 == "Lily" or nome4 == "Lily")
    ):
        print(
            "O quinteto estará reunido nessa jornada! É o momento perfeito pra brincar de “Você conhece o Ted?”."
        )

    # LUGARES
    lugar = input()

    laser_barney = "Com certeza a Arena de Laser Tag foi escolhida por influência de Barney. Se arrume Ted, é hora de botar um terno, tomar um whisky e partir pra diversão."

    if lugar == "Arena de Laser Tag":
        if quantidade_pessoas == 1 and nome1 == "Barney":
            print(laser_barney)
        elif quantidade_pessoas == 2 and (nome1 == "Barney" or nome2 == "Barney"):
            print(laser_barney)
        elif quantidade_pessoas == 3 and (
            nome1 == "Barney" or nome2 == "Barney" or nome3 == "Barney"
        ):
            print(laser_barney)
        elif quantidade_pessoas == 4 and (
            nome1 == "Barney"
            or nome2 == "Barney"
            or nome3 == "Barney"
            or nome4 == "Barney"
        ):
            print(laser_barney)

    if quantidade_pessoas == 1 and nome1 == "Robin" and lugar == "Carmichael’s":
        print(
            "Acho que Ted e Robin vão sair em um date… Tomara que Ted não roube aquela trompa azul da parede de novo."
        )

    if lugar == "MacLaren’s Pub":
        if quantidade_pessoas == 1 and (
            nome1 == "Barney"
            or nome1 == "Marshall"
            or nome1 == "Robin"
            or nome1 == "Lily"
        ):
            print("Não tem erro, né? Estar no MacLaren’s é como estar em casa.")
        elif (
            quantidade_pessoas == 2
            and (
                nome1 == "Barney"
                or nome1 == "Marshall"
                or nome1 == "Robin"
                or nome1 == "Lily"
            )
            or (
                nome2 == "Barney"
                or nome2 == "Marshall"
                or nome2 == "Robin"
                or nome2 == "Lily"
            )
        ):
            print("Não tem erro, né? Estar no MacLaren’s é como estar em casa.")
        elif (
            quantidade_pessoas == 3
            and (
                nome1 == "Barney"
                or nome1 == "Marshall"
                or nome1 == "Robin"
                or nome1 == "Lily"
            )
            or (
                nome2 == "Barney"
                or nome2 == "Marshall"
                or nome2 == "Robin"
                or nome2 == "Lily"
            )
            or (
                nome3 == "Barney"
                or nome3 == "Marshall"
                or nome3 == "Robin"
                or nome3 == "Lily"
            )
        ):
            print("Não tem erro, né? Estar no MacLaren’s é como estar em casa.")
        elif (
            quantidade_pessoas == 4
            and (
                nome1 == "Barney"
                or nome1 == "Marshall"
                or nome1 == "Robin"
                or nome1 == "Lily"
            )
            or (
                nome2 == "Barney"
                or nome2 == "Marshall"
                or nome2 == "Robin"
                or nome2 == "Lily"
            )
            or (
                nome3 == "Barney"
                or nome3 == "Marshall"
                or nome3 == "Robin"
                or nome3 == "Lilly"
            )
            or (
                nome4 == "Barney"
                or nome4 == "Marshall"
                or nome4 == "Robin"
                or nome4 == "Lily"
            )
        ):
            print("Não tem erro, né? Estar no MacLaren’s é como estar em casa.")
        else:
            print(
                "Um lugar habitual, mas com uma galera diferente. Será estranho, mas Ted vai."
            )

    if lugar == "MacLaren’s Pub":
        quant_media_cervejas = int(input())

    # FRASES PRA QUANTIDADES DE PESSOAS
    if quantidade_pessoas == 1:
        frase = "Saideira de um pra um. Nada melhor do que uma pessoa pra ouvir seus problemas."
    elif quantidade_pessoas == 2:
        frase = "Duas pessoas se compadeceram com a situação do pobre Ted."
    elif quantidade_pessoas == 3:
        frase = "Três pessoas! Ted conseguiu se divertir bastante."
    else:
        if (
            (
                nome1 == "Barney"
                or nome1 == "Marshall"
                or nome1 == "Robin"
                or nome1 == "Lily"
            )
            and (
                nome2 == "Barney"
                or nome2 == "Marshall"
                or nome2 == "Robin"
                or nome2 == "Lily"
            )
            and (
                nome3 == "Barney"
                or nome3 == "Marshall"
                or nome3 == "Robin"
                or nome3 == "Lily"
            )
            and (
                nome4 == "Barney"
                or nome4 == "Marshall"
                or nome4 == "Robin"
                or nome4 == "Lily"
            )
        ):
            frase = "O quinteto junto consegue resolver qualquer problema!"
        else:
            frase = "Saiu um quinteto um pouco diferente do que a gente tá acostumado, mas no fim conseguiram deixar Ted alegre."

    if lugar == "MacLaren’s Pub":
        quant_total_cervejas = quant_media_cervejas * (quantidade_pessoas + 1)
    # RELATÓRIO FINAL:
    print("\nRelatório da situação de Ted:")
    if quantidade_pessoas == 1:
        print(f"- Ted foi consolado por: {nome1}.")
    elif quantidade_pessoas == 2:
        print(f"- Ted foi consolado por: {nome1} e {nome2}.")
    elif quantidade_pessoas == 3:
        print(f"- Ted foi consolado por: {nome1}, {nome2} e {nome3}.")
    else:
        print(f"- Ted foi consolado por: {nome1}, {nome2}, {nome3} e {nome4}.")
    print(f"- O local de afogar as mágoas foi: {lugar}.")
    print(f"- {frase}")
    if lugar == "MacLaren’s Pub":
        print(
            f"- Quantidade de cervejas bebidas pelo grupo: {quant_total_cervejas} cervejas."
        )
    print(
        "Pelo visto todo mundo já sabe como funciona a cabeça dele, né? Depois do rolê Ted conseguiu esfriar a cabeça e já tá pronto pra quebrar mais a cara. Quem será que serão os próximos a consolar o querido Ted Mosby?"
    )
