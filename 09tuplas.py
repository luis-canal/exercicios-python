#01 - Localização de entregas - setor de logística
# coordenadas = (-25.9965, -54.7863)
# latitude, longitude = coordenadas #unpacking
# print(f"Latitude: {latitude} e Longitude: {longitude}")

#02 - Resumo de folha de pagamento - setor de RH
# def  calcular_folha(salario):
#     perc_desconto = 0.1
#     desconto = perc_desconto * salario
#     salario_liq = salario - desconto
#     return desconto, salario_liq

# desconto, salario_liquido = calcular_folha(10000)
# print(f"Desconto: {desconto} | Salário liquído: {salario_liquido}")

#03 - Processamento de vendas por unidade - setor comercial
# vendas_dia = [("monitor", 900, 25), ("teclado", 150, 40), ("mouse", 90, 36)]
# for i in vendas_dia:
#     produto = i[0]
#     preco = i[1]
#     qtde = i[2]
#     print(f"Produto: {produto} | Preço: {preco} | Quantidade: {qtde} | Total: {preco * qtde}")

#04 - Processamento de vendas regionais - setor de dashboard
dados_filias = {"Matriz": [10000, 20000, 15000],
                "Filial Norte": [7000, 3000, 19000],
                "Filial Sul": [13000, 20000],}

def analisar_vendas(lista_vendas):
    total_vendas = sum(lista_vendas)
    media_vendas = total_vendas / len(lista_vendas)
    return total_vendas, media_vendas

for f in dados_filias:
    vendas_filial = dados_filias[f]
    total_vendas_filial, media_vendas_filial = analisar_vendas(vendas_filial)
    print(f"Filial -> {f}: Total de vendas: {total_vendas_filial} | Media de vendas: {media_vendas_filial}")
