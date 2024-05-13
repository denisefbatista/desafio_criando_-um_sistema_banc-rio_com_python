menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        print("Depósito")
        # Solicitar o valor do depósito e atualizar o saldo
        valor = float(input("Qual o valor do depósito?: "))  
        if valor >= 1:
            saldo += valor  
            extrato += f"Depósito: +R${valor:.2f}\n"  
            print(f"Você depositou R${valor:.2f}!")
        else:
            print("Valor inválido")

    elif opcao == "2":
        print("Saque")
        valor = float(input("Qual o valor do saque?: "))  
        # Verificar se o valor do saque é positivo
        if valor >= 0:
            # Verificar se há saldo suficiente para o saque
            if valor <= saldo:  
                # Verificar se o valor do saque está dentro do limite
                if valor <= limite:  
                    # Processar o saque e atualizar o saldo e o extrato
                    saldo -= valor  
                    numero_saques += 1
                    if numero_saques > LIMITE_SAQUES:
                        print("Você atingiu o máximo de saques por hoje!")
                    else:
                        extrato += f"Saque: -R${valor:.2f}\n"  
                        print(f"Você sacou R${valor:.2f}!")
                else:
                    print("Você não pode sacar mais que R$500,00 por saque!")
            else:
                print("Saldo insuficiente.")
        else:
            print("Valor inválido")

    elif opcao == "3":
        print("Extrato")
        print(extrato)
        print(f"Seu saldo atual é de: R${saldo:.2f}")

    elif opcao == "0":
        print("Saindo...")
        break

    else:
        print("Opção inválida, por favor selecione novamente a opção desejada.")