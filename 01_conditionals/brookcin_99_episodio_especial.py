"""
Questão: BrookCin - 99: Episódio Especial

Enunciado:
Simulação de uma competição entre detetives da delegacia 99 organizada pelo Capitão Holt.
O programa deve verificar 5 critérios eliminatórios e, se o detetive passar por todos, calcular sua pontuação final baseada em desempenho e operações especiais.

Critérios Eliminatórios (nesta ordem):
1. Localização: Apenas "Manhattan" ou "Brooklyn".
2. Quantidade de casos: Mínimo de 20.
3. Média diária: Mínimo de 0.5 casos/dia.
4. Assistências: Mínimo de 5.
5. Operações de campo: Mínimo de 20.

Cálculo da Pontuação:
- Base: (Casos * 2) + (Assistências * 1.5) + (Operações * 0.5)
- Multiplicador (apenas se houve Operação Especial):
  - Infiltração: +50%
  - Escuta: +30%
  - Invasão: +20%
  - Outros: +10%

Input:
- Dados numéricos de performance e strings de detalhes da operação/local.

Output:
- Mensagens de aprovação ou desclassificação passo a passo.
- Classificação final baseada na pontuação (>=70, >=40, <40).
"""

# --- INPUTS ---
casos = int(input())
dias = int(input())
assistencias = int(input())
operacoes_em_campo = int(input())
operacao_especial = input()

tipo_operacao = ""
if operacao_especial == "sim":
    tipo_operacao = input()

local = input()

# --- CÁLCULOS PRELIMINARES ---

# 1. Pontuação Base
pontuacao = (casos * 2) + (assistencias * 1.5) + (operacoes_em_campo * 0.5)

# 2. Definição do Multiplicador (Aumento Percentual)
if operacao_especial == "sim":
    if tipo_operacao == "Infiltração":
        aumento = 1.5  # +50%
    elif tipo_operacao == "Escuta":
        aumento = 1.3  # +30%
    elif tipo_operacao == "Invasão":
        aumento = 1.2  # +20%
    else:
        aumento = 1.1  # +10% (Nenhuma das anteriores)
else:
    aumento = 1.0  # Sem aumento

# 3. Média Diária
if dias > 0:
    casos_dia = casos / dias
else:
    casos_dia = 0

# 4. Pontuação Final
pontuacao_final = pontuacao * aumento


# --- LÓGICA DE VALIDAÇÃO (ESTRUTURA DE FUNIL) ---

# 1º Requisito: Localização
if local != "Manhattan" and local != "Brooklyn":
    print(
        "Os casos não são nas áreas designadas por Holt. Peralta está desclassificado!"
    )
else:
    print("Pelo menos nos bairros corretos Jake está!")

    # 2º Requisito: Mínimo de Casos
    if casos < 20:
        print("Vishh, Jake já foi eliminado por não ter o mínimo de casos necessários.")
    else:
        print(
            "Detetive Peralta bateu o mínimo de casos, ele ainda está dentro da competição."
        )

        # 3º Requisito: Média Diária
        if casos_dia < 0.5:
            print(
                "A média diária de casos tá muito baixa, Peralta foi desclassificado."
            )
        else:
            print("Parece que Jake é bem consistente na sua média diária de casos.")

            # 4º Requisito: Assistências
            if assistencias < 5:
                print("Desclassificado! Jake precisa ajudar mais os companheiros.")
            else:
                print(
                    "Peralta ajudou bastante outros detetives, ele ainda está na competição!"
                )

                # 5º Requisito: Operações em Campo
                if operacoes_em_campo < 20:
                    print(
                        "Peralta precisa sair mais da delegacia, está faltando ação em campo!"
                    )
                else:
                    print(
                        "Jake ainda sobrevive por sua participação em campo, será que ele vai levar pra casa o prêmio?"
                    )

                    # --- ANÁLISE FINAL (APENAS SE SOBREVIVEU A TODOS OS REQUISITOS) ---

                    # Mensagem sobre Operação Especial
                    if operacao_especial == "sim":
                        print(
                            "Minha nossa! Jake Peralta é realmente um detetive diferenciado."
                        )
                    else:
                        print(
                            "Para que operação especial quando se tem números, não é?"
                        )

                    # Classificação por Pontuação
                    if pontuacao_final >= 70:
                        print(
                            "Jake é candidato forte ao prêmio. Será que Holt vai premiá-lo?"
                        )
                    elif pontuacao_final >= 40:
                        print(
                            "Muito bem! Mas ainda é incerto se vai ser suficiente para ganhar o prêmio."
                        )
                    else:
                        print("Muito difícil de Jake ganhar o prêmio.")
