# Definição do menu
menu = ''' BANCO DIGITAL SGS

    Opções:
    
    [1] Deposito
    [2] Saque
    [3] Extrato
    [4] Saldo
    [5] Fechar aplicativo 
    
    '''
    
# Opções válidas do menu
OPCOES_MENU = [1, 2, 3, 4, 5,]

# Limite de saques diários
LIMITE_SAQUES = 3

# Lista para armazenar o histórico de transações
extrato = []

# Saldo inicial da conta
saldo = 0

# Loop principal do aplicativo
while True:
    print(menu)  # Exibe o menu para o usuário
    opcao_escolhida_pelo_usuario = input("Digite o que deseja: ")  # Solicita a opção de ação desejada

    # Converte a entrada para um número inteiro se for um dígito; caso contrário, mantém como uma string
    opcao_escolhida_pelo_usuario = int(opcao_escolhida_pelo_usuario) if opcao_escolhida_pelo_usuario.isdigit() \
        else opcao_escolhida_pelo_usuario

    # Verifica se a escolha do usuário é uma opção de menu válida
    if opcao_escolhida_pelo_usuario not in OPCOES_MENU:
        print()
        print("Digite uma opção válida, opção escolhida inexistente.\n")
    elif opcao_escolhida_pelo_usuario == 1:
        # Opção de depósito
        valor_deposito = input("Digite o valor a ser depositado: ")
        if valor_deposito.replace('.', '', 1).isdigit() and float(valor_deposito) > 0:
            valor_deposito = float(valor_deposito)
            saldo += valor_deposito
            extrato.append(f"Depósito no valor de  R$ {valor_deposito:.2f} ")
            print(f"Depósito realizado no valor de R$ {valor_deposito:.2f}\n")
        else:
            print("O depósito não pode ser concluído pois não atende aos pré-requisitos.\n")
    elif opcao_escolhida_pelo_usuario == 2:
        # Opção de saque
        if LIMITE_SAQUES > 0:
            print(f"Saldo no valor de R$ {saldo:.2f}")
            valor_saque = input("Digite o valor do saque: ")
            valor_saque = float(valor_saque)
            if valor_saque > saldo:
                print("Saldo insuficiente para realizar o saque.")
            elif valor_saque > 500:
                print("valor de saque superior ao limite de R$ 500,00 por saque.")
            else:
                extrato.append(f"Saque no valor de  R$ {valor_saque:.2f} ")
                print(f"Saque realizado no valor de R$ {valor_saque:.2f}\n")
                saldo -= valor_saque
                LIMITE_SAQUES -= 1
        else:
            print("O saque não pode ser concluído pois excede o limite de saque diário.\n")
    elif opcao_escolhida_pelo_usuario == 3:
        # Opção de extrato
        if not extrato:
            print("Não possui nenhuma movimentação.\n")
        else:
            for operacao in extrato:
                print(operacao)
            print('\n')
    elif opcao_escolhida_pelo_usuario == 4:
        # Opção de consulta de saldo
        if saldo == 0:
            print("Não possui saldo no momento.")
        else:
            print(f"Valor do Saldo = R$ {saldo:.2f}\n")
    elif opcao_escolhida_pelo_usuario == 5:
        # Opção de fechar o aplicativo
        print("Fechando aplicativo...")
        break
