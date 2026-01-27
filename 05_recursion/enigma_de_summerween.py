def decifrar(frase_restante, chave_atual, alfabeto_ref, indice_original, lista_traps):
    # Caso base: Quando a frase restante for vazia, retorna uma string vazia.
    if len(frase_restante) == 0:
        return ""
    # Passo recursivo:
    else:
        caractere_atual = frase_restante[0]  # Primeiro caractere da frase restante
        proxima_frase = frase_restante[1:]  # Resto da frase
        # Se o caractere atual não estiver no alfabeto...
        if caractere_atual not in alfabeto_ref:
            # Adiciona o índice do caractere atual na lista de armadilhas
            lista_traps.append(indice_original)
            # Retorna uma string vazia e continua a recursão
            return "" + decifrar(
                proxima_frase,
                chave_atual,
                alfabeto_ref,
                indice_original + 1,
                lista_traps,
            )
        # Se o caractere atual estiver no alfabeto...
        else:
            Ci = alfabeto_ref.index(
                caractere_atual
            )  # Índice do caractere atual no alfabeto
            Ki = alfabeto_ref.index(chave_atual)  # Índice da chave atual no alfabeto
            Mi = (Ci - Ki) % 26  # Índice da letra decifrada
            letra_decifrada = alfabeto_ref[Mi]  # Letra decifrada
            # Retorna a letra decifrada e continua a recursão
            return letra_decifrada + decifrar(
                proxima_frase,
                letra_decifrada,
                alfabeto_ref,
                indice_original + 1,
                lista_traps,
            )


alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# Inputs:
chave_inicial = input()
frase_criptografada = input()
indices_armadilhas = []

# Output:
print("Decifrando mensagem do Trickster...")
mensagem_final = decifrar(
    frase_criptografada, chave_inicial, alfabeto, 0, indices_armadilhas
)
# Se houver armadilhas...
if len(indices_armadilhas) > 0:
    indices_em_str = []  # Lista para armazenar os índices das armadilhas
    for i in indices_armadilhas:  # Para cada índice na lista de armadilhas...
        indices_em_str.append(
            str(i)
        )  # Converte o índice para string e adiciona na lista
        texto_indices = ", ".join(indices_em_str)
    print(
        f"Esse Trickster é um picareta mesmo. Foram encontradas armadilhas nas posições: {texto_indices}"
    )
else:
    print("Nenhuma armadilha encontrada! Até que o Trickster foi bonzinho.")

print(f"Mensagem revelada: {mensagem_final}")
