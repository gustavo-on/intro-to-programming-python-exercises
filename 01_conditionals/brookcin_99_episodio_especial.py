# input
casos = int(input())
dias = int(input())
assistencias = int(input())
operacoes_em_campo = int(input())
operacao_especial = input()
tipo_operacao = ""
if operacao_especial == "sim":
    tipo_operacao = input()
local = input()

pontuacao = (casos * 2) + (assistencias * 1.5) + (operacoes_em_campo * 0.5)


if operacao_especial == "sim":
    if tipo_operacao == "Infiltração":
        aumento = 1.5
    elif tipo_operacao == "Escuta":
        aumento = 1.3
    elif tipo_operacao == "Invasão":
        aumento = 1.2
    else:
        aumento = 1.1
else:
    aumento = 1.0

if dias > 0:
    casos_dia = casos / dias

else:
    casos_dia = 0

pontuacao_final = pontuacao * aumento

if local != "Manhattan" and local != "Brooklyn":
    print(
        "Os casos não são nas áreas designadas por Holt. Peralta está desclassificado!"
    )
else:
    print("Pelo menos nos bairros corretos Jake está!")
    if casos < 20:
        print("Vishh, Jake já foi eliminado por não ter o mínimo de casos necessários.")
    else:
        print(
            "Detetive Peralta bateu o mínimo de casos, ele ainda está dentro da competição."
        )
        if casos_dia < 0.5:
            print(
                "A média diária de casos tá muito baixa, Peralta foi desclassificado."
            )
        else:
            print("Parece que Jake é bem consistente na sua média diária de casos.")
            if assistencias < 5:
                print("Desclassificado! Jake precisa ajudar mais os companheiros.")
            else:
                print(
                    "Peralta ajudou bastante outros detetives, ele ainda está na competição!"
                )
                if operacoes_em_campo < 20:
                    print(
                        "Peralta precisa sair mais da delegacia, está faltando ação em campo!"
                    )
                else:
                    print(
                        "Jake ainda sobrevive por sua participação em campo, será que ele vai levar pra casa o prêmio?"
                    )
                    if operacao_especial == "sim":
                        print(
                            "Minha nossa! Jake Peralta é realmente um detetive diferenciado."
                        )
                    else:
                        print(
                            "Para que operação especial quando se tem números, não é?"
                        )
                    if pontuacao_final >= 70:
                        print(
                            "Jake é candidato forte ao prêmio. Será que Holt vai premiá-lo?"
                        )
                    elif pontuacao_final >= 40:
                        print(
                            "Muito bem! Mas ainda é incerto se vai ser suficiente para ganhar o prêmio."
                        )
                    else:
                        print("Muito difícil de Jake ganhar o prêmio.")
