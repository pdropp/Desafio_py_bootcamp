from numpy import double


menu = """
    Escolha a opção que você deseja: 
    [DEPÓSITO] 
    [SAQUE]   
    [EXTRATO]
    
=> """

saldo = 0
limite_saque_diario = 500
extrato = ""
numero_saques = 0
limite_saques = 3


while True:

    opcao = input(menu).upper()

    match opcao:
        case "DEPOSITO":
            valor_deposito = int(input("Qual valor você deseja depositar? "))
            if valor_deposito > 0:
                saldo += valor_deposito
                extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
                print(f"Operação realizada com sucesso! Saldo após depósito: R$ {saldo:.2f}")
            else:
                print("Valor não permitido, tente outro valor acima de 0")

        case "SAQUE":
            if numero_saques >= limite_saques:
                print("Você excedeu o limite de saques diário")
            else:
                valor_saque = double(input("Qual valor você gostaria de sacar? "))
                if valor_saque > saldo:
                    print("Saldo insuficiente para realizar o saque.")
                elif valor_saque > limite_saque_diario:
                    print("Valor não permitido! Seu valor limite para saque é de R$ 500,00 ")
                elif valor_saque <= 0:
                    print("Valor de saque inválido, tente outra operação")
                else:
                    saldo -= valor_saque
                    limite_saque_diario -= valor_saque
                    numero_saques += 1
                    extrato += f"Saque: R$ {valor_saque:.2f}\n"
                    print(f"Saque realizado com sucesso! Seu saldo atual é de R$ {saldo:.2f}")
                    
        case "EXTRATO":
            print("\n========== EXTRATO ==========")
            print("Não foram realizadas movimentações." if not extrato else extrato)
            print(f"\nSaldo atual: R$ {saldo:.2f}")
            print("=============================")
            break

        case _:
            print("Opção inválida, tente novamente")
