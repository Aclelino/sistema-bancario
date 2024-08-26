saldo = 0
limit_day = 3
limit = 500
extrato = ""
print("""

#### System Bancking ####
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
		print("MENU > DEPOSITAR")
		valor = float(input("Digite o valor: "))
		saldo = saldo + valor
		print("Desposito realizado com sucesso!")
		extrato +=  "Depositado: R$ {:.2f}\n".format(valor)
	elif opcao == "2":
		print("MENU > SAQUE")
		valor = float(input("Digite o valor: "))
		if valor <= saldo:
			limit_day -= 1
			if limit_day >= 0 and valor <= limit :
				limit -= valor
				saldo = saldo - valor
				print("Saque realizado com sucesso!")
				extrato += " Saque: R$ {:.2f}\n".format(valor)
			else:
				print("Limite de saque esgotado!")
		else:
			print("Saldo Insulficiente")
	elif opcao == "3":
		print("MENU > Extrato")
		print(extrato, "\n\nSaldo disponivel: {:.2f}".format(saldo))
	elif opcao.lower() == "q":
		print("Tchau")
		break
