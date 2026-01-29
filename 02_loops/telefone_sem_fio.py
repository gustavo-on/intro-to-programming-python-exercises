"""
Título: Telefone sem fio

Resumo:
Simula a brincadeira de telefone sem fio entre estudantes, verificando se a palavra
inicial é transmitida corretamente até o último participante ou se ocorrem alterações
ao longo do processo.

Lógica principal:
- A primeira palavra dita serve como referência para toda a brincadeira.
- Cada participante compara a palavra que ouviu com a que repassa.
- Sempre que houver diferença, o evento é registrado como uma troca.
- Mensagens finais variam conforme a quantidade de trocas e o estado da palavra final.

Entradas:
- Número de participantes (int).
- Para cada participante: nome (str) e palavra falada (str).

Saídas:
- Mensagens indicando falhas de comunicação durante o jogo.
- Resultado final descrevendo se a palavra foi preservada ou modificada.
"""

print("Vai começar a brincadeira! Será que a palavra vai ficar igual até o fim?")

N = int(input())
participante_anterior = input()
palavra_inicial = input()
palavra_anterior = palavra_inicial
nomes = 2
repetiu = 0
nome_jogador_1 = ""
nome_jogador_2 = ""

while nomes <= N - 1:
    nome_participante = input()
    palavra_falada = input()
    nomes = nomes + 1

    # Verifica se o participante alterou a palavra em relação à que recebeu
    if palavra_falada != palavra_anterior:
        print(
            f"Parece que {nome_participante} não conseguiu ouvir muito bem e acabou passando pra frente uma palavra diferente da que escutou…"
        )

        # Armazena os primeiros jogadores que erraram para uso nos prints finais
        if repetiu == 0:
            nome_jogador_1 = nome_participante
            palavra_errada = palavra_falada
        elif repetiu == 1:
            nome_jogador_2 = nome_participante

        # Incrementa o contador de trocas ocorridas
        repetiu = repetiu + 1

    # Caso o número de trocas atinja 5, imprime a mensagem de confusão extrema
    if repetiu == 5:
        print(
            f"Caramba, que confusão! A palavra {palavra_inicial} já tá toda embaralhada e virou {palavra_falada}!"
        )

    participante_anterior = nome_participante
    palavra_anterior = palavra_falada

ultimo_participante = input()
ultima_palavra = input()

# Trata separadamente o último participante, comparando com a palavra anterior
if ultima_palavra != palavra_anterior:
    print(
        f"Parece que {ultimo_participante} não conseguiu ouvir muito bem e acabou passando pra frente uma palavra diferente da que escutou…"
    )
    repetiu = repetiu + 1

    # Garante que o segundo nome de erro seja registrado, se necessário
    if repetiu > 0:
        nome_jogador_2 = ultimo_participante

# Caso nenhuma troca tenha ocorrido durante todo o jogo
if repetiu == 0:
    print(
        f"Impressionante, todos os jogadores ouviram e falaram perfeitamente a palavra {palavra_inicial}! Talvez os telefones modernos comecem a perder espaço pra moda antiga."
    )

# Caso tenha havido trocas, mas a palavra final seja igual à inicial
if repetiu > 0 and ultima_palavra == palavra_inicial:
    print(
        f"Parece que ocorreram {repetiu} trocas durante o processo, mas mesmo com essa pequena confusão, a palavra {palavra_inicial} conseguiu chegar no fim do telefone sem fio."
    )

# Caso a palavra final seja diferente da palavra inicial
if ultima_palavra != palavra_inicial:
    if repetiu == 1:
        print(
            f"Poxa, foi por pouco, só quem errou foi {nome_jogador_1} que disse {palavra_errada} ao invés de {palavra_inicial}…"
        )
    elif repetiu == 2:
        print(
            f"Se não fosse pelos erros de {nome_jogador_1} e {nome_jogador_2} a palavra {palavra_inicial} poderia ter chegado até o fim, talvez eles devessem tentar de novo."
        )
    elif repetiu > 2:
        print(
            f"É, parece que os alunos se confundiram bastante durante a brincadeira e a palavra {palavra_inicial} acabou virando {ultima_palavra}. No total, ocorreram {repetiu} trocas."
        )
