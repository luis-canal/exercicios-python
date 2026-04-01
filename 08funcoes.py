#01 - Padronizador de produtos -  setor de e-comerce
# produtos_baguncados = ["iphone 13", "AiRpOdS Pro", "iPad mini", "caixa de som bluetooth"]
# def padronizar_texto(texto):
#     texto = texto.strip().title()
#     return texto

# for produto in produtos_baguncados:
#     produto_padronizado = padronizar_texto(produto)
#     print(produto_padronizado)

#02 - Calculadora de imposto sobre serviço - setor fiscal
def calcular_iss(valor):
    if valor > 5000:
        taxa = 0.05
    else:
        taxa = 0.03
    imposto = valor * taxa
    print("O valor do imposto é: ", imposto)
calcular_iss(8000)
calcular_iss(2000)


