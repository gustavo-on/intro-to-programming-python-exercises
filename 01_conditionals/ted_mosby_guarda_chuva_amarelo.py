x1 = int(input())  # X Ted
y1 = int(input())  # Y Ted
x2 = int(input())  # X guarda-chuva
y2 = int(input())  # Y guarda-chuva
amigoz = input()
amigo = amigoz.capitalize()

distancia_original = (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5

if amigo == "Barney":
    distancia_final = distancia_original + 10
    texto1 = "Nossa, eu sou incrível! Vimos o guarda-chuva em 5 minutos. Tão lendário que eu poderia até ter pego ele pra mim! Desafio aceito!"
    texto2 = "Esse não era o caminho para o guarda-chuva, mas com certeza é o caminho para uma noite lendária! Challenge accepted, vista seu terno!"
elif amigo == "Marshall":
    distancia_final = distancia_original - 5
    texto1 = "Obrigado pela ajuda, Marsh! Tão bom saber que a gente pode contar com os amigos pra achar a nossa cara-metade. Encontramos o guarda-chuva!"
    texto2 = "Tudo bem, cara. O destino é paciente. O importante é que estamos juntos nessa. Vamos tentar de novo amanhã."
elif amigo == "Lily":
    distancia_final = distancia_original - 10
    texto1 = "Ah! Não te falei? Peguei um atalho! Lilypad sabe das coisas. O guarda-chuva está aqui, e nem nos cansamos muito!"
    texto2 = "Isso não faz sentido! Meu atalho deveria ter funcionado! Que saco! Fiquei com fome de tanta caminhada."
else:
    distancia_final = distancia_original + 5
    texto1 = "Bem... acho que isso realmente aconteceu. Nem foi tão difícil assim. O guarda-chuva está bem aqui, Ted. Onde está o mistério?"
    texto2 = "Sério, Ted? Um guarda-chuva? O destino é um conceito abstrato."

print(f"Pelos meus cálculos a distância final encontrada foi {round(distancia_final)}!")

if distancia_final <= 50:
    print(f"{texto1}")
else:
    print(f"{texto2}")
