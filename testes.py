saldo = 0.00
saques_atuais = 0
SAQUES_LIMITES = 3
extrato = []

while True:
    print("Escolha uma opção:")
    print("1. Depositar")
    print("2. Sacar")
    print("3. Verificar saldo")
    print("4. Verificar extrato")
    print("5. Sair")
    op = int(input())

    if op == 1:
        if deposito <= 0:
            print("valor invalido")
        else:
            deposito = float(input("Quanto deseja depositar?: "))
            saldo += deposito
            extrato.append(f"Depósito: +{deposito}")
            print(f"Depósito realizado! Seu novo saldo é: {saldo}")

    elif op == 2:
        saque = float(input("Quanto deseja sacar?: "))
        if saque > 500.00:
            print("O saque não pode ser maior que 500.00")
        elif saldo < saque:
            print("Saldo insuficiente")
        elif saques_atuais == SAQUES_LIMITES:
            print("Limite de saques alcançado")
        else:
            saldo -= saque
            saques_atuais += 1
            extrato.append(f"Saque: -{saque}")
            print(f"Saque realizado! Seu novo saldo é: {saldo}")

    elif op == 3:
        print(f"Seu saldo é: {saldo}")

    elif op == 4:
        print("Extrato:")
        for transacao in extrato:
            print(transacao)
        print(f"Saldo atual: {saldo}")

    elif op == 5:
        print("Saindo do programa...")
        break

    else:
        print("Opção inválida!")