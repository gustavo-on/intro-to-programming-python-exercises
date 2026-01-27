def num_particoes(
    alvo, max
):  # Função recursiva que calcula o número de partições do número alvo (doces)
    # Caso base: se o alvo for 0, há apenas uma partição possível (vazia)
    if alvo == 0:
        return 1
    # Caso base: se o alvo for negativo ou o número máximo de doces for 0, não há partições possíveis
    elif alvo < 0 or max == 0:
        return 0
    # Passo recursivo
    else:
        return num_particoes(alvo, max - 1) + num_particoes(alvo - max, max)


# Inputs
doces = int(input())
particoes = num_particoes(doces, doces)

# Outputs
print("DOCES OU TRAVESSURAS???")
print(f"sem travessuras por hoje! tenho {particoes} sacolinhas pra vocês")
# Se o número de partições for ímpar...
if particoes % 2 == 1:
    print("hmm... número ímpar de sacolinhas 🍭 cuidado com as bruxas!")
# Caso contrário...
else:
    print("doces equilibrados, sem travessuras!")
