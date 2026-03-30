#01 - Automação de convites
# for i in range(11):
#     falta = 10 - i
#     if falta > 1:
#         print(f"Faltam {falta} minutos para começar a reunião")
#     elif falta == 1:
#         print(f"Falta {falta} minuto para começar a reunião")
#     else:
#         print("Reunião começou!!")

#02 - Cálculo de comissão progressiva
# vendas = [2000, 5000, 1000, 8000, 3000]
# comissao_total = 0
# for i in vendas:
#     if i > 4000:
#         comissao = 0.1
#     else:
#         comissao = 0.05
#     comissao_total = comissao_total + i * comissao
# print("Lista de vendas: ", vendas)
# print("Comissão total: ", comissao_total)

#03 - Verificação de estoque crítico
estoque = ["monitor", "mouse", "teclado", "gabinete", "processador"]
quantidade = [10, 35, 4, 20, 7]
for i in quantidade: 
    if i < 8:
        posicao = quantidade.index(i)
        print(f"ALERTA: o produto {estoque[posicao]} está com apenas {i} itens")