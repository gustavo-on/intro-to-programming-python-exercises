# Input:
niveis_dificuldade = input()

entrada_valida = True  # Variável para verificar se a entrada é válida
jogo_segue = True  # Variável para verificar se o jogo segue
dificuldade_lista = (
    niveis_dificuldade.split()
)  # Separa os valores de entrada em uma lista

# Se a entrada não tiver 4 valores, ela será inválida
if len(dificuldade_lista) != 4:
    print('"Uh, Phone Guy aqui. Os animatronics estão um pouco "sapecas" esta noite."')
    entrada_valida = False

# Verificar se todos os valores são numéricos e se estão entre 0 e 20:
if entrada_valida:  # Se a entrada for válida...
    # Para cada dificuldade na lista de dificuldades...
    for dificuldade in dificuldade_lista:
        # Se a dificuldade não for um número...
        if not dificuldade.isnumeric():
            entrada_valida = False  # Entrada será inválida
        # Caso contrário... (Se a dificuldade for um número)
        else:
            int_dificuldade = int(
                dificuldade
            )  # Transformar a dificuldade em um inteiro
            # Se a dificuldade for menor que 0 ou maior que 20...
            if int_dificuldade < 0 or int_dificuldade > 20:
                entrada_valida = False  # Entrada será inválida

    if (
        not entrada_valida
    ):  # Se a entrada for inválida... printar mensagem dos "sapecas"
        print(
            '"Uh, Phone Guy aqui. Os animatronics estão um pouco "sapecas" esta noite."'
        )
    else:  # Caso contrário... (Se a entrada for válida)
        # Transformar os valores da lista de dificuldades em inteiros
        lista_inteiros = []  # Lista para armazenar os inteiros
        for (
            dificuldade
        ) in dificuldade_lista:  # Para cada dificuldade na lista de dificuldades...
            lista_inteiros.append(
                int(dificuldade)
            )  # Adicionar o valor inteiro da dificuldade na lista de inteiros
        dificuldade_lista = (
            lista_inteiros  # Atualizar a lista de dificuldades para a lista de inteiros
        )

# Caso do "IT'S ME"
if entrada_valida:  # Se a entrada for válida...
    string_dificuldades = ""  # String para armazenar as dificuldades
    for (
        dificuldade
    ) in dificuldade_lista:  # Para cada dificuldade na lista de dificuldades...
        string_dificuldades += str(
            dificuldade
        )  # Adicionar o valor da dificuldade na string de dificuldades
    if (
        "1" in string_dificuldades
        and "9" in string_dificuldades
        and "8" in string_dificuldades
        and "7" in string_dificuldades
        and "0" in string_dificuldades
    ):  # Se a string de dificuldades tiver 1, 9, 8, 7 e 0...
        print('"IT\'S ME"')  # Printar a mensagem do "IT'S ME"
        jogo_segue = False  # O jogo não segue

# Caso do Golden Freddy na noite
golden_freddy_ativo = False  # Variável para verificar se o Golden Freddy está ativo
if entrada_valida and jogo_segue:  # Se a entrada for válida e o jogo seguir...
    numeros_golden = [
        1,
        7,
        8,
        9,
    ]  # Ordem crescente dos números de dificuldade para o Golden Freddy estar ativo
    dificuldades_ordenadas = sorted(
        dificuldade_lista
    )  # Ordenar a lista de dificuldades
    if (
        dificuldades_ordenadas == numeros_golden
    ):  # Se a lista de dificuldades ordenadas for igual à lista de números do Golden Freddy...
        golden_freddy_ativo = True  # Ativar o Golden Freddy


def simular_noite(hora, energia, niveis, golden_ativo):  # Função para simular a noite
    if energia <= 0:  # Se a energia for menor ou igual a 0...
        return None  # MORREU!!
    if hora == 6:  # Se a hora for 6...
        return [energia, ""]  # Retornar a energia e uma string vazia

    atacando_bonnie = (hora == 0) or (hora == 3)  # Bonnie ataca na hora 0 e 3
    atacando_chica = (hora == 1) or (hora == 4)  # Chica ataca na hora 1 e 4
    atacando_foxy = (hora == 4) and (
        energia > 50
    )  # Foxy ataca na hora 4 se a energia for maior que 50
    atacando_freddy = hora == 5  # Freddy ataca na hora 5
    atacando_golden_freddy = hora == 5  # Golden Freddy ataca na hora 5
    melhor_energia = -1  # Variável para armazenar a melhor energia
    melhor_configuracao = (
        None  # Variável para armazenar a melhor configuração [pe, pd, lz, cam]
    )

    # Para cada possibilidade de PE, PD, LZ e CAM...
    for pe in [0, 1]:
        for pd in [0, 1]:
            for lz in [0, 1]:
                for cam in [0, 1]:
                    sobreviveu = True  # Variável para verificar se sobreviveu
                    gasto_atual = 1 + (pe * 7) + (pd * 7) + (lz * 5) + (cam * 9)

                    # Verificar se conseguiu frustrar os ataques
                    if (
                        atacando_bonnie and niveis[0] > 0
                    ):  # Se o animatronic estiver atacando e a dificuldade dele for maior que 0...
                        if not (
                            (pe == 1) or (lz == 1 and cam == 0)
                        ):  # Se ele não fez o necessário para frustrar o ataque...
                            sobreviveu = False  # MORREU!!
                        else:  # Caso contrário... (Se ele fez o necessário para frustrar o ataque)
                            gasto_atual += 3 + (
                                niveis[0] * 0.25
                            )  # Adicionar o gasto de energia
                    if sobreviveu and atacando_chica and niveis[1] > 0:
                        if not ((pd == 1) or (cam == 1)):
                            sobreviveu = False
                        else:
                            gasto_atual += 2 + (niveis[1] * 0.35)
                    if sobreviveu and atacando_foxy and niveis[3] > 0:
                        if not (pe == 1):
                            sobreviveu = False
                        else:
                            gasto_atual += 5 + (niveis[3] * 0.15)
                    if sobreviveu and atacando_freddy and niveis[2] > 0:
                        if not (((pe == 1) and (pd == 1)) or (cam == 1)):
                            sobreviveu = False
                        else:
                            gasto_atual += 3 + (niveis[2] * 0.35)
                    if sobreviveu and atacando_golden_freddy and golden_ativo:
                        if not (cam == 1):
                            sobreviveu = False
                        else:
                            gasto_atual += 10 + (niveis[2] * 1.95)
                    # Se no final de tudo isso ele sobreviveu...
                    if sobreviveu:
                        # A nova energia será a energia atual menos o gasto atual
                        nova_energia = energia - gasto_atual
                        if (
                            nova_energia > melhor_energia
                        ):  # Se a nova energia for maior que a melhor energia...
                            melhor_energia = nova_energia  # Atualizar a melhor energia
                            melhor_configuracao = [
                                pe,
                                pd,
                                lz,
                                cam,
                            ]  # Atualizar a melhor configuração
    if melhor_configuracao == None:  # Se não houver melhor configuração...
        return None  # Retornar None

    pe_val, pd_val, lz_val, cam_val = (
        melhor_configuracao  # Pega os valores da melhor configuração
    )
    # Criar a linha atual
    pe_txt = (
        "SIM" if pe_val else "NÃO"
    )  # Se (opção) for verdadeira, o texto será "SIM", caso contrário, será "NÃO"
    pd_txt = "SIM" if pd_val else "NÃO"
    lz_txt = "SIM" if lz_val else "NÃO"
    cam_txt = "SIM" if cam_val else "NÃO"
    linha_atual = f"0{hora}:00 AM -> PE: {pe_txt} | PD: {pd_txt} | LZ: {lz_txt} | CAM: {cam_txt}\n"

    resultado_futuro = simular_noite(
        hora + 1, melhor_energia, niveis, golden_ativo
    )  # Simular a próxima hora

    if resultado_futuro:  # Se o resultado da próxima hora for válido... (não for None)
        energia_final = resultado_futuro[
            0
        ]  # A energia final será a energia do resultado da próxima hora
        texto_final = (
            linha_atual + resultado_futuro[1]
        )  # O texto final será a linha atual mais o texto do resultado da próxima hora
        return [energia_final, texto_final]  # Retornar a energia final e o texto final
    return None  # Retornar None se não sobreviver


if entrada_valida and jogo_segue:  # Se a entrada for válida e o jogo seguir...
    soma_dificuldades = sum(
        dificuldade_lista
    )  # Somar os valores da lista de dificuldades
    if soma_dificuldades == 0:  # Se a soma das dificuldades for 0...
        print('"Uh, olá? Olá? Phone Guy falando. Não tem ninguém aqui..."')
    else:  # Caso contrário... (Se a soma das dificuldades não for 0)
        resultado = simular_noite(
            0, 100, dificuldade_lista, golden_freddy_ativo
        )  # Simular a noite
        if resultado == None:  # Se o resultado for None...
            print(
                '"Uh, Phone Guy falando. Uh, não tem mais ninguém do outro lado, não é?"'
            )
        else:  # Caso contrário... (Se o resultado não for None)
            energia_final = resultado[0]  # Pegar a energia final do resultado
            print(
                f'"Uh, olá? Ei, wow, dia sete, parabéns. E ainda com {energia_final:.2f}% de energia. Eu sabia que você conseguiria."'
            )
            print(resultado[1].rstrip())  # Resultado[1]
