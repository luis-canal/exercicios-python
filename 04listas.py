#01 - Dashboard
vendas = [1500, 2000, 800, 3500, 1200]
total_vendas = sum(vendas)
quantidade_dias = len(vendas)
media = total_vendas / quantidade_dias

maior_venda = max(vendas)
menor_venda = min(vendas)
print(f"Total de vendas: {total_vendas}, média diaria de vendas: {media}, \
      maior venda: {maior_venda}, menor venda: {menor_venda}")

#02 - Gestão de estoque
estoque = ["monitor", "teclado", "mouse", "headset"]
def adicionar(item):
    estoque.append(str(item))
    print(f"item: {item} adicionado com sucesso")
    print(estoque)

def alterar(item, novo_item):
    posicao = estoque.index(item)
    estoque[posicao] = str(novo_item)
    print(f"item: {item} alterado com sucesso para {novo_item}")
    print(estoque)

def verificar(item):
    item_no_estoque = item in estoque
    print(f"Item está no estoque? {item_no_estoque}")
    print(estoque)

def remover(item):
    estoque.remove(item)
    print(f"Item {item} removido com sucesso")
    print(estoque)

adicionar("webcam")
alterar("teclado", "teclado mec")
verificar("impressora")
remover("mouse")

#03 - Organização de preços
fretes = [50, 80, 20, 150, 40]
fretes.sort(reverse=True)
top_fretes = fretes[:2]
print(f"Fretes: {fretes}")
print(f"Top fretes: {top_fretes}")

#04 - Sistema de logística
rota = ["São Paulo", "Campinas", "Jundiaí", "Sorocaba"]
novas = ["Itu", "Valinhos"]
rota.extend(novas)
posicao_sorocaba = rota.index("Sorocaba") + 1
print(f"Lista completa: {rota}")
print(f"Sorocaba é a {posicao_sorocaba}a cidade da rota")

#05 - Atualização interativa
import time, os
precos = [100.0, 250.0, 500.0]
vinhos = ["Branco", "Tinto", "Champagne"]
while True:
    print("""
1 - Adicionar vinho
2 - Alterar vinho
3 - Sair
""")
    opcao = int(input("opcao selecionada: "))
    if opcao == 1:
        os.system("cls")
        vinho = input("Nome do vinho: ")
        preco = float(input("preco: "))
        vinhos.append(vinho)
        precos.append(preco)
        print("vinho adicionado com sucesso")
        print(f"lista de vinhos: {vinhos}")
        print(f"lista de precos: {precos}")
        time.sleep(2)
        os.system("cls")
    elif opcao == 2:
        os.system("cls")
        vinho_alterado = input("Nome do vinho a ser alterado: ")
        novo_preco = float(input("Novo preco: "))
        posicao = vinhos.index(vinho_alterado)
        precos[posicao] = novo_preco
        print("vinho alterado com sucesso")
        print(f"lista de vinhos: {vinhos}")
        print(f"lista de precos: {precos}")
        time.sleep(2)
        os.system("cls")
    elif opcao == 3:
        print("Saindo")
        time.sleep(2)
        os.system("cls")
        break
    else:
        print("opcao inválida, tente novamente")
        time.sleep(2)
        os.system("cls")