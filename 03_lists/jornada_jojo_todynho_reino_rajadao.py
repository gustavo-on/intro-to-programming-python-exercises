"""
Título: A Jornada de Jojo Todynho no Reino do Rajadão

Resumo do problema:
O programa mantém um conjunto inicial de frases fixas e recebe novas frases via entrada.
Todas as frases (iniciais e novas) devem ser contabilizadas, exibindo quantas vezes cada
frase aparece, e ao final listadas em ordem alfabética, respeitando repetições.

Lógica principal / regra de funcionamento:
- As quatro frases iniciais já fazem parte da contagem.
- Novas frases são adicionadas à lista principal, podendo repetir frases existentes.
- Uma lista auxiliar controla quais frases já foram exibidas na contagem.
- A contagem é feita percorrendo a lista completa e contando ocorrências de cada frase.
- Ao final, todas as frases são ordenadas alfabeticamente, incluindo repetições.

Entradas:
- Um inteiro N representando a quantidade de novas frases.
- N strings, cada uma sendo uma nova frase a ser adicionada.

Saídas:
- Para cada frase distinta, imprime a quantidade total de ocorrências no formato:
  "frase": quantidade
- Uma lista com todas as frases (incluindo repetições), ordenadas alfabeticamente.
"""

# Lista inicial de frases que já entram na contagem
lista_frases = [
    "Que tiro foi esse?",
    "Segura a marimba",
    "Tá com raiva? Morde as costas",
    "Bateu de frente é só rajadão",
]

# Lista auxiliar para controlar quais frases já foram consideradas na impressão da contagem
lista_sem_repeticao = lista_frases.copy()

# Leitura da quantidade de novas frases
quant_novas_Frases = int(input())

for i in range(quant_novas_Frases):
    nova_frase = input()

    # Decisão: verifica se a frase já existe para evitar duplicação na lista de controle,
    # mas ainda assim permitir múltiplas ocorrências na lista principal
    if nova_frase in lista_frases:
        lista_frases.append(nova_frase)
    else:
        lista_sem_repeticao.append(nova_frase)
        lista_frases.append(nova_frase)

for i in lista_sem_repeticao:
    # Cálculo: conta quantas vezes cada frase aparece na lista completa,
    # garantindo que a contagem reflita todas as repetições
    print(f'"{i}": {lista_frases.count(i)}')

# Ordenação alfabética da lista completa, preservando todas as repetições
lista_ordenada = sorted(lista_frases)
print(lista_ordenada)
