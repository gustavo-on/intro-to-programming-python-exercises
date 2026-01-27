"""
Questão: Oferenda

Enunciado:
Tantan precisa de uma quantidade D de diamantes.
Três amigos fizeram ofertas para ele morar em suas vilas:
- Arthur: oferece 10 diamantes.
- Luiz: oferece 30 diamantes.
- Pedro: oferece 100 diamantes.

Tantan deve aceitar a oferta que supra sua necessidade (D), escolhendo a menor oferta possível entre as que atendem.
Se nenhuma oferta for suficiente (D > 100), ele responde "Nenhum".

Entrada:
- D (int): Quantidade de diamantes necessária.

Saída:
- Nome do amigo cuja oferta foi aceita ou "Nenhum".
"""

D = int(input())

# A verificação deve ser feita em ordem crescente (do menor para o maior)
# para garantir que Tantan pegue a menor oferta suficiente.

if D <= 10:
    print("Arthur")
elif D <= 30:
    print("Luiz")
elif D <= 100:
    print("Pedro")
else:
    print("Nenhum")
