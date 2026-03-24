#01 - Setor fiscal
taxa_imposto = 0.15
valor = input("Faturamento (ex. R$5.000,00): ")
valor = valor.replace("R$", "").replace(".", "").replace(",", ".")
valor_numerico = float(valor)
imposto = taxa_imposto * valor_numerico
print(f"Valor do imposto: R${imposto:,.2f}")

#02 - Setor de RH
print("-----------------")
nome = input("Digite seu nome completo: ")
email = input("Digite seu email: ")
posicao = nome.find(" ")
primeiro_nome = nome[:posicao].capitalize().strip()
email = email.strip().lower()
print(f"Cadastro: {primeiro_nome}. E-mail: {email}")

#03 - Setor de RH
print("-----------------")
fat_a = input("Faturamento da empresa A: ")
fat_b = input("Faturamento da empresa B: ")
fat_a_num = float(fat_a.replace("R$", "").replace(".", "").replace(",", ".")) 
fat_b_num = float(fat_b.replace("R$", "").replace(".", "").replace(",", "."))
fat_total = fat_a_num + fat_b_num
media = fat_total / 2
print(f"O faturamento total entre as duas empresas é R${fat_total:,.2f} e a média entre as empresas é de R${media:,.2f}")