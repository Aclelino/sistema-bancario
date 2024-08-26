saldo = 0
limit_day = 3
limit = 500
extrato = ""
print("""

#### System bancking ####
""")
menu = """
---#---#---

[1] Depositar
[2] Sacar
[3] Extrato
[Q] Sair

---#---#---

=> """

while True:
	
	opcao = str(input(menu))
	if opcao == "1":
		print("Depositar")
		valor = float(input("Digite o valor: "))
		saldo = saldo + valor
		extrato +=  " Depositado: R$ {:.2f}\n".format(valor)
	elif opcao == "2":
		print("Sacar")
		valor = float(input("Digite o valor: "))
		if valor <= saldo:
			limit_day -= 1
			if limit_day >= 0 and valor <= limit :
				
				saldo = saldo - valor
				extrato += " Saque: R$ {:.2f}\n".format(valor)
			else:
				print("Limite diario Esgotado")
		else:
			print("Saldo Insulficiente")
	elif opcao == "3":
		print("Extrato")
		print(extrato, "\n\nSaldo disponivel ", saldo)
	elif opcao == "q":
		print("Tchau")
		break
