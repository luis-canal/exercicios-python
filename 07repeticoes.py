#01 - Automação de convites
for i in range(11):
    falta = 10 - i
    if falta > 1:
        print(f"Faltam {falta} minutos para começar a reunião")
    elif falta == 1:
        print(f"Falta {falta} minuto para começar a reunião")
    else:
        print("Reunião começou!!")