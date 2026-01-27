# Funções de Ataque
def ataque(vida_atual, tipo_ataque):
    if tipo_ataque == "Você não tem o que é necessário para escalar.":
        print("Eu nunca vou conseguir chegar ao topo :(")
        return vida_atual - 20
    elif (
        tipo_ataque
        == "NÓS NUNCA DEVERÍAMOS TER SAÍDO DE CASA! VAMOS MORRER NESSA MONTANHA!"
    ):
        print("NAAÃO EU NUNCA DEVERIA TER INVENTADO DE ESCALAR ESSA MONTANHA!")
        return vida_atual - 50


# Funções de Reação:
def reacao(vida_atual, tipo_reacao):
    if tipo_reacao == "Calma Badeline, nós vamos conseguir.":
        return vida_atual + 25
    elif tipo_reacao == "Eu sei que somos capazes! Vamos em frente!":
        numero_respiracoes = int(input())
        return vida_atual + 10 * numero_respiracoes
    elif tipo_reacao == "Madeline, nós estamos com você. Continue!":
        return vida_atual + 60


vida_madeline = 100
while vida_madeline > 0 and vida_madeline < 150:
    ataque_badeline = input()
    vida_madeline = ataque(vida_madeline, ataque_badeline)
    if vida_madeline > 0 and vida_madeline < 150:
        reacao_madeline = input()
        vida_madeline = reacao(vida_madeline, reacao_madeline)

if vida_madeline >= 150:
    print(
        "Madeline chegou ao topo! Ela se senta em um banco para descansar e apreciar a vista."
    )
elif vida_madeline <= 0:
    print(
        "Madeline e Badeline não conseguiram se entender... parece que elas nunca vão ver a cidade de cima."
    )
