"""
Título: Phil's Literal House Tour

Resumo do problema:
O programa simula um sistema de catálogo e atendimento imobiliário de Phil Dunphy.
As propriedades são armazenadas em um dicionário, e para cada cliente o sistema
filtra as casas que atendem aos requisitos mínimos, calcula um score de compatibilidade
e seleciona a melhor opção disponível.

Regras de aprovação / lógica principal:
- As propriedades são cadastradas em um dicionário indexado pelo endereço.
- Cada cliente informa requisitos mínimos (quartos e orçamento máximo), armazenados em uma tupla.
- Apenas casas que atendem simultaneamente aos dois critérios são consideradas válidas.
- O score é calculado exclusivamente com base no número de quartos.
- A casa escolhida é a de maior score; em caso de empate, prevalece a primeira encontrada.
- Uma venda ocorre apenas se o score final for maior ou igual a 40.
- O atendimento continua até o nome da cliente ser "FIM", quando o relatório final é exibido.

Entradas:
- Um inteiro N indicando o número de propriedades.
- Para cada propriedade: bairro, endereço e par quartos-preço.
- Para cada cliente: nome e requisitos no formato quartos_min-orcamento_max.

Saídas:
- Diálogos iniciais e mensagens de atendimento.
- Informações da melhor casa encontrada ou aviso de inexistência de opções.
- Reações personalizadas das clientes.
- Relatório final com o total de vendas realizadas.
"""

# Diálogo inicial
print(
    "Phil, querido... Você tem certeza que essa música é literalmente sobre... casas?"
)
print(
    "A própria Sabrina disse que nada na música é uma metáfora! Além disso, o sobrenome dela é carpinteira, acho que ela tem lugar de fala…\n"
)
print("Catálogo concluído! Quem será que irá comprar uma casa de Phil?\n")


catalogo_phil = {}  # Dicionário principal que armazena todas as propriedades

# Recebimento de dados / catálogo do Phil
n = int(input())  # Quantidade de propriedades a serem cadastradas
for propriedades in range(n):
    str_info = input()
    bairro, endereco, quartos, preco = str_info.split("-")
    bairro, endereco, quartos, preco = (
        bairro.strip(),
        endereco.strip(),
        int(quartos.strip()),
        int(preco.strip()),
    )
    catalogo_phil[endereco] = {
        "bairro": bairro,
        "quartos": quartos,
        "preco": preco,
    }

total_vendas = 0  # Contador de vendas concluídas

# Loop de Atendimento
nome_cliente = input()
while nome_cliente != "FIM":  # Decisão: encerra o atendimento ao receber "FIM"
    quartos_min, orcamento_max = input().split("-")
    quartos_min, orcamento_max = int(quartos_min), int(orcamento_max)
    tupla_cliente = (
        quartos_min,
        orcamento_max,
    )  # Tupla garante imutabilidade dos requisitos do cliente

    # Variáveis de controle da melhor casa encontrada
    maior_score = -1
    melhor_endereco = ""
    melhor_bairro = ""
    melhor_quartos = 0
    melhor_preco = 0

    # Percorrer todo o catálogo para filtrar e avaliar casas
    for endereco, info in catalogo_phil.items():
        # Decisão: casa só é válida se atender simultaneamente quartos e orçamento
        if info["quartos"] >= quartos_min and info["preco"] <= orcamento_max:
            score_atual = info["quartos"] * 10  # Cálculo do score de compatibilidade
            # Decisão: mantém apenas a casa com maior score encontrado até o momento
            if score_atual > maior_score:
                maior_score = score_atual
                melhor_endereco, melhor_bairro, melhor_quartos, melhor_preco = (
                    endereco,
                    info["bairro"],
                    info["quartos"],
                    info["preco"],
                )

    # Decisão: nenhum score válido indica ausência de casas compatíveis
    if maior_score == -1:
        print(
            f"Puxa, {nome_cliente}, vou te avisar se algo aparecer. Não tenho nada com esses requisitos.\n"
        )
    else:
        print(f"🎤 Bem-vindo ao House Tour de {melhor_bairro}, {nome_cliente}!")
        print(f"➡ Casa: {melhor_endereco}")
        print(f"💖 Score: {maior_score} pontos\n")

        # Reações das Clientes
        if maior_score >= 40:  # Decisão: score suficiente para agradar a cliente
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

        # Mensagens de Resultado Final
        if maior_score >= 40:  # Decisão: apenas scores altos contam como venda
            total_vendas += 1
            print('Venda concluída! Phil dança triunfante ao som de "House Tour"!\n')
        else:
            print("Talvez a Sabrina realmente não estivesse falando de imóveis…\n")

    nome_cliente = input()

# Relatório Final de Vendas
print("===== RELATÓRIO DE VENDAS =====")
print(f"Total de casas vendidas: {total_vendas}")
print("===============================")
