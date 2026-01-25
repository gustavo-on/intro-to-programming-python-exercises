# D = dias construindo
# C = Casas construidas
# T = ticks por casa

D = int(input())
C = int(input())
ticks_1 = D * 24000 * 3
ticks_2 = ticks_1 * 3
ticks = ticks_2 // 2
T = ticks // C
print(T)
