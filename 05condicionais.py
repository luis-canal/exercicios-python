#01 - Validação de investimento
valor = input("Qual valor deseja investir(ex. R$5.000,00)?  ")
valor = float(valor.replace("R$", "").replace(".", "").replace(",", "."))

if valor < 0:
    print("valor deve ser maior que zero")
elif valor < 1000:
    print("Perfil iniciante: sugerimos tesouro direto")
elif valor >= 1000 and valor < 5000:
    print("Perfil moderado: sujerimos fundos imobiliários")
else:
    print("Perfil arrojado: seujerimos ações")

