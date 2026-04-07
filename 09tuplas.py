#01 - Localização de entregas - setor de logística
# coordenadas = (-25.9965, -54.7863)
# latitude, longitude = coordenadas #unpacking
# print(f"Latitude: {latitude} e Longitude: {longitude}")

#02 - Resumo de folha de pagamento - setor de RH
def  calcular_folha(salario):
    perc_desconto = 0.1
    desconto = perc_desconto * salario
    salario_liq = salario - desconto
    return desconto, salario_liq

desconto, salario_liquido = calcular_folha(10000)
print(f"Desconto: {desconto} | Salário liquído: {salario_liquido}")