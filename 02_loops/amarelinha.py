"""
Questão: Amarelinha

Resumo:
O programa simula uma brincadeira de amarelinha entre quatro jogadores
(Ana, Adrieli, Joab e Duda). Cada jogador realiza um número fixo de tentativas,
e em cada tentativa é registrado o número da última casa alcançada.

Lógica principal:
- Cada jogador tenta atravessar as casas de 1 a 5.
- Se alcançar a casa 5, completa a amarelinha e para antes do limite máximo.
- Caso contrário, continua até atingir o número máximo de tentativas.
- Ao final, verifica-se quem completou a amarelinha e determina-se o vencedor
ou se houve empate.

Entradas:
- Um inteiro representando o número máximo de tentativas por jogador.
- Para cada jogador, uma sequência de inteiros (1 a 5) indicando a última casa
alcançada em cada tentativa.

Saídas:
- Quantidade de tentativas realizadas por cada jogador.
- Última casa alcançada.
- Mensagem indicando se completou ou não a amarelinha.
- Resultado final: vencedor único ou empate.
"""

tentativas = int(input())  # número máximo de tentativas permitidas por jogador

# Variáveis de controle de tentativas e estado de execução de cada jogador
tent_ana = 0
ana = True
tent_adrieli = 0
adrieli = True
tent_joab = 0
joab = True
tent_duda = 0
duda = True

# Contador total de vencedores
vencedor = 0

# Flags para identificar quem completou a amarelinha
ana_venceu = False
adrieli_venceu = False
joab_venceu = False
duda_venceu = False

# ---------- ANA ----------
while ana:
    n_ana = int(input())  # última casa alcançada na tentativa atual
    tent_ana = tent_ana + 1

    # Interrompe se completar a amarelinha ou atingir o limite de tentativas
    if n_ana == 5 or tent_ana == tentativas:
        ana = False

print(f"Ana tentou {tent_ana} vezes e completou a última casa {n_ana}")
if n_ana == 5:  # decisão baseada na conclusão da amarelinha
    print("Ana completou a amarelinha!")
    vencedor = vencedor + 1
    ana_venceu = True
else:
    print("Ana não conseguiu completar a amarelinha!")

# ---------- ADRIELI ----------
while adrieli:
    n_adrieli = int(input())
    tent_adrieli = tent_adrieli + 1

    # Interrompe ao completar ou ao esgotar tentativas
    if n_adrieli == 5 or tent_adrieli == tentativas:
        adrieli = False

print(f"Adrieli tentou {tent_adrieli} vezes e completou a última casa {n_adrieli}")
if n_adrieli == 5:
    print("Adrieli completou a amarelinha!")
    vencedor = vencedor + 1
    adrieli_venceu = True
else:
    print("Adrieli não conseguiu completar a amarelinha!")

# ---------- JOAB ----------
while joab:
    n_joab = int(input())
    tent_joab = tent_joab + 1

    # Controle de parada por sucesso ou limite
    if n_joab == 5 or tent_joab == tentativas:
        joab = False

print(f"Joab tentou {tent_joab} vezes e completou a última casa {n_joab}")
if n_joab == 5:
    print("Joab completou a amarelinha!")
    vencedor = vencedor + 1
    joab_venceu = True
else:
    print("Joab não conseguiu completar a amarelinha!")

# ---------- DUDA ----------
while duda:
    n_duda = int(input())
    tent_duda = tent_duda + 1

    # Encerramento por conclusão ou tentativas máximas
    if n_duda == 5 or tent_duda == tentativas:
        duda = False

print(f"Duda tentou {tent_duda} vezes e completou a última casa {n_duda}")
if n_duda == 5:
    print("Duda completou a amarelinha!")
    vencedor = vencedor + 1
    duda_venceu = True
else:
    print("Duda não conseguiu completar a amarelinha!")

# ---------- RESULTADO FINAL ----------
if vencedor == 1:
    # Apenas um jogador venceu
    if ana_venceu:
        print("O vencedor é Ana!")
    elif adrieli_venceu:
        print("O vencedor é Adrieli!")
    elif joab_venceu:
        print("O vencedor é Joab!")
    else:
        print("O vencedor é Duda!")
else:
    # Dois ou mais vencedores configuram empate
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
