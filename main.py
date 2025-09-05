LIMITE_DE_SAQUES = 3

LIMITE_DE_VALOR_DE_SAQUES = 500

saldo = 0

saques = 0

sacado = 0

registro = []

while True :
	print(f"Saldo: R${saldo:.2f}.")

	print("Qual operação você deseja efetuar? Disponíveis:\n[sacar]\n[depositar]\n[extrato]")

	print("Digite [sair] para sair.")

	entrada = input("> ")

	match entrada :

		case "sair" : break

		case "depositar" :
			valor = float(input("Qual é o valor a ser depositado?\n> "))

			if valor < 0 :
				print("Ignorando valor negativo.")

				continue

			elif valor == 0 :
				print("Ignorando valor nulo.")

				continue

			else :
				registro.append({"operação": "depósito", "valor": valor})

				saldo += valor

		case "sacar" :

			if not (saques <= 3) :
				print("Limite de saques atingido.")

			else :
				if not (saques <= LIMITE_DE_SAQUES) :
					print(f"Limite de saques ({LIMITE_DE_SAQUES}) atingido.")

					continue

				saques += 1

				valor = float(input("Qual é o valor a ser sacado?\n> "))

				if (valor+sacado) > LIMITE_DE_VALOR_DE_SAQUES :
					print(f"Saque excede o limite de saques de {LIMITE_DE_VALOR_DE_SAQUES}.")

					continue

				sacado += valor

				saldo -= valor

				registro.append({"operação": "saque", "valor": valor})

		case "extrato" :
			for operacao in registro : print(operacao)

		case _ :
			print("Opção invalida.")

			continue
