"""
Questão: Doação de Ferro

Enunciado:
Tantan tem P packs de ferro e quer distribuir igualmente entre suas 3 vilas:
Hogsmeade, Kakariko e Solitude.
O que sobrar dessa divisão igualitária será descartado.
O programa deve calcular quanto cada vila recebe e quanto sobra.

Entrada:
- P (int): Quantidade total de packs de ferro.

Saída:
- V (int): Quantidade de packs para cada vila.
- F (int): Quantidade de packs que sobraram (resto).
"""

P = int(input())

# Divisão inteira (quantos packs cada vila recebe)
V = P // 3

# Resto da divisão (quanto sobra para ser jogado fora)
F = P % 3

print(V)
print(F)
