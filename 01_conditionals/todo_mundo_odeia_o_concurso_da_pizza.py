nota_1 = float(input())
nota_2 = float(input())
nota_3 = float(input())
qt_aulas = int(input())
qt_faltas = int(input())

media = (nota_1 + nota_2 + nota_3) / 3
presenca = ((qt_aulas - qt_faltas) / qt_aulas) * 100

print(f"Chris, você conseguiu média {media:.2f} e {presenca:.2f}% de presença.")

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
