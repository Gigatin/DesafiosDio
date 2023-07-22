menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

Escreva uma opção: """

saldo = 0
limite = 500
extrato = ""
qtd_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = int(input("Digite a quantidade que será depositada: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:}\n"

        else:
            print("Falha! Valor não permitido.")

    elif opcao == "s":
        valor = float(input("Valor Saque: "))

        saldoExcedente = valor > saldo

        limiteExcedente = valor > limite

        qntdSaquesExcedente = qtd_saques >= LIMITE_SAQUES

        if saldoExcedente:
            print("Falhou! Sem saldo.")

        elif limiteExcedente:
            print("Falhou! O limite da conta não permite.")

        elif qntdSaquesExcedente:
            print("Falha! Quantidade de saques diarios maximos já realizados.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:}\n"
            qtd_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n== Extrato ==")
        print("Sem novas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:}")
        print("===============")

    elif opcao == "q":
        break

    else:
        print("Operação invalida! selecione uma das opções presentes em nosso menu.")