print("INICIANDO SIMULAÇÃO...")

# Validação do jogador inicial
jogador1 = input()
while jogador1 != "Arthur" and jogador1 != "Samuel":
    print("Jogador inválido! Essa competição é apenas entre Arthur e Samuel!")
    jogador1 = input()

print(f"{jogador1} começa na corda!")

# Definir jogador 2
if jogador1 == "Arthur":
    jogador2 = "Samuel"
else:
    jogador2 = "Arthur"

# Número de rodadas
qtd_rodadas = int(input())

# Pontuações
pontos_arthur = 0
pontos_samuel = 0

# Simular cada rodada
for rodada in range(1, qtd_rodadas + 1):
    print(f"Começa a {rodada}ª rodada!")

    # Verificar se é a última rodada
    if rodada == qtd_rodadas:
        print("Última rodada! Valendo 2 pontos!")

    # Ler ritmo e aposta
    ritmo = int(input())
    aposta = int(input())

    print(
        f"{jogador2} aposta que {jogador1} não chega a {aposta} pulos! Vamos ver se é verdade! O ritmo de {jogador1} será {ritmo}!"
    )

    # Variáveis da rodada
    pulos_restantes = aposta
    tropecos = 0
    ja_imprimiu_quase_la = False
    caiu = False  # Variável para controlar se o jogador caiu

    # Simular os pulos
    while pulos_restantes > 0 and tropecos < 3:
        # Somar algarismos do número de pulos restantes
        soma = 0
        temp = pulos_restantes
        while temp > 0:
            soma += temp % 10
            temp //= 10

        # Verificar se soma está na sequência de Fibonacci
        # Um número n está em Fibonacci se 5n²+4 ou 5n²-4 é quadrado perfeito
        valor1 = 5 * soma * soma + 4
        valor2 = 5 * soma * soma - 4

        # Verificar se é quadrado perfeito
        raiz1 = int(valor1**0.5)
        raiz2 = int(valor2**0.5)

        eh_fibonacci = (raiz1 * raiz1 == valor1) or (raiz2 * raiz2 == valor2)

        if eh_fibonacci:
            print(
                f"O número da soma é {soma}, que faz parte da sequência de Fibonacci!! {jogador1} tropeça!"
            )
            tropecos += 1
        else:
            # Verificar se está quase chegando (menos de 1/4 dos pulos)
            if pulos_restantes < aposta / 4 and not ja_imprimiu_quase_la:
                print(f"{jogador1} está quase chegando ao apostado! Falta pouco!")
                ja_imprimiu_quase_la = True
            else:
                print(f"{jogador1} pula com maestria! Faltam {pulos_restantes} pulos!")

        # Diminuir pulos restantes
        pulos_restantes -= ritmo

    # Verificar se caiu por 3 tropeços
    if tropecos == 3:
        print(f"E agora não tem jeito, {jogador1} cai de cara no chão!")
        caiu = True

    pulos_realizados = aposta - pulos_restantes

    # PRIMEIRO, verifica se o jogador NÃO caiu e se atingiu a meta.
    if not caiu and pulos_realizados >= aposta:
        # Se não caiu e atingiu a meta, ele pontua.
        if pulos_realizados == aposta:
            print(
                f"{jogador1} cumpriu o prometido e alcançou {aposta} pulos! Ponto merecidíssimo!"
            )
        else:  # Superou a aposta
            diferenca = pulos_realizados - aposta
            print(
                f"{jogador1} vai além, e supera a aposta em {diferenca} Ponto(s)! Deixou o {jogador2} no chinelo!"
            )

        # Atribuir pontos
        pontos_a_somar = 2 if rodada == qtd_rodadas else 1
        if jogador1 == "Arthur":
            pontos_arthur += pontos_a_somar
        else:
            pontos_samuel += pontos_a_somar

    # exibe uma mensagem de performance baseada no quão perto ele chegou.
    else:
        if pulos_realizados < aposta / 2:
            print(
                f"Nossa!! Parece que {jogador1} não chegou nem na metade do apostado! Ainda bem que não foi competir pra valer no Round 6!"
            )
        elif pulos_realizados < aposta * 3 / 4:
            print(
                f"Nem muito perto, nem muito longe do apostado. Talvez {jogador1} teve apenas azar!"
            )
        elif pulos_realizados < aposta:
            print(f"Quase lá! por pouco {jogador1} não alcançou o apostado!")
        # Não há 'else' aqui, pois o caso de ter alcançado a aposta já foi tratado no primeiro 'if'.

    # Alternar jogadores para a próxima rodada
    temp = jogador1
    jogador1 = jogador2
    jogador2 = temp

# Resultado final
print("COMPUTANDO PREVISÃO FINAL...")

if pontos_arthur > pontos_samuel:
    print(
        f"Arthur venceu a competição com {pontos_arthur} ponto(s)! Trouxe orgulho para Maceió!"
    )
elif pontos_samuel > pontos_arthur:
    print(
        f"Samuel venceu a competição com {pontos_samuel} ponto(s)! O Messi careca em sua foto de perfil ficaria impressionado se soubesse!"
    )
elif pontos_arthur > 0:  # Caso de empate com pontos
    print(
        f"Houve um empate técnico! Ambos fizeram {pontos_arthur} ponto(s)! Óbvio que os dois monitores mais rápidos iriam empatar!"
    )
else:  # Empate sem pontos
    print(
        "Ninguém pontuou! Que competição sem graça! Acho que os monitores se garantem mais nas dúvidas de IP mesmo..."
    )
