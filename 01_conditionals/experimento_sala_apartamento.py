ashe = int(input())
aleo = int(input())
araj = int(input())
ahow = int(input())
eshe = int(input())
eleo = int(input())
eraj = int(input())
ehowa = int(input())


she = (ashe * 2) + (eshe * 3)
leo = (aleo * 2) + (eleo * 3)
raj = (araj * 2) + (eraj * 3)
how = (ahow * 2) + (ehowa * 3)

print(f"Pontuação final:\nSheldon: {she}\nLeonard: {leo}\nRaj: {raj}\nHoward: {how}")

maximo = max(she, leo, raj, how)

if maximo == she:
    vencedor = "Sheldon"
elif maximo == leo:
    vencedor = "Leonard"
elif maximo == raj:
    vencedor = "Raj"
else:
    vencedor = "Howard"

print(f"\nO cientista da semana é: {vencedor}")

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
