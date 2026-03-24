#01 - Validação de investimento
# valor = input("Qual valor deseja investir(ex. R$5.000,00)?  ")
# valor = float(valor.replace("R$", "").replace(".", "").replace(",", "."))

# if valor < 0:
#     print("valor deve ser maior que zero")
# elif valor < 1000:
#     print("Perfil iniciante: sugerimos tesouro direto")
# elif valor >= 1000 and valor < 5000:
#     print("Perfil moderado: sujerimos fundos imobiliários")
# else:
#     print("Perfil arrojado: seujerimos ações")

#02 - Controle de acesso ao sistema
# admins = ["ana@empresa.com", "rafael@empresa.com", "marcionic@empresa.com"]
# email = input("Insira seu email: ")
# email = email.lower().strip()

# if email in admins:
#     print("Parabéns, acesso permitido!")
# else:
#     print("Acesso negado!")

#03 - Cálculo de desconto progressivo
# valor_carrinho = input("Valor do carrinho: ")
# valor_carrinho = float(valor_carrinho.replace("R$", "").replace(".", "").replace(",", "."))
# if valor_carrinho >= 500:
#     desconto = valor_carrinho * 0.15
#     valor_carrinho = valor_carrinho - desconto
#     print(f"Desconto: R${desconto:,.2f}")
#     print(f"Valor do carrinho: R${valor_carrinho:,.2f}")
# elif valor_carrinho >= 200:
#     desconto = valor_carrinho * 0.10
#     valor_carrinho = valor_carrinho - desconto
#     print(f"Desconto: R${desconto:,.2f}")
#     print(f"Valor do carrinho: R${valor_carrinho:,.2f}")
# else:
#     desconto = 0
#     print(f"Desconto: R${desconto:,.2f}")
#     print(f"Valor do carrinho: R${valor_carrinho:,.2f}")

#04 - Análise de metas combinadas 
meta_vendedor = float(input("Meta vendedor: "))
vendas_vendedor = float(input("Vendas do vendedor: "))
meta_loja = float(input("Meta loja: "))
vendas_loja = float(input("Vendas da loja: "))

if vendas_loja > meta_loja and vendas_vendedor > meta_vendedor:
    bonus = vendas_vendedor * 0.2
else:
    bonus = 0

print(f"Seu bônus é R${bonus:,.2f}")