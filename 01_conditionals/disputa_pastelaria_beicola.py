"""
Questão: Disputa na Pastelaria do Beiçola

Enunciado:
O programa deve registrar o desempenho de 3 competidores em um concurso de comer pastéis.
É necessário identificar o vencedor (maior quantidade) e reagir a situações específicas envolvendo personagens de A Grande Família (Lineu, Floriano, Agostinho).

Regras:
1. Receber nome e quantidade de pastéis de 3 competidores.
2. Determinar o campeão baseado na maior quantidade (assumindo sem empates).
3. Regra do Lineu: Se "Lineu" estiver competindo, a disputa é cancelada pela vigilância sanitária.
4. Se Lineu não estiver, anuncia-se o vencedor.
5. Regra do Floriano: Se "Floriano" competiu e perdeu, imprimir mensagem de lamento.
6. Regras do Agostinho:
   - Se Agostinho venceu com > 100 pastéis: acusar de esconder na calça.
   - Se Agostinho venceu com > 50 e <= 100: comentar sobre a fome.

Input:
- 3 pares de dados: Nome (string) e Quantidade (int).

Output:
- Mensagem de cancelamento (se Lineu presente).
- Declaração do campeão.
- Mensagens extras para Floriano ou Agostinho conforme regras.
"""

# --- INPUTS ---
nome_competidor1 = input()
pasteis_competidor1 = int(input())
nome_competidor2 = input()
pasteis_competidor2 = int(input())
nome_competidor3 = input()
pasteis_competidor3 = int(input())

# --- CÁLCULO DO CAMPEÃO ---
# Determina o maior valor numérico entre os competidores
pasteis_Campeao = max(pasteis_competidor1, pasteis_competidor2, pasteis_competidor3)

# Identifica o nome associado à maior quantidade
if pasteis_Campeao == pasteis_competidor1:
    nome_Campeao = nome_competidor1
elif pasteis_Campeao == pasteis_competidor2:
    nome_Campeao = nome_competidor2
else:
    nome_Campeao = nome_competidor3

# --- REGRA DO LINEU (CANCELAMENTO) ---
# Se Lineu estiver entre os competidores, a competição acaba aqui
if (
    nome_competidor1 == "Lineu"
    or nome_competidor2 == "Lineu"
    or nome_competidor3 == "Lineu"
):
    print(
        "Lineu comeu um pastel com gosto estranho e usou sua autoridade na vigilancia sanitaria para acabar com a competição, Beiçola tá desolado!"
    )

else:
    # Se Lineu não está, anuncia o vencedor
    print(f"A(O) campeã(o) é {nome_Campeao}, com {pasteis_Campeao} pastéis consumidos!")

# --- REGRA DO FLORIANO ---
# Verifica se Floriano participou mas não ganhou
if (
    (nome_competidor1 == "Floriano")
    or (nome_competidor2 == "Floriano")
    or (nome_competidor3 == "Floriano")
):
    if nome_Campeao != "Floriano":
        print(
            f"Anos comendo pastel e perdeu justo para {nome_Campeao}, lastimável, Sr. Flor!"
        )

# --- REGRAS DO AGOSTINHO ---
# Verifica situações suspeitas ou de muita fome caso Agostinho vença
if (nome_Campeao == "Agostinho") and (pasteis_Campeao > 100):
    print("Acho que o Agostinho deve ter escondido alguns pastéis na calça, pilantra!")
elif nome_Campeao == "Agostinho" and pasteis_Campeao > 50:
    print("Agostinho madrugou no taxi e veio cheio de fome para a competição!")
