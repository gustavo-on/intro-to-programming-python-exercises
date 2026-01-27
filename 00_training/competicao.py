"""
Questão: Competição de Minecraft

Enunciado:
Arthur, Luiz e Pedro estão em uma competição para ver quem minera mais diamantes em um tempo H.
O programa deve calcular o total de diamantes de cada um (taxa * tempo) e imprimir o maior valor obtido.
A restrição é não utilizar estruturas condicionais (if/else) nem funções de máximo nativas.
Deve-se utilizar a fórmula matemática: x = (a + b + |a - b|) / 2 para encontrar o maior valor.

Entrada:
- A (int): Quantidade de diamantes por hora de Arthur.
- L (int): Quantidade de diamantes por hora de Luiz.
- P (int): Quantidade de diamantes por hora de Pedro.
- H (int): Duração da competição em horas.

Saída:
- M (int): O valor máximo de diamantes obtido por um dos participantes.
"""

A = int(input())
L = int(input())
P = int(input())
H = int(input())

# Cálculo do total de diamantes de cada um
TA = A * H
TL = L * H
TP = P * H

# Encontrando o maior entre Arthur e Luiz usando a fórmula
# (a + b + |a - b|) / 2
AL = (TA + TL + abs(TA - TL)) // 2

# Encontrando o maior entre o vencedor anterior e Pedro
Maior = (AL + TP + abs(AL - TP)) // 2

print(Maior)
