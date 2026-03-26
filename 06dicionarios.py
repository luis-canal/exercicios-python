#01 Atualização de cadastro de clientes
clientes = {"Lira": 5000, "Alon": 3000, "Julia": 4500}
nova_compra = 1500
clientes["Alon"] = clientes["Alon"] + nova_compra
clientes["Marcos"] = 2000
print(clientes)

#02 - Consulta de estoque
estoque = {"teclado": 50, "mouse": 30, "monitor": 45}
produto = input("Digite o produto: ")
produto = produto.lower().strip()
if produto in estoque:
    print(f"Produto: {produto}, Quantidade: {estoque[produto]}")
else:
    print("Produto não encontrado")

#03 - Análise de faturamento por região
vendas_regiao = {"Norte": 1500,
                 "Sul": 4600,
                 "Leste": 1300,
                 "Oeste": 5500,}
lista_vendas = list(vendas_regiao.values())
total_valor = sum(lista_vendas)
total_regioes = len(lista_vendas)
media = total_valor / total_regioes
print("Valor total de vendas: ", total_valor)
print("Média de vendas entre as regiões: ", media)

#04 - Avaliação de desempenho
desempenho = {"Gui": [7, 8, 9], "Kaili": [5, 9, 7], "Tiago": [6, 7, 8]}
nome = input("Digite um nome: ")
nota_nome = desempenho[nome]
print(f"\n =={nome}==")
print("Notas: ", nota_nome)
media = sum(nota_nome) / len(nota_nome)
print("Média: ", media)

#05 - Limpeza de banco de dados
estoque = {"celular": 400, "câmera": 130, "rádio": 19, "telefone": 300}
print(estoque)
estoque.pop("rádio")
print(estoque)
celular_esta = "celular" in estoque
print("celular no estoque: ", celular_esta)