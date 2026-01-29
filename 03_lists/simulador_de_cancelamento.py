"""
Título: O Simulador de Cancelamento

Resumo do problema:
O programa simula o impacto de eventos ocorridos na vida de subcelebridades digitais,
calculando ganhos ou perdas percentuais de seguidores conforme cada acontecimento.
Ao final da simulação, os artistas são ordenados em um ranking decrescente de seguidores.

Regras principais:
- Evento 1: perde 10% dos seguidores.
- Evento 2: ganha 5% dos seguidores.
- Evento 3: perde 15% dos seguidores.
- Outros eventos: número de seguidores permanece inalterado.
- O número de seguidores deve ser sempre inteiro (valores decimais são truncados).
- A ordenação do ranking deve ser feita exclusivamente com Bubble Sort.
- Em caso de empate, a ordem de inserção deve ser mantida.

Entradas:
- Quantidade de artistas participantes.
- Nome e número inicial de seguidores de cada artista.
- Um evento associado a cada artista.

Saídas:
- Relatório da simulação de eventos.
- Ranking final com até os 3 artistas com mais seguidores.
"""

# Entrada: número de artistas participantes da dinâmica
n_artistas_dinamica = int(input())

lista_artistas_seguidores = []

# Loop para leitura do nome e seguidores iniciais de cada artista
for artista in range(n_artistas_dinamica):
    artista_novo = input()
    # Separação do nome e da quantidade inicial de seguidores
    nome, seguimores = artista_novo.split(" - ")
    lista_artistas_seguidores.append(nome)
    lista_artistas_seguidores.append(int(seguimores))

lista_eventos = []

# Loop para leitura dos eventos, mantendo a mesma ordem dos artistas
for artista in range(0, len(lista_artistas_seguidores), 2):
    evento_artista = int(input())
    lista_eventos.append(evento_artista)

# Cabeçalho do simulador
print("--- Simulador de Cancelamento ---\n")

# Loop principal para processar os eventos de cada subcelebridade
for i in range(0, len(lista_artistas_seguidores), 2):
    print(f"A subcelebridade da vez é: {lista_artistas_seguidores[i]}")

    # Decisão baseada no tipo de evento
    if lista_eventos[i // 2] == 1:
        print(f"{lista_artistas_seguidores[i]} perdeu 10% dos seguidores!")
        # Cálculo da perda de 10%
        lista_artistas_seguidores[i + 1] *= 0.9

    elif lista_eventos[i // 2] == 2:
        print(f"{lista_artistas_seguidores[i]} ganhou 5% de seguidores!")
        # Cálculo do ganho de 5%
        lista_artistas_seguidores[i + 1] *= 1.05

    elif lista_eventos[i // 2] == 3:
        print(f"{lista_artistas_seguidores[i]} perdeu 15% dos seguidores!")
        # Cálculo da perda de 15%
        lista_artistas_seguidores[i + 1] *= 0.85

    else:
        print("Nenhum evento relevante. Seguidores continuam os mesmos.")

# Ordenação dos artistas por número de seguidores (Bubble Sort)
for i in range(0, len(lista_artistas_seguidores), 2):
    for j in range(0, len(lista_artistas_seguidores) - 2, 2):
        # Decisão: troca se o artista atual tiver menos seguidores que o próximo
        if lista_artistas_seguidores[j + 1] < lista_artistas_seguidores[j + 3]:
            (
                lista_artistas_seguidores[j],
                lista_artistas_seguidores[j + 1],
                lista_artistas_seguidores[j + 2],
                lista_artistas_seguidores[j + 3],
            ) = (
                lista_artistas_seguidores[j + 2],
                lista_artistas_seguidores[j + 3],
                lista_artistas_seguidores[j],
                lista_artistas_seguidores[j + 1],
            )

# Cabeçalho do ranking final
print("\n--- RANKING FINAL DE SEGUIDORES ---")

# Impressão do primeiro colocado
print(
    f"1º Lugar: {lista_artistas_seguidores[0]} com {int(lista_artistas_seguidores[1])} seguidores."
)

# Decisão: imprimir o segundo colocado apenas se existir
if n_artistas_dinamica > 1:
    print(
        f"2º Lugar: {lista_artistas_seguidores[2]} com {int(lista_artistas_seguidores[3])} seguidores."
    )

# Decisão: imprimir o terceiro colocado apenas se existir
if n_artistas_dinamica > 2:
    print(
        f"3º Lugar: {lista_artistas_seguidores[4]} com {int(lista_artistas_seguidores[5])} seguidores."
    )
