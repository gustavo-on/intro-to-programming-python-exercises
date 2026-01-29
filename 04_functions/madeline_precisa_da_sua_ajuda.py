"""
Título: A Madeline precisa da sua ajuda!

Resumo do problema:
O programa simula o conflito interno de Madeline durante a escalada do Monte Celeste,
representado por ataques de Badeline e reações de Madeline. Cada interação altera a
vida da personagem, que começa em 100 pontos, e o programa encerra quando a vida
atinge 0 ou 150.

Regras de aprovação / Lógica principal:
- A vida inicial de Madeline é 100.
- Ataques de Badeline sempre reduzem a vida.
- Reações de Madeline ou incentivos dos amigos recuperam vida.
- O fluxo é sempre: ataque → reação, enquanto a vida estiver entre 0 e 150.
- Se a vida atingir 150, Madeline vence.
- Se a vida atingir 0 ou menos, Madeline falha.
- Caso a vida chegue a 0 após um ataque, nenhuma reação é solicitada.

Entradas:
- Strings representando ataques de Badeline.
- Strings representando reações de Madeline ou incentivo dos amigos.
- Um inteiro adicional quando a reação envolver respirações.

Saídas:
- Frases narrativas correspondentes aos ataques.
- Mensagem final indicando sucesso ou fracasso da escalada.
"""


# Funções de Ataque
def ataque(vida_atual, tipo_ataque):
    # Decisão: identifica qual ataque foi usado para aplicar a penalidade correta
    if tipo_ataque == "Você não tem o que é necessário para escalar.":
        print("Eu nunca vou conseguir chegar ao topo :(")
        # Cálculo: ataque de ansiedade reduz 20 pontos de vida
        return vida_atual - 20
    elif (
        tipo_ataque
        == "NÓS NUNCA DEVERÍAMOS TER SAÍDO DE CASA! VAMOS MORRER NESSA MONTANHA!"
    ):
        print("NAAÃO EU NUNCA DEVERIA TER INVENTADO DE ESCALAR ESSA MONTANHA!")
        # Cálculo: ataque de pânico reduz 50 pontos de vida
        return vida_atual - 50


# Funções de Reação:
def reacao(vida_atual, tipo_reacao):
    # Decisão: reação simples que recupera uma quantidade fixa de vida
    if tipo_reacao == "Calma Badeline, nós vamos conseguir.":
        return vida_atual + 25
    # Decisão: reação dependente de um valor adicional fornecido pelo usuário
    elif tipo_reacao == "Eu sei que somos capazes! Vamos em frente!":
        numero_respiracoes = int(input())
        # Cálculo: cada respiração recupera 10 pontos de vida
        return vida_atual + 10 * numero_respiracoes
    # Decisão: incentivo dos amigos concede um bônus fixo alto
    elif tipo_reacao == "Madeline, nós estamos com você. Continue!":
        return vida_atual + 60


vida_madeline = 100

# Decisão: o loop continua apenas enquanto a vida estiver dentro dos limites permitidos
while vida_madeline > 0 and vida_madeline < 150:
    ataque_badeline = input()
    vida_madeline = ataque(vida_madeline, ataque_badeline)

    # Decisão: só permite reação se Madeline ainda estiver viva e abaixo do limite máximo
    if vida_madeline > 0 and vida_madeline < 150:
        reacao_madeline = input()
        vida_madeline = reacao(vida_madeline, reacao_madeline)

# Decisão final: determina o desfecho da história com base no valor da vida
if vida_madeline >= 150:
    print(
        "Madeline chegou ao topo! Ela se senta em um banco para descansar e apreciar a vista."
    )
elif vida_madeline <= 0:
    print(
        "Madeline e Badeline não conseguiram se entender... parece que elas nunca vão ver a cidade de cima."
    )
