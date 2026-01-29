"""
Título: Uma Noite com o Frederico!

Resumo do problema:
O desafio consiste em simular uma noite do jogo Five Nights at Freddy’s, buscando a melhor sequência
de decisões horárias (portas, luzes e câmera) que permita ao personagem sobreviver até as 6h com a
maior quantidade possível de energia restante. A simulação deve considerar ataques de animatrônicos,
custos energéticos fixos e variáveis, além de casos especiais como a presença do Golden Freddy.

Regras de aprovação / lógica principal:
- A entrada deve conter exatamente quatro valores inteiros entre 0 e 20; caso contrário, é inválida.
- Se todas as dificuldades forem 0, não há animatrônicos e a noite termina imediatamente.
- A cada hora (0h a 5h), decisões são tomadas simultaneamente e afetam o consumo de energia.
- Ataques devem ser corretamente frustrados; falhar em qualquer ataque resulta em morte.
- O algoritmo utiliza recursão para simular hora a hora e escolher a configuração que maximiza a energia.
- Vitória ocorre apenas se o personagem alcançar 6h com energia maior que 0.

Entradas:
- Uma linha com quatro números inteiros separados por espaço, representando as dificuldades de
  Bonnie, Chica, Freddy e Foxy.

Saídas:
- Mensagens específicas para entrada inválida, ausência de animatrônicos, derrota ou vitória.
- Em caso de vitória, impressão da energia final (com duas casas decimais) e da sequência horária
  de decisões adotadas.
"""

# Input:
niveis_dificuldade = input()

entrada_valida = True  # Controla se a análise pode prosseguir
jogo_segue = True  # Controla se a simulação da noite será executada
dificuldade_lista = (
    niveis_dificuldade.split()
)  # Quebra a entrada em valores individuais

# Decisão: quantidade incorreta de valores invalida a entrada
if len(dificuldade_lista) != 4:
    print('"Uh, Phone Guy aqui. Os animatronics estão um pouco "sapecas" esta noite."')
    entrada_valida = False

# Decisão: validação de tipo e faixa dos valores
if entrada_valida:
    for dificuldade in dificuldade_lista:
        if (
            not dificuldade.isnumeric()
        ):  # Valor não numérico compromete toda a simulação
            entrada_valida = False
        else:
            int_dificuldade = int(dificuldade)
            if int_dificuldade < 0 or int_dificuldade > 20:  # Fora da faixa permitida
                entrada_valida = False

    if not entrada_valida:
        print(
            '"Uh, Phone Guy aqui. Os animatronics estão um pouco "sapecas" esta noite."'
        )
    else:
        # Conversão definitiva para inteiros após validação completa
        lista_inteiros = []
        for dificuldade in dificuldade_lista:
            lista_inteiros.append(int(dificuldade))
        dificuldade_lista = lista_inteiros

# Decisão: caso especial do "IT'S ME" encerra o programa imediatamente
if entrada_valida:
    string_dificuldades = ""
    for dificuldade in dificuldade_lista:
        string_dificuldades += str(dificuldade)
    if (
        "1" in string_dificuldades
        and "9" in string_dificuldades
        and "8" in string_dificuldades
        and "7" in string_dificuldades
        and "0" in string_dificuldades
    ):
        print('"IT\'S ME"')
        jogo_segue = False

# Decisão: ativação do Golden Freddy apenas para o anagrama exato de 1,7,8,9
golden_freddy_ativo = False
if entrada_valida and jogo_segue:
    numeros_golden = [1, 7, 8, 9]
    dificuldades_ordenadas = sorted(dificuldade_lista)
    if dificuldades_ordenadas == numeros_golden:
        golden_freddy_ativo = True


def simular_noite(hora, energia, niveis, golden_ativo):
    # Decisão: energia zerada implica morte imediata
    if energia <= 0:
        return None
    # Decisão: alcançar 6h encerra a recursão com sucesso
    if hora == 6:
        return [energia, ""]

    # Definição dos ataques por hora segue regras fixas do problema
    atacando_bonnie = (hora == 0) or (hora == 3)
    atacando_chica = (hora == 1) or (hora == 4)
    atacando_foxy = (hora == 4) and (
        energia > 50
    )  # Condição extra baseada na energia atual
    atacando_freddy = hora == 5
    atacando_golden_freddy = hora == 5

    melhor_energia = -1  # Referência para maximizar energia restante
    melhor_configuracao = None

    # Exploração exaustiva das decisões possíveis (backtracking implícito)
    for pe in [0, 1]:
        for pd in [0, 1]:
            for lz in [0, 1]:
                for cam in [0, 1]:
                    sobreviveu = True
                    # Cálculo do custo base: gasto fixo por hora + ferramentas ativadas
                    gasto_atual = 1 + (pe * 7) + (pd * 7) + (lz * 5) + (cam * 9)

                    # Decisão: cada bloco avalia se o ataque é frustrado; falha implica morte
                    if atacando_bonnie and niveis[0] > 0:
                        if not ((pe == 1) or (lz == 1 and cam == 0)):
                            sobreviveu = False
                        else:
                            gasto_atual += 3 + (
                                niveis[0] * 0.25
                            )  # Custo variável por dificuldade

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

                    # Cálculo da energia restante após todas as penalidades
                    if sobreviveu:
                        nova_energia = energia - gasto_atual
                        if nova_energia > melhor_energia:
                            melhor_energia = nova_energia
                            melhor_configuracao = [pe, pd, lz, cam]

    # Decisão: nenhuma configuração viável implica morte
    if melhor_configuracao is None:
        return None

    pe_val, pd_val, lz_val, cam_val = melhor_configuracao

    # Conversão da melhor decisão para o formato textual exigido
    pe_txt = "SIM" if pe_val else "NÃO"
    pd_txt = "SIM" if pd_val else "NÃO"
    lz_txt = "SIM" if lz_val else "NÃO"
    cam_txt = "SIM" if cam_val else "NÃO"
    linha_atual = f"0{hora}:00 AM -> PE: {pe_txt} | PD: {pd_txt} | LZ: {lz_txt} | CAM: {cam_txt}\n"

    # Chamada recursiva avança a simulação para a próxima hora
    resultado_futuro = simular_noite(hora + 1, melhor_energia, niveis, golden_ativo)

    if resultado_futuro:
        energia_final = resultado_futuro[0]
        texto_final = linha_atual + resultado_futuro[1]
        return [energia_final, texto_final]
    return None


if entrada_valida and jogo_segue:
    soma_dificuldades = sum(
        dificuldade_lista
    )  # Avalia se existe ao menos um animatrônico ativo
    if soma_dificuldades == 0:
        print('"Uh, olá? Olá? Phone Guy falando. Não tem ninguém aqui..."')
    else:
        resultado = simular_noite(0, 100, dificuldade_lista, golden_freddy_ativo)
        if resultado is None:
            print(
                '"Uh, Phone Guy falando. Uh, não tem mais ninguém do outro lado, não é?"'
            )
        else:
            energia_final = resultado[0]
            print(
                f'"Uh, olá? Ei, wow, dia sete, parabéns. E ainda com {energia_final:.2f}% de energia. Eu sabia que você conseguiria."'
            )
            print(resultado[1].rstrip())
