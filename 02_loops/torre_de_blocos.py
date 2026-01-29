"""
Título: Torre de Blocos

Resumo:
Constrói visualmente uma torre de blocos utilizando caracteres, onde cada andar
possui largura crescente e alinhamento à direita, simulando o empilhamento de blocos.

Lógica principal:
- A altura da torre define o número de linhas impressas.
- Cada andar possui uma quantidade crescente de blocos '#'.
- O alinhamento é obtido calculando a quantidade de espaços em branco à esquerda.
- O caractere de espaço utilizado é o Braille Pattern Blank, conforme exigido.

Entradas:
- Altura da torre (int), representando o número de andares.

Saídas:
- Impressão de uma torre em formato textual, usando '#' para blocos
  e o caractere Braille Pattern Blank para os espaços vazios.
"""

# ALTURA DA TORRE:
altura_torre = int(input())
andar = "#"
soma = "##"
numero_andar = 1
espaco = "⠀"  # caractere Braille Pattern Blank, exigido pelo enunciado

for i in range(altura_torre):
    # Calcula quantos espaços são necessários para alinhar o andar à direita
    espaco_andar = altura_torre - numero_andar

    # Gera a quantidade total de espaços em branco para o alinhamento visual
    espaco_total = espaco * espaco_andar

    # Imprime o andar atual com espaçamento e blocos correspondentes
    print(espaco + espaco_total + andar)

    # Atualiza o número do andar para o próximo nível da torre
    numero_andar = numero_andar + 1

    # A cada novo andar, adiciona dois blocos para manter o padrão ímpar de largura
    andar = andar + soma
