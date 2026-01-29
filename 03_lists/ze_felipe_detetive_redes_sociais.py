"""
Título: Zé Felipe: O Detetive das Redes Sociais

Resumo do problema:
Analisa uma sequência de eventos envolvendo Virgínia, Zé Felipe e um Jogador Misterioso para
determinar um nível de suspeita. Os eventos devem ser organizados cronologicamente e avaliados
com base em regras de sobreposição de horários, resultando em um relatório investigativo final.

Lógica principal / Regras de aprovação:
- Todos os eventos são ordenados cronologicamente pelo horário de início (e fim, em caso de empate),
  usando Bubble Sort, sem funções nativas de ordenação.
- Se existir um evento do tipo VJM, a investigação é encerrada imediatamente com suspeita máxima.
- Sobreposição entre Virgínia e Jogador Misterioso aumenta a suspeita.
- Sobreposição entre Virgínia e Zé Felipe reduz a suspeita, sem permitir valores negativos.
- Eventos isolados não afetam a pontuação.
- Ao final, o nível de suspeita define a conclusão textual da investigação.

Entradas:
- Um inteiro representando o número de eventos.
- N strings no formato: SIGLA - EVENTO - HORA_INICIO - HORA_FIM.

Saídas:
- Mensagem inicial de investigação.
- Linha do tempo dos eventos ordenados.
- Resumo com contadores de encontros suspeitos e álibis.
- Conclusão final baseada no nível de suspeita calculado.
"""

# Mensagem inicial:
print("Iniciando investigação... Zé Felipe está focado.")

# Variáveis de controle da investigação
nivel_de_suspeita = 0
num_encontros_suspeitos = 0
num_alibis_confirmados = 0
prova_definitiva = False
lista_eventos = []

# Número de eventos:
num_eventos = int(input())

for i in range(num_eventos):
    evento = input()
    # Dividindo a string em partes para isolar personagem, evento e horários
    partes = evento.split("-")
    sigla_personagem = partes[0].strip()
    evento = partes[1].strip()
    horainicio = partes[2].strip()
    horafim = partes[3].strip()

    # Regra 1: presença de VJM encerra a investigação com prova definitiva
    if sigla_personagem == "VJM":
        prova_definitiva = True

    # Conversão de horas para minutos para permitir comparação numérica consistente
    horainicio_split = horainicio.split(":")
    inicio_minutos = (int(horainicio_split[0]) * 60) + int(horainicio_split[1])
    horafim_split = horafim.split(":")
    fim_minutos = (int(horafim_split[0]) * 60) + int(horafim_split[1])

    # Armazena o evento com horários convertidos e originais para análise e impressão
    lista_eventos.append(
        [inicio_minutos, fim_minutos, sigla_personagem, evento, horainicio, horafim]
    )

# Se houver prova definitiva, ignora toda a análise detalhada
if prova_definitiva:  # Regra 1
    nivel_de_suspeita = 100
else:
    # Ordenação dos eventos por horário usando Bubble Sort (restrição do problema)
    n = len(lista_eventos)
    for i in range(n):
        for j in range(0, n - i - 1):
            evento_A = lista_eventos[j]
            evento_B = lista_eventos[j + 1]
            inicio_A = evento_A[0]
            fim_A = evento_A[1]
            inicio_B = evento_B[0]
            fim_B = evento_B[1]

            # Troca se o evento A começa depois do evento B
            if inicio_A > inicio_B:
                lista_eventos[j], lista_eventos[j + 1] = (
                    lista_eventos[j + 1],
                    lista_eventos[j],
                )
            # Critério de desempate: quem termina mais cedo vem primeiro
            elif inicio_A == inicio_B:
                if fim_A > fim_B:
                    lista_eventos[j], lista_eventos[j + 1] = (
                        lista_eventos[j + 1],
                        lista_eventos[j],
                    )

    # Impressão da linha do tempo já ordenada
    print("\n--- Linha do Tempo dos Eventos ---")
    for evento in lista_eventos:
        sigla = evento[2].strip()
        nome_evento = evento[3].strip()
        horainicio = evento[4].strip()
        horafim = evento[5].strip()

        # Mapeamento de siglas para nomes completos para exibição correta
        if sigla == "V":
            nome_personagem = "Virgínia"
        elif sigla == "JM":
            nome_personagem = "Jogador Misterioso"
        elif sigla == "ZF":
            nome_personagem = "Zé Felipe"
        elif sigla == "VJM":
            nome_personagem = "Virgínia e Jogador Misterioso"

        print(f"{horainicio}-{horafim}: {nome_personagem} - {nome_evento}")

    # Análise de sobreposição entre eventos no mesmo local
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

            # Apenas eventos no mesmo local podem gerar suspeita ou álibi
            if local_A == local_B:
                # Condição matemática de sobreposição de intervalos
                if (inicio_A < fim_B) and (inicio_B < fim_A):
                    # Encontro suspeito: Virgínia + Jogador Misterioso
                    if (sigla_A == "V" and sigla_B == "JM") or (
                        sigla_A == "JM" and sigla_B == "V"
                    ):
                        nivel_de_suspeita += 35
                        num_encontros_suspeitos += 1
                    # Álibi confirmado: Virgínia + Zé Felipe
                    elif (sigla_A == "V" and sigla_B == "ZF") or (
                        sigla_A == "ZF" and sigla_B == "V"
                    ):
                        nivel_de_suspeita -= 20
                        num_alibis_confirmados += 1
                        # Garante que a suspeita nunca seja negativa
                        if nivel_de_suspeita < 0:
                            nivel_de_suspeita = 0

    print("\n--- Resumo da Análise ---")
    print(f"Encontros Suspeitos: {num_encontros_suspeitos}")
    print(f"Álibis Confirmados: {num_alibis_confirmados}")

# Conclusão da Análise baseada nos intervalos de suspeita
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
