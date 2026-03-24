#01 - Relatório de margem de lucro
fat = 45000
custo = 23500
lucro = fat - custo
margem = lucro / fat
print(f"Lucro: R${lucro:,.2f}")
print(f"Margem: {margem:.0%}")

#02 - Padronização de dados do crm
nome = " mArCoS aNtOnIo rOcHa "
email = " MARCOS.ROCHA@GMAIL.COM "
nome = nome.strip() #essa função tira espaços no fim, no começo e espaço duplicados
nome = nome.title() #transforma o nome num titulo
print(nome)
email = email.strip()
email = email.lower() #deixa tudo minusculo
print(email)

#03 - Migração de servidor de e-mail
email = "andre_silva@empresa.com.br"
print(email)
email = email.replace("@empresa.com.br", "@grupocorp.com")
print(email)

#04 - Extração de username para log
email = "beatriz.oliveira@empresa.com"
posicao_a = email.find("@")
log = email[:posicao_a]
print(log)

#05 - Personalização de email
nome = "lucas ferreira canal"
pos_e = nome.find(" ")
nome = nome[:pos_e]
nome = nome.title()
print(f"Olá, {nome}! seja bem-vindo ao nosso clube.")