"""
Questão: Glavin! Essa máquina só pode ser piada!

Enunciado:
O programa simula a máquina do Professor Frink para validar previsões de invenções.
A validade é determinada se o ano da invenção for divisível pelo número de letras do nome do inventor.

Regras:
1. Imprimir "Ativando a máquina..." antes de qualquer input.
2. Receber o nome do inventor e o ano.
3. Calcular se o Ano é divisível pelo tamanho do Nome.
   - Se SIM: Previsão Confiável.
   - Se NÃO: Previsão Instável.
4. Regras Especiais para "Frink":
   - Se for confiável e for o Frink: A máquina está com defeito (ele não acredita).
   - Se for instável e for o Frink: O rebigulador jamais existiria.
5. Para outros nomes, imprimir as mensagens padrão de confiável ou instável.

Input:
- Nome (string) e Ano (int).

Output:
- Mensagem de ativação.
- Resultado da análise da previsão.
"""

# --- MENSAGEM INICIAL OBRIGATÓRIA ---
print("Ativando a máquina...")

# --- INPUTS ---
nome = str(input())
ano = int(input())

# --- PROCESSAMENTO DE DADOS ---
# Formata o nome para capitalizado e conta o número de letras
nome2 = nome.capitalize()
n = len(nome)

# --- LÓGICA DE VALIDAÇÃO (DIVISIBILIDADE) ---
# Verifica se o ano é divisível pelo número de letras do nome
if ano % n == 0:
    # Caso: PREVISÃO CONFIÁVEL

    # Exceção para o Professor Frink
    if nome2 == "Frink":
        print(
            "Professor Frink irá inventar o rebigulador?! A máquina deve estar com defeito! Glavin!"
        )
    # Caso padrão para outros inventores
    else:
        print(f"Previsão confiável! O rebigulador será real em {ano}!")

else:
    # Caso: PREVISÃO INSTÁVEL

    # Exceção para o Professor Frink
    if nome2 == "Frink":
        print(
            "Nem precisava colocar os dados! O rebigulador jamais existiria em qualquer universo!"
        )
    # Caso padrão para outros inventores
    else:
        print(
            f"Previsão instável! {nome2} também deve achar que o rebigulador é ridículo..."
        )
