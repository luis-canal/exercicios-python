#01 Atualização de cadastro de clientes
# clientes = {"Lira": 5000, "Alon": 3000, "Julia": 4500}
# nova_compra = 1500
# clientes["Alon"] = clientes["Alon"] + nova_compra
# clientes["Marcos"] = 2000
# print(clientes)

#02 - Consulta de estoque
estoque = {"teclado": 50, "mouse": 30, "monitor": 45}
produto = input("Digite o produto: ")
produto = produto.lower().strip()
if produto in estoque:
    print(f"Produto: {produto}, Quantidade: {estoque[produto]}")
else:
    print("Produto não encontrado")