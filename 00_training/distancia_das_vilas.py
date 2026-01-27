"""
Questão: Distância das vilas

Enunciado:
O programa deve calcular a distância euclidiana entre a posição atual de Tantan (X, Z) e três vilas no mapa do Minecraft.
A altura (Y) é desconsiderada para o cálculo da distância, focando apenas no plano XZ.
A fórmula utilizada é: D = sqrt((X1 - X2)² + (Z1 - Z2)²).

Coordenadas das Vilas (X, Z):
- Hogsmeade: (34, 220)
- Kakariko: (0, 0)
- Solitude: (140, 456)

Entrada:
- X (int): Coordenada X atual.
- Z (int): Coordenada Z atual.

Saída:
- Três linhas indicando a distância para cada vila, formatadas com duas casas decimais.
"""

X = int(input())
Z = int(input())

# Cálculo da distância para Hogsmeade (34, 220)
DH = (X - 34) ** 2 + (Z - 220) ** 2
H = DH**0.5

# Cálculo da distância para Kakariko (0, 0)
DK = (X - 0) ** 2 + (Z - 0) ** 2
K = DK**0.5

# Cálculo da distância para Solitude (140, 456)
DS = (X - 140) ** 2 + (Z - 456) ** 2
S = DS**0.5

print(f"Distancia para Hogsmeade: {H:.2f}")
print(f"Distancia para Kakariko: {K:.2f}")
print(f"Distancia para Solitude: {S:.2f}")
