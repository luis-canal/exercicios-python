#01 - Cálculo de bônus de vendas
fat = 50000
perc_bonus = 0.1
bonus_total = fat * perc_bonus
fat_liquido = fat - bonus_total
print(f"Faturamento liquido: R${fat_liquido:.2f}")
print(f"Bonus Total: R${bonus_total:.2f}")

#02 - Controle de estoque
estoque = 250
vendas = 78
reposicao = 100
estoque_atualizado = estoque - vendas + reposicao
print(f"Estoque atualizado: {estoque_atualizado}")

#03 - Divisao de cargas
caixas = 1250
caminhao = 12
caminhoes_cheios = caixas // caminhao
caixas_restantes = caixas % caminhao
print("caminhoes cheios:", caminhoes_cheios)
print("caixas restantes:", caixas_restantes)

#04 - Analise de margem de lucro
faturamento = 15000
custos = 5000
perc_imposto = 0.15
imposto = faturamento * perc_imposto
lucro = faturamento - custos - imposto
margem_lucro = lucro / faturamento
print("imposto:", imposto)
print("lucro:", lucro)
print("margem de lucro:", margem_lucro)
meta = margem_lucro > 0.3
print("meta atingida?", meta)

#05 - Conersão de tempo de contrato
duracao = 40 
anos = duracao // 12
meses = duracao % 12
print(f"{anos} anos e {meses} meses")
