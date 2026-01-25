nome_competidor1 = input()
pasteis_competidor1 = int(input())
nome_competidor2 = input()
pasteis_competidor2 = int(input())
nome_competidor3 = input()
pasteis_competidor3 = int(input())

pasteis_Campeao = max(pasteis_competidor1, pasteis_competidor2, pasteis_competidor3)

if pasteis_Campeao == pasteis_competidor1:
    nome_Campeao = nome_competidor1
elif pasteis_Campeao == pasteis_competidor2:
    nome_Campeao = nome_competidor2
else:
    nome_Campeao = nome_competidor3

if (
    nome_competidor1 == "Lineu"
    or nome_competidor2 == "Lineu"
    or nome_competidor3 == "Lineu"
):
    print(
        "Lineu comeu um pastel com gosto estranho e usou sua autoridade na vigilancia sanitaria para acabar com a competição, Beiçola tá desolado!"
    )

else:
    print(f"A(O) campeã(o) é {nome_Campeao}, com {pasteis_Campeao} pastéis consumidos!")

if (
    (nome_competidor1 == "Floriano")
    or (nome_competidor2 == "Floriano")
    or (nome_competidor3 == "Floriano")
):
    if nome_Campeao != "Floriano":
        print(
            f"Anos comendo pastel e perdeu justo para {nome_Campeao}, lastimável, Sr. Flor!"
        )

if (nome_Campeao == "Agostinho") and (pasteis_Campeao > 100):
    print("Acho que o Agostinho deve ter escondido alguns pastéis na calça, pilantra!")
elif nome_Campeao == "Agostinho" and pasteis_Campeao > 50:
    print("Agostinho madrugou no taxi e veio cheio de fome para a competição!")
