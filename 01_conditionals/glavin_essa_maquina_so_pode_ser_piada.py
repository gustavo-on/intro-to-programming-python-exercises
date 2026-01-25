print("Ativando a máquina...")

nome = str(input())
ano = int(input())

nome2 = nome.capitalize()
n = len(nome)

if ano % n == 0:
    if nome2 == "Frink":
        print(
            "Professor Frink irá inventar o rebigulador?! A máquina deve estar com defeito! Glavin!"
        )
    else:
        print(f"Previsão confiável! O rebigulador será real em {ano}!")

else:
    if nome2 == "Frink":
        print(
            "Nem precisava colocar os dados! O rebigulador jamais existiria em qualquer universo!"
        )
    else:
        print(
            f"Previsão instável! {nome2} também deve achar que o rebigulador é ridículo..."
        )
