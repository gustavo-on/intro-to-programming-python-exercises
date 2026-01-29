"""
Questão: Pula Cin!

Enunciado:
Simulação de uma competição de pular corda entre Arthur e Samuel (Round 6).
O programa deve gerenciar rodadas, apostas, ritmos de pulo e penalidades baseadas na Sequência de Fibonacci.

Lógica Principal:
1. Validação de Loop: O jogo só aceita "Arthur" ou "Samuel".
2. Loop de Rodadas:
   - Alternância de quem está pulando.
   - Cálculo de pontos (peso 2 na última rodada).
3. Loop de Pulos (dentro da rodada):
   - O loop ocorre enquanto houver pulos restantes e tropeços < 3.
   - Soma dos algarismos dos pulos restantes.
   - Verificação de Fibonacci: (5*n^2 + 4) ou (5*n^2 - 4) é quadrado perfeito.
   - Se Fibonacci: Tropeça.
   - Se não: Imprime status ("Maestria" ou "Quase lá").
   - Subtrai o ritmo dos pulos restantes.
4. Pós-Rodada:
   - Verifica se caiu (3 tropeços).
   - Verifica se cumpriu a aposta e calcula pontuação.
   - Imprime mensagens de desempenho baseadas na porcentagem concluída.
5. Resultado Final: Compara pontuações e declara o vencedor.

Input:
- Nome inicial, Qtd Rodadas, Pares de Ritmo/Aposta.

Output:
- Mensagens passo a passo da simulação e placar final.
"""

print("INICIANDO SIMULAÇÃO...")

# --- 1. VALIDAÇÃO DO JOGADOR INICIAL ---
jogador1 = input()
while jogador1 != "Arthur" and jogador1 != "Samuel":
    print("Jogador inválido! Essa competição é apenas entre Arthur e Samuel!")
    jogador1 = input()

print(f"{jogador1} começa na corda!")

# Define o jogador 2 baseado na escolha inicial
if jogador1 == "Arthur":
    jogador2 = "Samuel"
else:
    jogador2 = "Arthur"

# --- 2. CONFIGURAÇÃO DA PARTIDA ---
qtd_rodadas = int(input())
pontos_arthur = 0
pontos_samuel = 0

# --- 3. LOOP DE RODADAS ---
for rodada in range(1, qtd_rodadas + 1):
    print(f"Começa a {rodada}ª rodada!")

    # Verifica se é a rodada final (pontuação dobrada)
    if rodada == qtd_rodadas:
        print("Última rodada! Valendo 2 pontos!")

    # Inputs da rodada específica
    ritmo = int(input())
    aposta = int(input())

    print(
        f"{jogador2} aposta que {jogador1} não chega a {aposta} pulos! Vamos ver se é verdade! O ritmo de {jogador1} será {ritmo}!"
    )

    # Variáveis de controle da rodada
    pulos_restantes = aposta
    tropecos = 0
    ja_imprimiu_quase_la = False
    caiu = False  # Flag para saber se a rodada acabou por queda

    # --- 4. LOOP DE PULOS (A AÇÃO) ---
    # Continua enquanto faltar pulos E o jogador não tiver caído 3 vezes
    while pulos_restantes > 0 and tropecos < 3:

        # A. Soma dos algarismos
        soma = 0
        temp = pulos_restantes
        while temp > 0:
            soma += temp % 10
            temp //= 10

        # B. Verificação Fibonacci (Método do Quadrado Perfeito)
        # Um número n é Fibonacci se 5n^2 + 4 ou 5n^2 - 4 for quadrado perfeito
        valor1 = 5 * soma * soma + 4
        valor2 = 5 * soma * soma - 4

        raiz1 = int(valor1**0.5)
        raiz2 = int(valor2**0.5)

        eh_fibonacci = (raiz1 * raiz1 == valor1) or (raiz2 * raiz2 == valor2)

        if eh_fibonacci:
            print(
                f"O número da soma é {soma}, que faz parte da sequência de Fibonacci!! {jogador1} tropeça!"
            )
            tropecos += 1
        else:
            # C. Verificação de progresso ("Quase lá" vs "Maestria")
            # Só imprime "quase chegando" se for < 1/4 da aposta e ainda não tiver impresso
            if pulos_restantes < aposta / 4 and not ja_imprimiu_quase_la:
                print(f"{jogador1} está quase chegando ao apostado! Falta pouco!")
                ja_imprimiu_quase_la = True
            else:
                print(f"{jogador1} pula com maestria! Faltam {pulos_restantes} pulos!")

        # D. Decremento (o pulo acontece aqui)
        pulos_restantes -= ritmo

    # --- 5. RESULTADO DA RODADA ---

    # Verifica queda fatal
    if tropecos == 3:
        print(f"E agora não tem jeito, {jogador1} cai de cara no chão!")
        caiu = True

    # Calcula quantos pulos foram feitos efetivamente
    # Nota: pulos_restantes pode ser negativo se o ritmo ultrapassar o 0,
    # então aposta - pulos_restantes dá o total percorrido corretamente.
    pulos_realizados = aposta - pulos_restantes

    # Lógica de Pontuação e Mensagens Finais da Rodada
    # Só pontua se NÃO caiu e se atingiu/superou a meta
    if not caiu and pulos_realizados >= aposta:
        if pulos_realizados == aposta:
            print(
                f"{jogador1} cumpriu o prometido e alcançou {aposta} pulos! Ponto merecidíssimo!"
            )
        else:  # Superou
            diferenca = pulos_realizados - aposta
            print(
                f"{jogador1} vai além, e supera a aposta em {diferenca} Ponto(s)! Deixou o {jogador2} no chinelo!"
            )

        # Atribuição de pontos
        pontos_a_somar = 2 if rodada == qtd_rodadas else 1
        if jogador1 == "Arthur":
            pontos_arthur += pontos_a_somar
        else:
            pontos_samuel += pontos_a_somar

    else:
        # Mensagens de falha baseadas na porcentagem concluída
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
        # Se caiu mas tinha superado a aposta (caso raro onde tropeça no último),
        # a lógica cai aqui ou no if anterior? O enunciado diz "Após 3 tropeços... sua vez se encerra".
        # Assumimos que cair invalida o sucesso.

    # Alternância de Jogadores para a próxima iteração
    temp = jogador1
    jogador1 = jogador2
    jogador2 = temp

# --- 6. PREVISÃO FINAL ---
print("COMPUTANDO PREVISÃO FINAL...")

if pontos_arthur > pontos_samuel:
    print(
        f"Arthur venceu a competição com {pontos_arthur} ponto(s)! Trouxe orgulho para Maceió!"
    )
elif pontos_samuel > pontos_arthur:
    print(
        f"Samuel venceu a competição com {pontos_samuel} ponto(s)! O Messi careca em sua foto de perfil ficaria impressionado se soubesse!"
    )
elif pontos_arthur > 0:  # Empate com pontos
    print(
        f"Houve um empate técnico! Ambos fizeram {pontos_arthur} ponto(s)! Óbvio que os dois monitores mais rápidos iriam empatar!"
    )
else:  # Empate zerado
    print(
        "Ninguém pontuou! Que competição sem graça! Acho que os monitores se garantem mais nas dúvidas de IP mesmo..."
    )
