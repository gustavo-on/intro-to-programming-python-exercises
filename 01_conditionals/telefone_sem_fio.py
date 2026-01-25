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

    if palavra_falada != palavra_anterior:
        print(
            f"Parece que {nome_participante} não conseguiu ouvir muito bem e acabou passando pra frente uma palavra diferente da que escutou…"
        )
        if repetiu == 0:
            nome_jogador_1 = nome_participante
            palavra_errada = palavra_falada
        elif repetiu == 1:
            nome_jogador_2 = nome_participante
        repetiu = repetiu + 1

    if repetiu == 5:
        print(
            f"Caramba, que confusão! A palavra {palavra_inicial} já tá toda embaralhada e virou {palavra_falada}!"
        )

    participante_anterior = nome_participante
    palavra_anterior = palavra_falada

ultimo_participante = input()
ultima_palavra = input()
if ultima_palavra != palavra_anterior:
    print(
        f"Parece que {ultimo_participante} não conseguiu ouvir muito bem e acabou passando pra frente uma palavra diferente da que escutou…"
    )
    repetiu = repetiu + 1
    if repetiu > 0:
        nome_jogador_2 = ultimo_participante

if repetiu == 0:
    print(
        f"Impressionante, todos os jogadores ouviram e falaram perfeitamente a palavra {palavra_inicial}! Talvez os telefones modernos comecem a perder espaço pra moda antiga."
    )

if repetiu > 0 and ultima_palavra == palavra_inicial:
    print(
        f"Parece que ocorreram {repetiu} trocas durante o processo, mas mesmo com essa pequena confusão, a palavra {palavra_inicial} conseguiu chegar no fim do telefone sem fio."
    )

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
