"""
Questão: Nickname

Enunciado:
O programa deve gerar um nickname para o jogo Minecraft unindo o primeiro nome e o sobrenome do usuário.
A regra principal é que não pode haver espaços entre os nomes.
O sistema garante que a soma dos caracteres estará dentro do limite permitido (3 a 16).

Entrada:
- N (str): Primeiro nome.
- S (str): Sobrenome.

Saída:
- O nickname formado pela concatenação direta do nome e sobrenome.
"""

N = input()
S = input()

# Concatenação de strings: junta o primeiro com o segundo sem espaços
nickname = N + S

print(nickname)
