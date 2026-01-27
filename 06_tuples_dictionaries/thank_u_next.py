# Fase 1: As exigências de Ariana
dicio_exigencias = {}  # Dicionário vazio para armazenar as exigências
exigencias = input()
while exigencias != "MIMOS RECEBIDOS":  # Enquanto não for a frase de parada...
    categoria, item, quantidade = exigencias.split(
        ": "
    )  # Separa a string em categoria, item e quantidade
    quantidade = int(quantidade)  # Converte a quantidade para inteiro
    if (
        categoria == "Bebidas" and item == "latte"
    ):  # Se a categoria for Bebidas e o item for latte, adiciona mais um latte
        quantidade = quantidade + 1
    dicio_exigencias[categoria] = (
        item,
        quantidade,
    )  # Adiciona a categoria, item e quantidade ao dicionário
    exigencias = input()

# Fase 2: O Reabastecimento
frase_reabastecimento = input()
while (
    frase_reabastecimento != "ACABOU, a Glinda está pronta!"
):  # Enquanto o input não for a frase de parada...
    frase = frase_reabastecimento.split()  # Separa a string em uma lista de strings
    # Cria variáveis para armazenar a quantidade, categoria e item
    quantidade = int(frase[1])
    categoria = frase[5]
    item = frase[7][:-1]
    frase_reabastecimento = input()
    atual = dicio_exigencias.get(
        categoria
    )  # Verifica se a categoria já existe no dicionário
    if atual:  # Se a categoria já existir...
        item_original, quantidade_original = (
            atual  # Atribui o item e a quantidade original da categoria
        )
        novo_saldo = (
            quantidade_original - quantidade
        )  # Calcula o novo saldo da categoria subtraindo a quantidade original pela quantidade recebida
        dicio_exigencias[categoria] = (
            item_original,
            novo_saldo,
        )  # Atualiza o dicionário com o novo saldo

# Output. Relatório de Balanço Final:
print("Relatório de Balanço Final:")

for categoria, (
    item,
    quantidade,
) in (
    dicio_exigencias.items()
):  # Para cada categoria, item e quantidade no dicionário...
    # Se a quantidade for menor ou igual a zero...
    if quantidade <= 0:
        print(
            f"Categoria: {categoria} Item: {item} Status: Você entregou TUDO! O mimo tá mais que garantido."
        )
    # Caso contrário... (se a quantidade for maior que zero))
    else:
        print(
            f"Categoria: {categoria} Item: {item} Status: Golpe BAIXÍSSIMO! Faltam {quantidade} mimos. Corre!"
        )
print()

# Checagens específicas
# Se a categoria "Maquiagem" existir no dicionário...
if "Maquiagem" in dicio_exigencias:
    # Se o item da categoria "Maquiagem" for "Gloss"...
    if dicio_exigencias["Maquiagem"][0] == "Gloss":
        # Se a quantidade do item "Gloss" for menor ou igual a zero, sucesso.
        if dicio_exigencias["Maquiagem"][1] <= 0:
            print("TUDO! O Gloss tá on. O look de Glinda tá salvo!")
        # Caso contrário (se a quantidade for maior que zero), falha.
        else:
            print("CADÊ meu gloss? Como divarei? ... A Glinda tá chorando de raiva!")
# Se a categoria "Bebidas" existir no dicionário...
if "Bebidas" in dicio_exigencias:
    # Se o item da categoria "Bebidas" for "latte"
    if dicio_exigencias["Bebidas"][0] == "latte":
        # Se a quantidade do item "latte" for menor ou igual a zero, sucesso.
        if dicio_exigencias["Bebidas"][1] <= 0:
            print(
                "Latte gelado pronto! A voz de Glinda está salva. Pode vir o próximo take"
            )
        # Caso contrário (se a quantidade for maior que zero), falha.
        else:
            print("Cadeia neles! Faltou o Mimo Sagrado. Essa equipe tá perdida!")

# Veredito Final
print()
print("Veredito Final")
contador = 0  # Variável para contar quantas categorias estão com saldo negativo
# Para cada categoria, item e quantidade no dicionário...
for categoria, (item, quantidade) in dicio_exigencias.items():
    # Se a quantidade for maior que zero, ou seja, se a categoria não estiver com saldo negativo...
    if quantidade > 0:
        contador += 1  # Adiciona 1 ao contador
# Se o contador for maior ou igual a 3...
if contador >= 3:
    print("Thank U, Next! A equipe de camarim foi demitida!")
# Caso contrário (se o contador for menor que 3)...
else:
    print("Estoque Aprovado! Glinda vai brilhar em Wicked!")
