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
