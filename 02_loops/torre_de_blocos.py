# ALTURA DA TORRE:
altura_torre = int(input())
andar = "#"
soma = "##"
numero_andar = 1
espaco = "⠀"

for i in range(altura_torre):
    espaco_andar = altura_torre - numero_andar
    espaco_total = espaco * espaco_andar

    print(espaco + espaco_total + andar)
    numero_andar = numero_andar + 1
    andar = andar + soma
