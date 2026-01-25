# CADA UM DEVE PERCORRER TODAS CASAS NA ORDEM CORRETA (UMA CASA POR VEZ)
# Pode errar (perder o equilíbrio ou pisar fora da linha)
# Pulo = o avanço de uma casa
# Tentativa = uma rodada inteira em que o jogador tenta atravessar as casas, fazendo vários pulos até errar ou até completar a última casa (5)
# input é o último pulo bem sucedido da tentativa

# Registrar tentativas de cada jogador, e qual foi a última casa alcançada e quem conseguiu completar a amarelinha
tentativas = int(input())  # número de tentativas por jogador
tent_ana = 0
ana = True
tent_adrieli = 0
adrieli = True
tent_joab = 0
joab = True
tent_duda = 0
duda = True
vencedor = 0
ana_venceu = False
adrieli_venceu = False
joab_venceu = False
duda_venceu = False
anterior_ana = 0
anterior_adrieli = 0
anterior_joab = 0
anterior_duda = 0

while ana:
    n_ana = int(input())  # Ultima casa que parou
    tent_ana = tent_ana + 1
    anterior_ana = n_ana
    if n_ana == 5 or tent_ana == tentativas:
        ana = False

print(f"Ana tentou {tent_ana} vezes e completou a última casa {n_ana}")
if n_ana == 5:
    print("Ana completou a amarelinha!")
    vencedor = vencedor + 1
    ana_venceu = True
else:
    print("Ana não conseguiu completar a amarelinha!")


while adrieli:
    n_adrieli = int(input())
    tent_adrieli = tent_adrieli + 1
    anterior_adrieli = n_adrieli
    if n_adrieli == 5 or tent_adrieli == tentativas:
        adrieli = False
print(f"Adrieli tentou {tent_adrieli} vezes e completou a última casa {n_adrieli}")
if n_adrieli == 5:
    print("Adrieli completou a amarelinha!")
    vencedor = vencedor + 1
    adrieli_venceu = True
else:
    print("Adrieli não conseguiu completar a amarelinha!")

while joab:
    n_joab = int(input())
    tent_joab = tent_joab + 1
    anterior_joab = n_joab
    if n_joab == 5 or tent_joab == tentativas:
        joab = False
print(f"Joab tentou {tent_joab} vezes e completou a última casa {n_joab}")
if n_joab == 5:
    print("Joab completou a amarelinha!")
    vencedor = vencedor + 1
    joab_venceu = True
else:
    print("Joab não conseguiu completar a amarelinha!")

while duda:
    n_duda = int(input())
    tent_duda = tent_duda + 1
    anterior_duda = n_duda
    if n_duda == 5 or tent_duda == tentativas:
        duda = False
print(f"Duda tentou {tent_duda} vezes e completou a última casa {n_duda}")
if n_duda == 5:
    print("Duda completou a amarelinha!")
    vencedor = vencedor + 1
    duda_venceu = True
else:
    print("Duda não conseguiu completar a amarelinha!")

if vencedor == 1:
    if ana_venceu:
        print("O vencedor é Ana!")
    elif adrieli_venceu:
        print("O vencedor é Adrieli!")
    elif joab_venceu:
        print("O vencedor é Joab!")
    else:
        print("O vencedor é Duda!")

else:
    if vencedor == 2:
        if ana_venceu and adrieli_venceu:
            print("Houve empate entre: Ana, Adrieli")
        elif ana_venceu and joab_venceu:
            print("Houve empate entre: Ana, Joab")
        elif ana_venceu and duda_venceu:
            print("Houve empate entre: Ana, Duda")
        elif adrieli_venceu and joab_venceu:
            print("Houve empate entre: Adrieli, Joab")
        elif adrieli_venceu and duda_venceu:
            print("Houve empate entre: Adrieli, Duda")
        elif joab_venceu and duda_venceu:
            print("Houve empate entre: Joab, Duda")
    elif vencedor == 3:
        if not ana_venceu:
            print("Houve empate entre: Adrieli, Joab, Duda")
        elif not adrieli_venceu:
            print("Houve empate entre: Ana, Joab, Duda")
        elif not joab_venceu:
            print("Houve empate entre: Ana, Adrieli, Duda")
        else:
            print("Houve empate entre: Ana, Adrieli, Joab")
    else:
        print("Houve empate entre: Ana, Adrieli, Joab, Duda")
