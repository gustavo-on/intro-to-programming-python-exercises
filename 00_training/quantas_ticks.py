"""
Questão: Quantas Ticks?

Enunciado:
O programa deve calcular quantos ticks (unidade de tempo do jogo) foram gastos para construir cada casa.
Sabe-se que:
1. Tantan joga 3 horas reais por dia.
2. 1 dia no jogo = 20 minutos reais = 24000 ticks.
3. 1 hora real = 3 dias no jogo.
4. Ele só constrói durante o dia (metade do dia do jogo, ou seja, 12000 ticks).

O cálculo segue a ordem: Dias Reais -> Horas Reais -> Dias de Jogo -> Ticks Totais -> Ticks Úteis (Dia) -> Ticks por Casa.

Entrada:
- D (int): Dias da vida real jogando.
- C (int): Quantidade total de casas construídas.

Saída:
- T (int): Quantidade de ticks gastos por casa.
"""

D = int(input())  # Dias na vida real
C = int(input())  # Quantidade de casas

# 1. Calcular horas reais jogadas (3 horas por dia)
horas_reais = D * 3

# 2. Converter horas reais em dias de jogo
# Se 20 min reais = 1 dia de jogo, então 60 min (1h) = 3 dias de jogo
dias_jogo = horas_reais * 3

# 3. Calcular ticks totais (1 dia de jogo = 24000 ticks)
total_ticks = dias_jogo * 24000

# 4. Calcular ticks úteis de construção
# Ele só constrói de dia, que é metade do tempo (dia + noite)
ticks_construcao = total_ticks // 2

# 5. Calcular ticks por casa
T = ticks_construcao // C

print(T)
