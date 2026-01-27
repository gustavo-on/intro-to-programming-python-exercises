# Mensagem inicial:
print("Iniciando investigação... Zé Felipe está focado.")

# Variáveis de controle:
nivel_de_suspeita = 0
num_encontros_suspeitos = 0
num_alibis_confirmados = 0
prova_definitiva = False
lista_eventos = []

# Número de eventos:
num_eventos = int(input())

for i in range(num_eventos):
    evento = input()
    # Dividindo a string em partes:
    partes = evento.split("-")
    sigla_personagem = partes[0].strip()
    evento = partes[1].strip()
    horainicio = partes[2].strip()
    horafim = partes[3].strip()

    if sigla_personagem == "VJM":
        prova_definitiva = True

    # Horas em minutos:
    horainicio_split = horainicio.split(":")
    inicio_minutos = (int(horainicio_split[0]) * 60) + int(horainicio_split[1])
    horafim_split = horafim.split(":")
    fim_minutos = (int(horafim_split[0]) * 60) + int(horafim_split[1])

    # Guardando os eventos em uma lista:
    lista_eventos.append(
        [inicio_minutos, fim_minutos, sigla_personagem, evento, horainicio, horafim]
    )

if prova_definitiva:  # Regra 1
    nivel_de_suspeita = 100
else:
    # Ordenando a lista de eventos com Bubble Sort:
    n = len(lista_eventos)
    for i in range(n):
        for j in range(0, n - i - 1):
            # Comparação:
            evento_A = lista_eventos[j]
            evento_B = lista_eventos[j + 1]
            inicio_A = evento_A[0]
            fim_A = evento_A[1]
            inicio_B = evento_B[0]
            fim_B = evento_B[1]
            # Lógica de Troca:
            if inicio_A > inicio_B:
                lista_eventos[j], lista_eventos[j + 1] = (
                    lista_eventos[j + 1],
                    lista_eventos[j],
                )
            elif inicio_A == inicio_B:
                if fim_A > fim_B:
                    lista_eventos[j], lista_eventos[j + 1] = (
                        lista_eventos[j + 1],
                        lista_eventos[j],
                    )

    # Agora que a lista está ordenada, imprimimos a lista ordenada
    print("\n--- Linha do Tempo dos Eventos ---")
    for evento in lista_eventos:
        sigla = evento[2].strip()
        nome_evento = evento[3].strip()
        horainicio = evento[4].strip()
        horafim = evento[5].strip()
        # Encontrar o nome completo:
        if sigla == "V":
            nome_personagem = "Virgínia"
        elif sigla == "JM":
            nome_personagem = "Jogador Misterioso"
        elif sigla == "ZF":
            nome_personagem = "Zé Felipe"
        elif sigla == "VJM":
            nome_personagem = "Virgínia e Jogador Misterioso"
        print(f"{horainicio}-{horafim}: {nome_personagem} - {nome_evento}")

    # Análise de Sobreposição:
    n = len(lista_eventos)
    for i in range(n):
        for j in range(i + 1, n):
            evento_A = lista_eventos[i]
            evento_B = lista_eventos[j]
            inicio_A = evento_A[0]
            fim_A = evento_A[1]
            sigla_A = evento_A[2]
            local_A = evento_A[3]
            inicio_B = evento_B[0]
            fim_B = evento_B[1]
            sigla_B = evento_B[2]
            local_B = evento_B[3]
            if local_A == local_B:
                if (inicio_A < fim_B) and (inicio_B < fim_A):
                    if (sigla_A == "V" and sigla_B == "JM") or (
                        sigla_A == "JM" and sigla_B == "V"
                    ):
                        nivel_de_suspeita += 35
                        num_encontros_suspeitos += 1
                    elif (sigla_A == "V" and sigla_B == "ZF") or (
                        sigla_A == "ZF" and sigla_B == "V"
                    ):
                        nivel_de_suspeita -= 20
                        num_alibis_confirmados += 1
                        if nivel_de_suspeita < 0:
                            nivel_de_suspeita = 0

    print("\n--- Resumo da Análise ---")
    print(f"Encontros Suspeitos: {num_encontros_suspeitos}")
    print(f"Álibis Confirmados: {num_alibis_confirmados}")

# Conclusão da Análise:
print("")
if nivel_de_suspeita >= 100:
    print("TRAIÇÃO CONFIRMADA! Zé Felipe vai fazer uma música sobre isso.")
elif nivel_de_suspeita >= 70:
    print(
        f"Nível de Suspeita: {nivel_de_suspeita} - MUITO SUSPEITO! Zé Felipe vai ter uma conversa séria com a Virgínia."
    )
elif nivel_de_suspeita >= 30:
    print(
        f"Nível de Suspeita: {nivel_de_suspeita} - Hmmm, algo de estranho não está certo. Zé Felipe vai ficar de olho."
    )
else:
    print(
        f"Nível de Suspeita: {nivel_de_suspeita} - Não há motivo para preocupação. Zé Felipe pode respirar aliviado e voltar a brincar com a Maria Flor."
    )
