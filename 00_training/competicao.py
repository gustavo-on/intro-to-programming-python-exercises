A = int(input())
L = int(input())
P = int(input())
H = int(input())

TA = A * H
TL = L * H
TP = P * H

AL = (TA + TL + abs(TA - TL)) // 2
Maior = (AL + TP + abs(AL - TP)) // 2

print(Maior)
