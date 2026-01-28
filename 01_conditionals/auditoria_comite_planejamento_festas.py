"""
Questão: A Auditoria do Comitê de Planejamento de Festas (CPF)

Enunciado:
O programa deve auditar as despesas do comitê com base em regras hierárquicas.
1. Regra de Ouro (Angela): Gastos > 100 são reprovados (exceto se for a Angela).
2. Regras do Michael:
   - "Mágica" ou "Fantasia" são reprovados.
   - Gastos > 60 geram ressalvas (com mensagens específicas para Natal/Aniversário).
   - Outros gastos são aprovados (suspeitos).
3. Regras por Evento:
   - Halloween: Regras específicas para "Abóbora" e outros itens.
   - Aniversário: Regras específicas para "Bolo" e "Sorvete...".
4. Regra Geral: Baseada apenas no valor (> 50 com ressalvas, senão aprovado).

Entrada:
- Nome do Item, Valor, Responsável, Tipo de Evento.

Saída:
- Status da compra (Aprovada, Reprovada, Ressalvas).
- Comentário da Angela.
"""

# Inicialização de variáveis para segurança (evitar erro de "variável não definida")
analise = ""
mensagem = ""

# Inputs
nomeitemx = input()
valoritem = float(input())
respcomprax = input()
eventox = input()

# Tratamento de Strings (Padronização)
evento = eventox.capitalize()
respcompra = respcomprax.capitalize()
# O capitalize garante que "abóbora" vire "Abóbora" e "mágica" vire "Mágica"
nomeitem = nomeitemx.capitalize()

# Constantes de Status
aprovado = "Compra Aprovada!"
reprovado = "Compra Reprovada!"
ressalvas = "Compra Aprovada com ressalvas!"

# --- LÓGICA DE AUDITORIA ---

# 1. REGRAS DA ANGELA (REGRA DE OURO)
# Verifica primeiro o valor teto de $100
if (valoritem > 100) and respcompra != "Angela":
    analise = reprovado
    mensagem = "Gasto excessivo e irresponsável! Onde está a disciplina fiscal?!"
elif (valoritem > 100) and respcompra == "Angela":
    analise = aprovado
    mensagem = "Apenas eu tenho discernimento para gastos desta magnitude."
elif (valoritem <= 100) and respcompra == "Angela":
    analise = aprovado
    mensagem = "Compra feita por mim, obviamente dentro dos padrões de excelência."

# 2. REGRAS PARA MICHAEL SCOTT
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
    # Obs: Se for Michael, >60 e outro evento (ex: Halloween), a mensagem mantém-se vazia
    # ou cai na regra geral se a lógica permitisse, mas aqui o elif já capturou.
elif respcompra == "Michael":
    analise = aprovado
    mensagem = "Uma compra surpreendentemente sensata vinda do Michael. Suspeito."

# 3. REGRAS POR TIPO DE EVENTO
# Halloween
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

# Aniversário
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

# 4. DEMAIS EVENTOS OU FUNCIONÁRIOS (REGRA GERAL)
elif valoritem > 50:
    analise = ressalvas
    mensagem = "Está dentro do orçamento, mas não quer dizer que não vou verificar!"
else:
    analise = aprovado
    mensagem = "Esta compra não viola nenhum regulamento... por enquanto."

# OUTPUT FINAL
print(analise)
print(mensagem)
