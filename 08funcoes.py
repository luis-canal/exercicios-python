#01 - Padronizador de produtos -  setor de e-comerce
produtos_baguncados = ["iphone 13", "AiRpOdS Pro", "iPad mini", "caixa de som bluetooth"]
def padronizar_texto(texto):
    texto = texto.strip().title()
    return texto

for produto in produtos_baguncados:
    produto_padronizado = padronizar_texto(produto)
    print(produto_padronizado)