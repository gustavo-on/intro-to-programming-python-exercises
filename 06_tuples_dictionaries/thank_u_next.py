"""
Título: Thank U, Next!

Resumo do problema:
O programa implementa um sistema de controle de estoque de mimos exigidos por Ariana Grande
em seu camarim. As exigências iniciais representam um saldo devedor, que deve ser abatido
conforme os itens chegam no reabastecimento. Ao final, é gerado um relatório detalhado do
status de cada categoria, checagens críticas específicas e um veredito final da diva.

Regras de aprovação / lógica principal:
- As exigências iniciais são armazenadas em um dicionário, onde cada categoria mapeia para
  uma tupla (item_principal, saldo_devedor).
- Para a categoria "Bebidas" com item "latte", a exigência inicial é incrementada em 1,
  garantindo um latte extra.
- Durante o reabastecimento, apenas categorias existentes são consideradas, abatendo-se
  a quantidade recebida do saldo devedor.
- Saldo final maior que zero indica estoque negativo (faltou mimo).
- Saldo final menor ou igual a zero indica pedido atendido ou excedente.
- O veredito final depende da quantidade de categorias que permaneceram com saldo negativo.

Entradas:
- Fase 1: Strings no formato "Categoria: Item: Quantidade" até a entrada "MIMOS RECEBIDOS".
- Fase 2: Strings descrevendo reabastecimentos até "ACABOU, a Glinda está pronta!".

Saídas:
- Relatório de balanço final com o status de cada categoria.
- Mensagens específicas para itens críticos (Gloss e latte).
- Veredito final indicando aprovação ou demissão da equipe.
"""

# Fase 1: As exigências de Ariana
dicio_exigencias = {}  # Dicionário que armazena o saldo devedor por categoria
exigencias = input()
while (
    exigencias != "MIMOS RECEBIDOS"
):  # Decisão: encerra a leitura das exigências iniciais
    categoria, item, quantidade = exigencias.split(": ")
    quantidade = int(quantidade)
    # Decisão: regra especial para garantir um latte extra na categoria Bebidas
    if categoria == "Bebidas" and item == "latte":
        quantidade = quantidade + 1
    dicio_exigencias[categoria] = (item, quantidade)
    exigencias = input()

# Fase 2: O Reabastecimento
frase_reabastecimento = input()
while (
    frase_reabastecimento != "ACABOU, a Glinda está pronta!"
):  # Decisão: encerra o reabastecimento
    frase = frase_reabastecimento.split()
    quantidade = int(frase[1])
    categoria = frase[5]
    item = frase[7][:-1]
    frase_reabastecimento = input()

    atual = dicio_exigencias.get(categoria)  # Decisão: só abate se a categoria existir
    if atual:
        item_original, quantidade_original = atual
        # Cálculo: abatimento do saldo devedor subtraindo o que chegou do que ainda faltava
        novo_saldo = quantidade_original - quantidade
        dicio_exigencias[categoria] = (item_original, novo_saldo)

# Output. Relatório de Balanço Final:
print("Relatório de Balanço Final:")

for categoria, (item, quantidade) in dicio_exigencias.items():
    # Decisão: saldo menor ou igual a zero indica pedido atendido ou excedente
    if quantidade <= 0:
        print(
            f"Categoria: {categoria} Item: {item} Status: Você entregou TUDO! O mimo tá mais que garantido."
        )
    # Decisão: saldo maior que zero indica estoque negativo
    else:
        print(
            f"Categoria: {categoria} Item: {item} Status: Golpe BAIXÍSSIMO! Faltam {quantidade} mimos. Corre!"
        )
print()

# Checagens específicas
# Decisão: só verifica maquiagem se a categoria existir
if "Maquiagem" in dicio_exigencias:
    if dicio_exigencias["Maquiagem"][0] == "Gloss":
        # Decisão: avalia se o saldo do Gloss foi totalmente abatido
        if dicio_exigencias["Maquiagem"][1] <= 0:
            print("TUDO! O Gloss tá on. O look de Glinda tá salvo!")
        else:
            print("CADÊ meu gloss? Como divarei? ... A Glinda tá chorando de raiva!")

# Decisão: só verifica bebidas se a categoria existir
if "Bebidas" in dicio_exigencias:
    if dicio_exigencias["Bebidas"][0] == "latte":
        # Decisão: avalia se o saldo do latte foi totalmente abatido
        if dicio_exigencias["Bebidas"][1] <= 0:
            print(
                "Latte gelado pronto! A voz de Glinda está salva. Pode vir o próximo take"
            )
        else:
            print("Cadeia neles! Faltou o Mimo Sagrado. Essa equipe tá perdida!")

# Veredito Final
print()
print("Veredito Final")
contador = 0  # Contador de categorias com saldo devedor positivo
for categoria, (item, quantidade) in dicio_exigencias.items():
    # Decisão: saldo maior que zero indica estoque negativo
    if quantidade > 0:
        contador += 1

# Decisão final baseada no número de categorias em falta
if contador >= 3:
    print("Thank U, Next! A equipe de camarim foi demitida!")
else:
    print("Estoque Aprovado! Glinda vai brilhar em Wicked!")
