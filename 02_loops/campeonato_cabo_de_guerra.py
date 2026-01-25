print("Começa agora o treinamento para grande final mundial de cabo de guerra!")

# Escolhendo a quantidade de rodadas
# Quantidade de partidas ímpar
qnt_partidas = int(input())
while qnt_partidas % 2 == 0:
    print("Não deverá haver empates! O número de partidas deverá ser ímpar.")
    qnt_partidas = int(input())
print(f"Eles batalharão em {qnt_partidas} longas partidas.")

# Partidas
partidas_joao = 0
partidas_arthur = 0

# Forças de Arthur e João
forca_arthur = int(input())
forca_joao = int(input())
while forca_arthur == forca_joao:
    forca_arthur = int(input())
    forca_joao = int(input())
resistencia = int(input())

# MAIS FORTE E MAIS FRACO
if forca_arthur > forca_joao:
    mais_forte = "Arthur"
    mais_fraco = "João"
else:
    mais_forte = "João"
    mais_fraco = "Arthur"

numero_determinante = 0

# Loop de partidas
partida_atual = 1
while partida_atual <= qnt_partidas:
    # Início da partida
    print(f"Começa a {partida_atual}ª partida!")
    print(f"Placar geral: {partidas_arthur} X {partidas_joao}")

    # resistências
    resistencia_arthur = resistencia
    resistencia_joao = resistencia

    # Partida
    while resistencia_arthur > 0 and resistencia_joao > 0:
        numero_determinante = int(input())

        # SE FOR QUADRADO PERFEITO
        if numero_determinante**0.5 == int(numero_determinante**0.5):
            print("O número é um quadrado perfeito! Arthur consegue puxar mais forte.")
            resistencia_arthur += 1
            resistencia_joao -= 1

        else:
            # SE FOR PRIMO
            divisores = 0
            for i in range(1, numero_determinante + 1):
                if numero_determinante % i == 0:
                    divisores += 1
            if divisores == 2:
                print("O primo do primo é primo do primo? João puxa mais forte!")
                resistencia_arthur -= 1
                resistencia_joao += 1
            else:
                print(
                    f"{mais_forte} é o mais forte! {mais_fraco} não consegue segurar."
                )
                if mais_forte == "Arthur":
                    resistencia_arthur += 1
                    resistencia_joao -= 1
                else:
                    resistencia_joao += 1
                    resistencia_arthur -= 1

    # FIM DA PARTIDA
    if resistencia_arthur <= 0:
        print("João usa seus talentos de mangueboy e leva essa para casa!")
        partidas_joao += 1
    else:
        print("Arthur dá orgulho para Maceió e ganha a partida!")
        partidas_arthur += 1

    # Verificação sem chance de virada
    if (partidas_arthur == (qnt_partidas // 2) + 1) or (
        partidas_joao == (qnt_partidas // 2) + 1
    ):
        partida_atual = qnt_partidas
    partida_atual += 1

# FIM DE TODAS PARTIDAS
print("\nAgora eles estão prontos para o mundial!")
print(f"Placar final: {partidas_arthur} X {partidas_joao}")

# Ganhador final
if partidas_arthur > partidas_joao:
    nome_ganhador = "Arthur"
    nome_perdedor = "João"
else:
    nome_ganhador = "João"
    nome_perdedor = "Arthur"

# Se o perdedor tiver 0 vitórias
if min(partidas_arthur, partidas_joao) <= 0:
    print(f"{nome_perdedor} não teve chance! {nome_ganhador} venceu todas as partidas.")
else:
    print(
        f"O ganhador foi {nome_ganhador} com uma diferença de {abs(partidas_arthur - partidas_joao)} partidas."
    )
