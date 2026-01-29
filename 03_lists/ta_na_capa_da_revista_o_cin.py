"""
Título: Tá na Capa da Revista: O CIn!!!

Resumo do problema:
Simula o controle de acesso a um desfile de gala do CIn, processando a entrada de pessoas na passarela.
Cada entrada pode ser um monitor oficial, um patrocinador (invasão tolerada) ou um intruso comum
(invasão não tolerada), com regras específicas de substituição por monitores disponíveis e eventos
especiais após um número determinado de invasões.

Lógica principal / Regras de aprovação:
- Monitores oficiais sempre entram normalmente.
- O patrocinador associado à marca do evento entra como invasão tolerada e não conta como invasão.
- Intrusos comuns geram invasão não tolerada e devem ser substituídos por um monitor disponível,
  respeitando ordem alfabética e uso único.
- Caso não haja monitor disponível, o intruso entra sem substituição.
- Após a terceira invasão não tolerada, o desfilante especial "Core" é inserido imediatamente.
- Ao final, são exibidas mensagens especiais caso certas subcelebridades tenham aparecido como intrusas.

Entradas:
- Um inteiro representando o número total de pessoas que tentarão entrar no desfile.
- Uma string com a marca do patrocinador.
- N strings, cada uma representando o nome de um desfilante.

Saídas:
- Mensagens informando o início do desfile.
- Mensagens de invasão (tolerada ou não).
- Listagem ordenada dos desfilantes que efetivamente entraram, com numeração.
- Mensagens especiais finais, caso subcelebridades específicas tenham aparecido.
"""

monitores_oficiais = [
    "Adrieli Queiroz",
    "Arthur Jorge",
    "César Cavalcanti",
    "Elisson Oliveira",
    "Filipe Moreira",
    "Gabriela Alves",
    "Joab Henrique",
    "Maria Fernanda",
    "Miriam Gonzaga",
    "Sofia Remindes",
]

# Variáveis de controle do estado global do desfile
contador_invasoes = 0  # Conta apenas invasões não toleradas
core_adicionado = False  # Garante que o Core seja inserido apenas uma vez
posicao_desfilante = 1  # Numeração sequencial dos desfilantes exibidos

desfile_final = []  # Armazena quem efetivamente entrou no desfile
subs_desfilantes = []  # Registra intrusos especiais para mensagens finais
nomes_input = []  # Guarda todas as entradas recebidas para validações posteriores

# Output inicial obrigatório
print("Senhoras e senhores, o desfile de gala do CIn vai começar!")

# Leitura dos dados iniciais do problema
numeros_desfilantes = int(input())
marca_do_patrocinador = input()

# Associação entre marca patrocinadora e o nome da subcelebridade tolerada
patrocinador_nome = ""
if marca_do_patrocinador == "Tha Beauty":
    patrocinador_nome = "Thais Linares"
elif marca_do_patrocinador == "DeGuê?":
    patrocinador_nome = "Davi Brito"
elif marca_do_patrocinador == "Diva Depressão":
    patrocinador_nome = "Edu e Fih"

# Leitura de todos os nomes de desfilantes
for i in range(numeros_desfilantes):
    nomes_input.append(input())

# Construção da lista inicial de monitores disponíveis para substituição
monitores_disponiveis = []
for monitor in monitores_oficiais:
    # Apenas monitores que não aparecem em nenhuma entrada podem ser usados como substitutos
    if monitor not in nomes_input:
        monitores_disponiveis.append(monitor)
        monitores_disponiveis.sort()  # Mantém a ordem alfabética exigida pelo enunciado

# Processamento sequencial do desfile
for desfilante in nomes_input:
    if desfilante in monitores_oficiais:
        # Entrada direta de monitor oficial, sem qualquer restrição
        desfile_final.append(desfilante)
        print(f"Desfilante de n° {posicao_desfilante}: {desfilante}!")
        posicao_desfilante += 1

    elif desfilante == patrocinador_nome:
        # Invasão tolerada por patrocínio: não incrementa o contador de invasões
        print("Invasão tolerada por motivos de patrocínio!")
        desfile_final.append(desfilante)
        print(f"Desfilante de n° {posicao_desfilante}: {desfilante}!")
        posicao_desfilante += 1

    else:
        # Invasão não tolerada: deve gerar substituição ou entrada forçada
        contador_invasoes += 1
        print(f"{desfilante} invadiu a passarela! Segurem ele(a), produção!")

        # Registro de intrusos especiais para mensagens finais
        if (
            desfilante == "Gretchen"
            or desfilante == "Tulla Luana"
            or desfilante == "Inês Brasil"
        ):
            subs_desfilantes.append(desfilante)

        if len(monitores_disponiveis) > 0:
            # Substituição ocorre apenas se ainda houver monitores elegíveis
            monitor_substituto = monitores_disponiveis.pop(0)
            desfile_final.append(monitor_substituto)
            print(f"Desfilante de n° {posicao_desfilante}: {monitor_substituto}!")
            posicao_desfilante += 1
        else:
            # Caso extremo: nenhum monitor disponível, o intruso entra mesmo assim
            desfile_final.append(desfilante)
            print(
                f"Desfilante de n° {posicao_desfilante}: {desfilante}?! Pelo visto não havia como substituir..."
            )
            posicao_desfilante += 1

        # Inserção do Core após exatamente três invasões não toleradas
        if contador_invasoes == 3 and not core_adicionado:
            print(
                "Muitas invasões estão deixando a galera irritada... Chama o Core pra acalmar os ânimos!"
            )
            desfile_final.append("Core")
            print(f"Desfilante de n° {posicao_desfilante}: Core!")
            posicao_desfilante += 1
            core_adicionado = True

# Mensagens finais condicionais à presença de subcelebridades específicas
if len(subs_desfilantes) > 0:
    print("Nas arquibancadas do CIn, sussurros indignados agitam a multidão...")
    for intruso in subs_desfilantes:
        if intruso == "Gretchen":
            print(
                '"Eles tem que respeitar os meus 37 anos de carreira! Eu hoje sou um ícone, se eu morrer hoje eu vou continuar sendo a Gretchen!"'
            )
        elif intruso == "Tulla Luana":
            print(
                '"Ninguém ser humano está acima de mim! Mas eu estou acima de muitos... é assim que eu penso."'
            )
        elif intruso == "Inês Brasil":
            print('"É aquele ditado... Vamo fazer o quê?"')
