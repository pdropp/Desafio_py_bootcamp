def MENU_BANCO():
    menu = """\n
    ===Menu===
    [DP]]\tDepositar
    [SC]\tSacar
    [EX]\tExtrato
    [NC]\tNova conta
    [LC]\tListar contas
    [NU]\tNovo usuário
    [Q]\tSair
    
    => """
    return  input(menu);

def depositar(saldo, valor, extrato):

    if valor > 0:
        saldo += valor
        extrato += f"Depósito: \tR$ {valor:.2f}\n"
        print("\n === Depóstio realizado com sucesso! ===")
    else: 
        print("\n === operação falhou! o valor infomrado é inválido. ===")
    return saldo, extrato;


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saques:
        print("\n *** Operação falhou! você não tem saldo suficiente. ***")
    elif excedeu_limite:
        print("\n *** Operação falhou! o valor de saque excede o limite. ***")
    elif excedeu_saldo:
        print("\n *** Operação falhou! Número máximo de saques excedido. ***")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: \t\tR$ {valor:.2f}\n"
        numero_saques +=1
        print("\n === Saque realizado com sucesso! ===")

    else:
        print("\n *** Operação falhou! o valor informado é inválido. ***")
    return saldo, extrato
    


def exibir_extrato(saldo, / , *, extrato):
    print("\n ==================== EXTRATO ==================== ")
    print("Não foram realizaadas movimentações" if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("=====================================================")


def criar_usuario(usuarios):
   cpf = input("Informe o CPF (somente número): ")
   usuario = filtrar_usuario(cpf, usuarios=usuarios)
   
   if usuario:
        print("\n *** Usuário já existe com esse CPF ***")
        return
    
   nome = input("Infomre nome completo: ")
   data_nascimento = input("Infomre a data de nascimento (dd-mm-aaaa): ")
   endereco = input("Infomre o endereço (logradouro, nro - bairro - cidade/sigla estado)")
    
   usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
   print("=== Usuário cadastrado com sucesso! ===")

def filtrar_usuario(cpf, usuarios):
    usuario_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuario_filtrados[0] if usuario_filtrados else None;

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o cpf do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("\n === Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usario": usuario}
    
    print("\n *** Usuário não encontrado, fluxo de criação de ocnta encerrado! ***")
    return

def listar_contas(contas):
    for conta in contas:
        linha = f"""
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(linha)

def main():
    LIMITE_SAQUE = 3
    AGENCIA = "0001"
    
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    
    while True:
        opcao = MENU_BANCO()
    
        if opcao == "DP":
            valor = float(input("Informe o valor do depósito: "))
        
            saldo, extrato = depositar(saldo, valor, extrato)
        
        elif opcao == "SC":
            valores = float(input("informe o valor do saque: "))
        
            saldo, extrato = sacar(
            saldo=saldo,
            valor=valores,
            extrato=extrato,
            limite=limite,
            numero_saques=numero_saques,
            limite_saques=LIMITE_SAQUE,
            
            )
        elif opcao == "EX":
            exibir_extrato(saldo, extrato=extrato)
            
        elif opcao == "NU":
            criar_usuario(usuarios)
        elif opcao == "NC":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)
            
        elif opcao == "LC":
            listar_contas(contas)
            
        elif opcao == "Q":
            break
        
        else:
            print("*** Operação inválida, por favor sleecione novamente a operação desejada.")

main()
