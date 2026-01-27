"""
Questão: Tamanho da Caverna

Enunciado:
O programa deve calcular o volume total de uma caverna (quantidade de blocos a serem quebrados).
A caverna tem formato de prisma com base quadrada.
Recebe-se o tamanho do lado da base (L) e a altura (A).
O cálculo é: Volume = (L * L) * A.

Entrada:
- L (int): Tamanho do lado da base da caverna.
- A (int): Altura da caverna.

Saída:
- B (int): Número total de blocos (volume da caverna).
"""

# Recebe o lado e já eleva ao quadrado para obter a área da base
L = int(input()) ** 2
A = int(input())

# Calcula o volume total (Área da base * Altura)
volume = L * A
print(volume)
