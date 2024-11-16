nome = str(input('Digite seu nome: '))
usuario = nome.title()

print(f'Olá, {usuario}! Escolha uma das opções abaixo.')

opcoes = [1, 2, 3, 4]

deposito = 1
saque = 2
extrato = 3
sair = 4

menu = """
-----------------------
Depositar: [1]
Saque: [2]
Extrato: [3]
Sair: [4]
-----------------------
"""

saldo = 0
SAQUE_CAIXA = 3  # Limite de saques por dia
SAQUE_LIMITE_CAIXA = 500  # Limite de valor por saque
SAQUE_LIMITE_DIA = 1500  # Limite de valor total por dia
saques_realizados = 0  # Contador de saques

while True:
    opcao = int(input(menu))

    if opcao == 1:
        deposito = float(input('Digite o valor a ser depositado em sua conta: '))
        saldo += deposito
        print(f'Seu novo saldo é de: R$ {saldo:.2f}')
        escolha = int(input('Deseja voltar ao menu? [1] SIM ou [2] para NÃO: '))
        if escolha > 1:
            print('Obrigado por usar nosso banco!')
            break

    elif opcao == 2:
        if saques_realizados >= SAQUE_CAIXA:
            print(f"Desculpe {usuario}, você atingiu o limite máximo de {SAQUE_CAIXA} saques diários.")
        else:
            sacar = float(input('Digite o valor a ser sacado: '))
            if sacar <= saldo and sacar <= SAQUE_LIMITE_CAIXA and sacar <= SAQUE_LIMITE_DIA:
                saldo -= sacar
                saques_realizados += 1
                print(f'Seu novo saldo é de: R$ {saldo:.2f}')
            else:
                print(f"Desculpe {usuario}, o valor do saque excede o saldo ou o limite permitido. Verifique se o valor não excede seu limite diário de R$ {SAQUE_LIMITE_DIA} ou seu limite de saque em caixa de R$ {SAQUE_LIMITE_CAIXA}.")
        
        escolha = int(input('Deseja voltar ao menu? [1] SIM ou [2] para NÃO: '))
        if escolha > 1:
            print('Obrigado por usar nosso banco!')
            break

    elif opcao == 3:
        print(f'Seu saldo atual é de: R$ {saldo:.2f}')
        escolha = int(input('Deseja voltar ao menu? [1] SIM ou [2] para NÃO: '))
        if escolha > 1:
            print('Obrigado por usar nosso banco!')
            break

    elif opcao == 4:
        print('Obrigado por usar nosso banco!')
        break

    else:
        print("Opção inválida. Por favor, selecione uma opção válida.")
