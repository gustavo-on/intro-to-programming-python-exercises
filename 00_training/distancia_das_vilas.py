X = int(input())
Z = int(input())
DH = (X - 34)**2 + (Z - 220)**2
H = DH**0.5
DK = (X - 0)**2 + (Z - 0)**2
K = DK**0.5
DS = (X - 140)**2 + (Z - 456)**2
S = DS**0.5
print(f"Distancia para Hogsmeade: {H:.2f}")
print(f"Distancia para Kakariko: {K:.2f}")
print(f"Distancia para Solitude: {S:.2f}")