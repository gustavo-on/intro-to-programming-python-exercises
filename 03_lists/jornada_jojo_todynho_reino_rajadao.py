# Frase inicial
lista_frases = [
    "Que tiro foi esse?",
    "Segura a marimba",
    "Tá com raiva? Morde as costas",
    "Bateu de frente é só rajadão",
]
lista_sem_repeticao = lista_frases.copy()

# inputs
quant_novas_Frases = int(input())
for i in range(quant_novas_Frases):
    nova_frase = input()
    if nova_frase in lista_frases:
        lista_frases.append(nova_frase)
    else:
        lista_sem_repeticao.append(nova_frase)
        lista_frases.append(nova_frase)

for i in lista_sem_repeticao:
    print(f'"{i}": {lista_frases.count(i)}')

lista_ordenada = sorted(lista_frases)
print(lista_ordenada)
