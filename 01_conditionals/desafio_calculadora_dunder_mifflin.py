"""
Questão: O Desafio da Calculadora na Dunder Mifflin

Enunciado:
Criar uma calculadora que realize as 4 operações básicas (+, -, *, /) entre dois números inteiros.
Restrições:
1. O código deve ter no MÁXIMO 3 linhas.
2. Divisão por zero é considerada inválida.
3. Operadores desconhecidos são inválidos.
4. Em caso de erro (operador inválido ou div por 0), imprimir a mensagem de sabotagem do Jim.

Entrada:
- x (int): Primeiro número.
- operador (str): O símbolo da operação.
- y (int): Segundo número.

Saída:
- O resultado da operação (int) OU a mensagem de erro específica.
"""

x, op, y = int(input()), input(), int(input())
msg = "Alerta! Alguém tentou usar um operador que não existe. Só um idiota faria isso. Provavelmente o Jim. Isso é claramente uma tentativa de sabotagem corporativa."
print(
    x + y
    if op == "+"
    else (
        x - y
        if op == "-"
        else x * y if op == "*" else x // y if op == "/" and y != 0 else msg
    )
)
