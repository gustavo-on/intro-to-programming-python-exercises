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

# Variáveis de controle
contador_invasoes = 0
core_adicionado = False
posicao_desfilante = 1

desfile_final = []  # Lista de desfilantes que realmente entraram no desfile
subs_desfilantes = []  # Lista de desfilantes que foram substituidos
nomes_input = []  # Lista de nomes colocados no input

# Output inicial
print("Senhoras e senhores, o desfile de gala do CIn vai começar!")

# Inputs iniciais
numeros_desfilantes = int(input())
marca_do_patrocinador = input()

# Relacionar marcas e patrocinadores
patrocinador_nome = ""
if marca_do_patrocinador == "Tha Beauty":
    patrocinador_nome = "Thais Linares"
elif marca_do_patrocinador == "DeGuê?":
    patrocinador_nome = "Davi Brito"
elif marca_do_patrocinador == "Diva Depressão":
    patrocinador_nome = "Edu e Fih"

# Nomes dos desfilantes
for i in range(numeros_desfilantes):
    nomes_input.append(input())

# Lista de monitores disponíveis
monitores_disponiveis = []
for monitor in monitores_oficiais:
    if (
        monitor not in nomes_input
    ):  # Se o monitor não estiver na lista de nomes colocados
        monitores_disponiveis.append(monitor)
        monitores_disponiveis.sort()

# Desfile
for desfilante in nomes_input:
    if desfilante in monitores_oficiais:
        desfile_final.append(desfilante)
        print(f"Desfilante de n° {posicao_desfilante}: {desfilante}!")
        posicao_desfilante += 1

    elif desfilante == patrocinador_nome:
        print("Invasão tolerada por motivos de patrocínio!")
        desfile_final.append(desfilante)
        print(f"Desfilante de n° {posicao_desfilante}: {desfilante}!")
        posicao_desfilante += 1

    else:
        contador_invasoes += 1
        print(f"{desfilante} invadiu a passarela! Segurem ele(a), produção!")
        if (
            desfilante == "Gretchen"
            or desfilante == "Tulla Luana"
            or desfilante == "Inês Brasil"
        ):
            subs_desfilantes.append(desfilante)

        if len(monitores_disponiveis) > 0:  # Se houver monitores disponíveis
            monitor_substituto = monitores_disponiveis.pop(0)
            desfile_final.append(monitor_substituto)
            print(f"Desfilante de n° {posicao_desfilante}: {monitor_substituto}!")
            posicao_desfilante += 1
        else:  # Se não houver monitores disponíveis
            desfile_final.append(desfilante)
            print(
                f"Desfilante de n° {posicao_desfilante}: {desfilante}?! Pelo visto não havia como substituir..."
            )
            posicao_desfilante += 1

        # Condição Core
        if contador_invasoes == 3 and not core_adicionado:
            print(
                "Muitas invasões estão deixando a galera irritada... Chama o Core pra acalmar os ânimos!"
            )
            desfile_final.append("Core")
            print(f"Desfilante de n° {posicao_desfilante}: Core!")
            posicao_desfilante += 1
            core_adicionado = True

# Output final
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
