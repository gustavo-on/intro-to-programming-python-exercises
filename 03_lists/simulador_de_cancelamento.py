# Simulador de cancelamento
# Processar os eventos da vida de cada um e, ao final, revelar quem permaneceu no TOPO DA FAMA

# Eventos:
# Evento 1: Envolver-se em uma polêmica. perde 10% dos seus seguidores (0.9 * seguidores)
# Evento 2: Postar um vídeo de treino inspirador. ganha 5% de seguidores (1.05 * seguidores)
# Evento 3: Fazer uma publicidade controversa. Perde 15% dos seus seguidores (0.85 * seguidores)
# Outro evento: O número de seguidores não se altera.
# OBS: Seguidores sempre valor inteiro. Decimal desconsiderado
# Proibido função sort(). Usar o Bubble Sort

# Inputs
n_artistas_dinamica = int(input())  # Número artistas dinâmica
lista_artistas_seguidores = []
# Para cada um dos artistas...
for artista in range(n_artistas_dinamica):
    artista_novo = input()  # Adicionar nome do artista
    nome, seguimores = artista_novo.split(
        " - "
    )  # Separar o nome e os seguidores iniciais
    lista_artistas_seguidores.append(nome)
    lista_artistas_seguidores.append(
        int(seguimores)
    )  # Adicionar o nome e o número de seguidores

# Evento de cada artista...
lista_eventos = []
for artista in range(0, len(lista_artistas_seguidores), 2):
    evento_artista = int(input())
    lista_eventos.append(evento_artista)

# Output
# Iniciar imprimindo o cabeçalho do simulador com uma linha vazia:
print("--- Simulador de Cancelamento ---\n")
# Anunciar de quem é a vez:
for i in range(0, len(lista_artistas_seguidores), 2):
    print(f"A subcelebridade da vez é: {lista_artistas_seguidores[i]}")
    # Imprimir o resultado da ação:
    if lista_eventos[i // 2] == 1:  # Se o evento for 1
        print(f"{lista_artistas_seguidores[i]} perdeu 10% dos seguidores!")
        lista_artistas_seguidores[i + 1] *= 0.9
    elif lista_eventos[i // 2] == 2:  # Se o evento for 2
        print(f"{lista_artistas_seguidores[i]} ganhou 5% de seguidores!")
        lista_artistas_seguidores[i + 1] *= 1.05
    elif lista_eventos[i // 2] == 3:  # Se o evento for 3
        print(f"{lista_artistas_seguidores[i]} perdeu 15% dos seguidores!")
        lista_artistas_seguidores[i + 1] *= 0.85
    else:  # Se o evento for outro
        print("Nenhum evento relevante. Seguidores continuam os mesmos.")

# Bubble Sort de artistas e seguidores em ordem crescente:
for i in range(0, len(lista_artistas_seguidores), 2):
    for j in range(0, len(lista_artistas_seguidores) - 2, 2):
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


print("\n--- RANKING FINAL DE SEGUIDORES ---")
# Printar o último da lista
print(
    f"1º Lugar: {lista_artistas_seguidores[0]} com {int(lista_artistas_seguidores[1])} seguidores."
)
if n_artistas_dinamica > 1:
    # Printar o penúltimo da lista
    print(
        f"2º Lugar: {lista_artistas_seguidores[2]} com {int(lista_artistas_seguidores[3])} seguidores."
    )
if n_artistas_dinamica > 2:
    # Printar o antepenúltimo da lista
    print(
        f"3º Lugar: {lista_artistas_seguidores[4]} com {int(lista_artistas_seguidores[5])} seguidores."
    )
