"""
Questão: Ted Mosby e a Teoria do Guarda-Chuva Amarelo

Enunciado:
O programa calcula a distância entre Ted e o Guarda-Chuva Amarelo e ajusta esse valor
dependendo do amigo que o acompanha (Barney, Marshall, Lily ou Robin).
Ao final, exibe a distância arredondada e uma mensagem baseada no sucesso da busca.

Cálculos:
1. Distância Euclidiana: √((x2 - x1)² + (y2 - y1)²)
2. Ajustes por Amigo:
   - Barney: +10 (aventura longa)
   - Marshall: -5 (ajuda a chegar)
   - Lily: -10 (atalhos)
   - Robin: +5 (independente/imprevisto)

Regras de Saída:
- Se distancia_final <= 50: Mensagem de sucesso (encontraram).
- Se distancia_final > 50: Mensagem de falha/outra aventura.

Input:
- Coordenadas de Ted (x1, y1) e do Guarda-Chuva (x2, y2).
- Nome do amigo.

Output:
- Valor da distância final arredondada.
- Mensagem de contexto.
"""

# --- INPUTS ---
x1 = int(input())  # X Ted
y1 = int(input())  # Y Ted
x2 = int(input())  # X guarda-chuva
y2 = int(input())  # Y guarda-chuva
amigoz = input()

# Tratamento da string (garante inicial maiúscula)
amigo = amigoz.capitalize()

# --- CÁLCULO DA DISTÂNCIA EUCLIDIANA ---
distancia_original = (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5

# --- LÓGICA POR AMIGO (AJUSTE DE DISTÂNCIA E MENSAGENS) ---
if amigo == "Barney":
    # Barney aumenta a distância (+10)
    distancia_final = distancia_original + 10
    texto1 = "Nossa, eu sou incrível! Vimos o guarda-chuva em 5 minutos. Tão lendário que eu poderia até ter pego ele pra mim! Desafio aceito!"
    texto2 = "Esse não era o caminho para o guarda-chuva, mas com certeza é o caminho para uma noite lendária! Challenge accepted, vista seu terno!"

elif amigo == "Marshall":
    # Marshall diminui a distância (-5)
    distancia_final = distancia_original - 5
    texto1 = "Obrigado pela ajuda, Marsh! Tão bom saber que a gente pode contar com os amigos pra achar a nossa cara-metade. Encontramos o guarda-chuva!"
    texto2 = "Tudo bem, cara. O destino é paciente. O importante é que estamos juntos nessa. Vamos tentar de novo amanhã."

elif amigo == "Lily":
    # Lily diminui muito a distância (-10) com atalhos
    distancia_final = distancia_original - 10
    texto1 = "Ah! Não te falei? Peguei um atalho! Lilypad sabe das coisas. O guarda-chuva está aqui, e nem nos cansamos muito!"
    texto2 = "Isso não faz sentido! Meu atalho deveria ter funcionado! Que saco! Fiquei com fome de tanta caminhada."

else:
    # Robin (ou qualquer outro) aumenta um pouco (+5)
    distancia_final = distancia_original + 5
    texto1 = "Bem... acho que isso realmente aconteceu. Nem foi tão difícil assim. O guarda-chuva está bem aqui, Ted. Onde está o mistério?"
    texto2 = "Sério, Ted? Um guarda-chuva? O destino é um conceito abstrato."

# --- SAÍDA DE DADOS ---
# Imprime a distância arredondada (round)
print(f"Pelos meus cálculos a distância final encontrada foi {round(distancia_final)}!")

# Verifica o sucesso da busca baseada na distância final
if distancia_final <= 50:
    print(f"{texto1}")
else:
    print(f"{texto2}")
