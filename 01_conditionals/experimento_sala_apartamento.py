"""
Questão: O Experimento da Sala de Apartamento

Enunciado:
O programa calcula a pontuação de Sheldon, Leonard, Raj e Howard para decidir o "Cientista da Semana".
A fórmula é: Pontuação = (Artigos * 2) + (Experimentos * 3).

Critérios de Desempate (Prioridade):
1. Sheldon (se ele estiver no empate, ele ganha).
2. Leonard.
3. Raj.
4. Howard.

Entrada:
- 4 inteiros (artigos de Sheldon, Leonard, Raj, Howard).
- 4 inteiros (experimentos de Sheldon, Leonard, Raj, Howard).

Saída:
- Lista com a pontuação final de cada um.
- Nome do vencedor.
- Frase temática do vencedor.
"""

# Leitura dos Artigos
a_she = int(input())
a_leo = int(input())
a_raj = int(input())
a_how = int(input())

# Leitura dos Experimentos
e_she = int(input())
e_leo = int(input())
e_raj = int(input())
e_how = int(input())

# Cálculo das pontuações
# Regra: (artigos * 2) + (experimentos * 3)
score_she = (a_she * 2) + (e_she * 3)
score_leo = (a_leo * 2) + (e_leo * 3)
score_raj = (a_raj * 2) + (e_raj * 3)
score_how = (a_how * 2) + (e_how * 3)

# Exibição dos resultados parciais
print(
    f"Pontuação final:\nSheldon: {score_she}\nLeonard: {score_leo}\nRaj: {score_raj}\nHoward: {score_how}"
)

# Definição do vencedor
# A função max() pega o maior valor numérico
maior_pontuacao = max(score_she, score_leo, score_raj, score_how)

# A ordem dos IFs garante o critério de desempate exigido no enunciado:
# Sheldon > Leonard > Raj > Howard
if maior_pontuacao == score_she:
    vencedor = "Sheldon"
elif maior_pontuacao == score_leo:
    vencedor = "Leonard"
elif maior_pontuacao == score_raj:
    vencedor = "Raj"
else:
    vencedor = "Howard"

print(f"\nO cientista da semana é: {vencedor}")

# Frases finais específicas
if vencedor == "Sheldon":
    print("Não é atoa que ele ganhou o prêmio Nobel")
elif vencedor == "Leonard":
    print(
        "A vitória dele prova que aguentar o Sheldon já é um experimento científico por si só."
    )
elif vencedor == "Raj":
    print(
        "Ele comemora... mas ainda precisa da ajuda do cachorro para falar com mulheres."
    )
else:
    print("Um pequeno passo para a ciência, um grande salto para alguém com mestrado.")
