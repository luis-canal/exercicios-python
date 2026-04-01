#01 - Padronizador de produtos -  setor de e-comerce
# produtos_baguncados = ["iphone 13", "AiRpOdS Pro", "iPad mini", "caixa de som bluetooth"]
# def padronizar_texto(texto):
#     texto = texto.strip().title()
#     return texto

# for produto in produtos_baguncados:
#     produto_padronizado = padronizar_texto(produto)
#     print(produto_padronizado)

#02 - Calculadora de imposto sobre serviço - setor fiscal
# def calcular_iss(valor):
#     if valor > 5000:
#         taxa = 0.05
#     else:
#         taxa = 0.03
#     imposto = valor * taxa
#     print("O valor do imposto é: ", imposto)
# calcular_iss(8000)
# calcular_iss(2000)

#03 - Analisador de margem de lucro - setor financeiro
# def analisar_margem(fat, custo):
#     lucro = fat - custo
#     margem = lucro / fat
#     if margem >= 0.3:
#         print("Margem saudável")
#     else:
#         print("Margem baixa")

# analisar_margem(10000, 6000)

#04 - Verificador de meta de vendedores - setor comercial
# dic_vendedores = {"João": 12000, "Maria": 8000, "José": 10000}
# meta = 10000
# def bateu_meta(vendas_vendedores: dict, meta: float):
#     for vendedor in vendas_vendedores:
#         if vendas_vendedores[vendedor] >= meta:
#             print(f"Vendedor {vendedor} bateu a meta!")
#         else:
#             print(f"Vendedor {vendedor} NÃO bateu a meta!")

# bateu_meta(dic_vendedores, meta)

#05 - Conversor de moeda interativo - setor de importação
def converter_real(valor_dolares, cotacao_dolar):
    valor_em_real = valor_dolares * cotacao_dolar
    return valor_em_real

precos_usd = [100, 50, 250]
precos_real = []
def processar_precos(precos: list, cotacao):
    for i in precos:
        valor = converter_real(i, cotacao)
        precos_real.append(valor)
    print(precos_real)

processar_precos(precos_usd, 5.20)