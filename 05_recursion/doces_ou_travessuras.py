"""
Título: Doces ou Travessuras

Resumo do problema:
Calcular o número de partições possíveis de um número natural N, onde cada partição
representa uma forma distinta de distribuir N doces em pacotinhos de tamanhos positivos.

Lógica principal / Regras:
- Uma partição é uma decomposição de N como soma de inteiros positivos, sem considerar ordem.
- A solução utiliza recursão para explorar duas decisões: usar ou não um determinado valor máximo.
- O caso base N = 0 representa exatamente uma partição válida (a soma vazia).
- Valores negativos ou ausência de números disponíveis inviabilizam partições.

Entradas:
- Um inteiro N (N ≥ 1), representando a quantidade total de doces.

Saídas:
- Impressão de mensagens temáticas.
- Quantidade total de partições possíveis de N.
- Mensagem adicional indicando se o número de partições é par ou ímpar.
"""


def num_particoes(alvo, max):
    # Decisão: atingir exatamente zero doces caracteriza uma partição válida
    if alvo == 0:
        return 1

    # Decisão: valores negativos ou limite máximo zero inviabilizam a soma
    elif alvo < 0 or max == 0:
        return 0

    else:
        # Cálculo recursivo:
        # soma das partições que não usam o valor máximo atual
        # com as que usam ao menos uma vez esse valor
        return num_particoes(alvo, max - 1) + num_particoes(alvo - max, max)


# Entrada garantida pelo enunciado como válida
doces = int(input())

# Cálculo: inicia a recursão permitindo valores até o próprio número de doces
particoes = num_particoes(doces, doces)

print("DOCES OU TRAVESSURAS???")
print(f"sem travessuras por hoje! tenho {particoes} sacolinhas pra vocês")

# Decisão: verificação de paridade do número de partições
if particoes % 2 == 1:
    print("hmm... número ímpar de sacolinhas 🍭 cuidado com as bruxas!")
else:
    print("doces equilibrados, sem travessuras!")
