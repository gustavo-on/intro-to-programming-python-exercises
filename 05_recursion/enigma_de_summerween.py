"""
Título: O Enigma de Summerween

Resumo do problema:
Decifrar uma mensagem criptografada usando uma cifra encadeada baseada no alfabeto.
Cada letra decifrada torna-se a chave da próxima, ignorando símbolos que não pertencem
ao alfabeto e registrando suas posições como armadilhas.

Lógica principal / Regras:
- A decifração segue a fórmula Mi = (Ci - Ki) mod 26.
- A chave inicial é usada apenas para a primeira letra válida.
- Cada letra decifrada passa a ser a chave da próxima iteração.
- Símbolos fora do alfabeto não geram letra decifrada e não alteram a chave,
  mas têm seus índices registrados como armadilhas.
- A solução é implementada de forma recursiva.

Entradas:
- Uma letra maiúscula representando a chave inicial.
- Uma string representando a frase criptografada (letras e possíveis símbolos).

Saídas:
- Mensagens informativas sobre o início da decifração.
- Lista de índices onde símbolos inválidos foram encontrados (se existirem).
- Mensagem final decifrada contendo apenas letras válidas.
"""


def decifrar(frase_restante, chave_atual, alfabeto_ref, indice_original, lista_traps):
    # Decisão: condição de parada da recursão quando não há mais caracteres a processar
    if len(frase_restante) == 0:
        return ""
    else:
        caractere_atual = frase_restante[0]
        proxima_frase = frase_restante[1:]

        # Decisão: caracteres fora do alfabeto não participam da cifra
        # e devem ser registrados como armadilhas sem alterar a chave atual
        if caractere_atual not in alfabeto_ref:
            lista_traps.append(indice_original)
            return "" + decifrar(
                proxima_frase,
                chave_atual,
                alfabeto_ref,
                indice_original + 1,
                lista_traps,
            )
        else:
            # Cálculo: conversão da letra criptografada para seu índice numérico
            Ci = alfabeto_ref.index(caractere_atual)

            # Cálculo: conversão da chave atual para índice, permitindo a subtração modular
            Ki = alfabeto_ref.index(chave_atual)

            # Cálculo central da cifra:
            # uso de módulo 26 garante retorno ao intervalo do alfabeto
            Mi = (Ci - Ki) % 26

            letra_decifrada = alfabeto_ref[Mi]

            # Decisão implícita: a letra decifrada torna-se a próxima chave,
            # mantendo o encadeamento exigido pelo enigma
            return letra_decifrada + decifrar(
                proxima_frase,
                letra_decifrada,
                alfabeto_ref,
                indice_original + 1,
                lista_traps,
            )


alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Entradas garantidas pelo enunciado como válidas
chave_inicial = input()
frase_criptografada = input()

indices_armadilhas = []

print("Decifrando mensagem do Trickster...")

mensagem_final = decifrar(
    frase_criptografada, chave_inicial, alfabeto, 0, indices_armadilhas
)

# Decisão: existência de armadilhas altera a mensagem de saída
if len(indices_armadilhas) > 0:
    indices_em_str = []
    for i in indices_armadilhas:
        # Conversão necessária apenas para formatação da saída textual
        indices_em_str.append(str(i))
        texto_indices = ", ".join(indices_em_str)

    print(
        f"Esse Trickster é um picareta mesmo. Foram encontradas armadilhas nas posições: {texto_indices}"
    )
else:
    print("Nenhuma armadilha encontrada! Até que o Trickster foi bonzinho.")

print(f"Mensagem revelada: {mensagem_final}")
