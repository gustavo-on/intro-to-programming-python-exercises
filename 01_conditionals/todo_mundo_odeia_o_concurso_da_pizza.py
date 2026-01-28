"""
Questão: Todo Mundo Odeia o Concurso da Pizza

Enunciado:
O programa deve ajudar Chris a calcular sua média final em Álgebra e sua porcentagem de presença.
Regras para aprovação:
- Média >= 7.0
- Presença >= 75%

Condições de Saída:
1. Média >= 8 e Presença >= 75%: Aprovado com louvor (ajuda na pizza).
2. 7 <= Média < 8 e Presença >= 75%: Aprovado (passou raspando).
3. Média >= 7 e Presença < 75%: Reprovado por Falta.
4. Média < 7 e Presença >= 75%: Reprovado por Nota.
5. Média < 7 e Presença < 75%: Reprovado por ambos.

Entrada:
- Nota 1 (float)
- Nota 2 (float)
- Nota 3 (float)
- Quantidade de aulas (int)
- Quantidade de faltas (int)

Saída:
- Média e porcentagem de presença.
- Mensagem de status correspondente com frases da série.
"""

nota_1 = float(input())
nota_2 = float(input())
nota_3 = float(input())
qt_aulas = int(input())
qt_faltas = int(input())

# Cálculo da média simples
media = (nota_1 + nota_2 + nota_3) / 3

# Cálculo da porcentagem de presença
# (Total - Faltas) / Total
presenca = ((qt_aulas - qt_faltas) / qt_aulas) * 100

print(f"Chris, você conseguiu média {media:.2f} e {presenca:.2f}% de presença.")

# Verificação das condições
if media >= 8 and presenca >= 75:
    print("Chris está APROVADO por nota e por presença! 🎉")
    print("Pisante maneiro, Chris! Agora é só torcer pros outros não vacilarem.")
elif (media >= 7 and media < 8) and presenca >= 75:
    print("Chris está APROVADO! ✅")
    print("Sacomé, né? Passou raspando, mas a pizza ainda ficou longe.")
elif media >= 7 and presenca < 75:
    print("Chris ESTÁ REPROVADO por FALTA. ❌")
    print("Trágico! Não adianta só saber, tem que aparecer.")
elif media < 7 and presenca >= 75:
    print("Chris ESTÁ REPROVADO por NOTA. ❌")
    print("Chris, já pro seu quarto ou eu vou te bater até você virar o avesso!")
else:
    print("Chris ESTÁ REPROVADO por NOTA e por FALTA. ❌")
    print(
        "Chris, você perdeu o juízo? Eu trouxe você para esse mundo e posso muito bem tirar você dele."
    )
