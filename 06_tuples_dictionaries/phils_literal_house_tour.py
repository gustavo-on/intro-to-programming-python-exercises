# Diálogo inicial
print(
    "Phil, querido... Você tem certeza que essa música é literalmente sobre... casas?"
)
print(
    "A própria Sabrina disse que nada na música é uma metáfora! Além disso, o sobrenome dela é carpinteira, acho que ela tem lugar de fala…\n"
)
print("Catálogo concluído! Quem será que irá comprar uma casa de Phil?\n")


catalogo_phil = {}  # Dicionário com o catálogo de casas do Phil

# Recebimento de dados/catálogo do Phil:
n = int(input())  # Número de propriedades a serem cadastradas
for propriedades in range(n):  # Para cada propriedade...
    str_info = input()  # Recebe a string com as informações da propriedade
    bairro, endereco, quartos, preco = str_info.split(
        "-"
    )  # Divide as informações da string
    bairro, endereco, quartos, preco = (
        bairro.strip(),
        endereco.strip(),
        int(quartos.strip()),
        int(preco.strip()),
    )  # Converte os tipos de dados e remove espaços extras
    catalogo_phil[endereco] = {
        "bairro": bairro,
        "quartos": quartos,
        "preco": preco,
    }  # Adiciona a propriedade ao catálogo

total_vendas = 0

# Loop de Atendimento:
nome_cliente = input()  # Recebe o nome do cliente
while nome_cliente != "FIM":  # Enquanto houver clientes...
    quartos_min, orcamento_max = input().split(
        "-"
    )  # Recebe os requisitos da cliente e divide
    quartos_min, orcamento_max = int(quartos_min), int(
        orcamento_max
    )  # Converte os tipos de dados dos requisitos
    tupla_cliente = (
        quartos_min,
        orcamento_max,
    )  # Cria uma tupla com os requisitos do cliente
    # Variáveis para armazenar a melhor opção
    maior_score = -1
    melhor_endereco = ""
    melhor_bairro = ""
    melhor_quartos = 0
    melhor_preco = 0

    # Percorrer o catálogo:
    for endereco, info in catalogo_phil.items():  # Para cada propriedade no catálogo...
        # Se o nº de quartos e o preço estiverem dentro dos requisitos, então a casa é uma opção
        if info["quartos"] >= quartos_min and info["preco"] <= orcamento_max:
            score_atual = info["quartos"] * 10  # Calcula o score da casa
            # Se o score atual for maior que o maior score até agora...
            if score_atual > maior_score:
                maior_score = score_atual  # Atualiza o maior score
                melhor_endereco, melhor_bairro, melhor_quartos, melhor_preco = (
                    endereco,
                    info["bairro"],
                    info["quartos"],
                    info["preco"],
                )  # Atualiza as informações da melhor casa

    if (
        maior_score == -1
    ):  # Se não houver nenhuma casa que atenda aos requisitos... (Nenhuma fez pontos)
        print(
            f"Puxa, {nome_cliente}, vou te avisar se algo aparecer. Não tenho nada com esses requisitos.\n"
        )
    else:  # Caso contrário... (Teve pelo menos uma casa que fez pontos)
        print(f"🎤 Bem-vindo ao House Tour de {melhor_bairro}, {nome_cliente}!")
        print(f"➡ Casa: {melhor_endereco}")
        print(f"💖 Score: {maior_score} pontos\n")

        # Reações das Clientes:
        if maior_score >= 40:
            if nome_cliente == "Sabrina Carpenter":
                print(
                    '"Uau, Phil! Acho que finalmente encontrei o cenário perfeito para o clipe de House Tour!"'
                )
            elif nome_cliente == "Taylor Swift":
                print('"Essa casa é perfeita para passar as férias na praia!"')
            else:
                print(
                    f'"{nome_cliente} ficou encantado(a)! Phil comemora mais uma venda de sucesso!"'
                )
        else:
            if nome_cliente == "Sabrina Carpenter":
                print('"Hmm... Sabe Phil, a letra não era tão literal assim…"')
            elif nome_cliente == "Taylor Swift":
                print('"Nós nunca vamos comprar essa casa juntos, Phil!"')
            else:
                print('"Parece que a música não ajudou nas vendas dessa vez…"')
        print()
        # Mensagens de Resultado Final:
        if maior_score >= 40:
            total_vendas += 1
            print('Venda concluída! Phil dança triunfante ao som de "House Tour"!\n')
        else:
            print("Talvez a Sabrina realmente não estivesse falando de imóveis…\n")
    nome_cliente = input()
# Relatório Final de Vendas:
print("===== RELATÓRIO DE VENDAS =====")
print(f"Total de casas vendidas: {total_vendas}")
print("===============================")
