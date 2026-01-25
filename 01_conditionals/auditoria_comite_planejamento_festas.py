nomeitemx = input()
valoritem = float(input())
respcomprax = input()
eventox = input()

evento = eventox.capitalize()
respcompra = respcomprax.capitalize()
nomeitem = nomeitemx.capitalize()

aprovado = "Compra Aprovada!"
reprovado = "Compra Reprovada!"
ressalvas = "Compra Aprovada com ressalvas!"

# REGRAS DA ANGELA:
if (valoritem > 100) and respcompra != "Angela":
    analise = reprovado
    mensagem = "Gasto excessivo e irresponsável! Onde está a disciplina fiscal?!"
elif (valoritem > 100) and respcompra == "Angela":
    analise = aprovado
    mensagem = "Apenas eu tenho discernimento para gastos desta magnitude."
elif (valoritem <= 100) and respcompra == "Angela":
    analise = aprovado
    mensagem = "Compra feita por mim, obviamente dentro dos padrões de excelência."

# REGRAS PARA MICHAEL SCOTT:
elif (respcompra == "Michael") and (nomeitem == "Mágica" or nomeitem == "Fantasia"):
    analise = reprovado
    mensagem = "O Comitê não financia frivolidades e palhaçadas, Michael."
elif respcompra == "Michael" and (valoritem > 60):
    analise = ressalvas
    if evento == "Natal":
        mensagem = (
            "O espírito natalino de Michael é... excessivo. A nota será conferida."
        )
    elif evento == "Aniversário":
        mensagem = "Michael nunca gasta tanto nos aniversários dos funcionários, deve ser o dele!"
elif respcompra == "Michael":
    analise = aprovado
    mensagem = "Uma compra surpreendentemente sensata vinda do Michael. Suspeito."

# REGRAS POR TIPO DE EVENTO:
# HALLOWEEN
elif evento == "Halloween":
    if (nomeitem == "Abóbora") and valoritem <= 30:
        analise = aprovado
        mensagem = "Uma abóbora de tamanho e custo razoáveis. Eficiente."
    elif (nomeitem == "Abóbora") and valoritem > 30:
        analise = ressalvas
        mensagem = "Por que uma abóbora precisa ser tão cara? Extravagância."
    else:
        analise = ressalvas
        mensagem = (
            "Decoração de Halloween... Tenho certeza que Phyllis exagerou de novo."
        )

# ANIVERSÁRIO
elif evento == "Aniversário":
    if (nomeitem == "Bolo") and valoritem <= 40:
        analise = aprovado
        mensagem = (
            "Um bolo modesto para celebrar mais um ano de produtividade, parabéns!"
        )
    elif nomeitem == "Sorvete de menta com chocolate":
        analise = reprovado
        mensagem = "Este sabor de sorvete é uma abominação e não entrará em meu evento."
    else:
        analise = aprovado
        mensagem = (
            "Itens de aniversário devem ser práticos, não uma distração do trabalho."
        )

# DEMAIS EVENTOS OU FUNCIONÁRIOS
elif valoritem > 50:
    analise = ressalvas
    mensagem = "Está dentro do orçamento, mas não quer dizer que não vou verificar!"
else:
    analise = aprovado
    mensagem = "Esta compra não viola nenhum regulamento... por enquanto."

# OUTPUT:
print(analise)
print(mensagem)
