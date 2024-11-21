# Usar apenas para rodar codes em aprendizado!

'''
Desafio v1: Sistema bancário(simples) para um usuario, onde sejá possivel depositar e armazenar; extratos deveram poder ser consultados.
Saque limite diario de 3 vezes, no valor de 500,00 cada

'''

nome = str(input('Digite seu nome: '))
usuario = nome.title()

print(f'Olá, {usuario}! Escolha uma das opções abaixo.')

opcoes = [1,2,3,4]

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

SAQUE_CAIXA = 3
SAQUE_LIMITE_CAIXA = 500
SAQUE_LIMITE_DIA = 1500
saque_limite_diario = SAQUE_LIMITE_DIA
saque_caixa_dia = SAQUE_CAIXA
cliente_limite_dia = ...


while True:

    opcao = int(input(menu))

    if opcao == 1:
        deposito = float(input('Digite o valor a ser depositado em sua conta: '))
        saldo += deposito
        print(f'Seu novo saldo é de: {saldo}:')
        escolha = int(input('Deseja voltar ao menu? [1] SIM ou [2] para NÂO: '))
        if escolha > 1:
            print('Obrigado por usar nosso banco!')
            break
        else:
            menu

    if opcao == 2:
        sacar = float(input('Digite, o valor a ser sacado: '))
        if sacar < saldo and sacar < SAQUE_LIMITE_CAIXA:
            print(f'Seu novo saldo é de: R$ {saldo - sacar}')
            escolha = int(input('Deseja voltar ao menu? [1] SIM ou [2] para NÂO: '))
            if escolha == 1:
                print('Obrigado por usar nosso banco!')
                menu
            else:
                break              
        else:
            print(f"Desculpe {usuario}, mas não foi possivel completar o saque. Pois seu saque de R$ {sacar}, é maior do que o saldo em sua conta ou seus limites. Verifique se o valor não excede seu limite diario de R$ {SAQUE_LIMITE_DIA} ou seu limite de saque em caixa de R$ {SAQUE_LIMITE_CAIXA}")
            escolha = int(input('Deseja voltar ao menu? [1] SIM ou [2] para NÂO: '))
            if escolha > 1:
                print('Obrigado por usar nosso banco!')
                break

    if opcao == 3:
        print(f'Seu saldo atual é de: R$ {saldo: .2f}')
        escolha = int(input('Deseja voltar ao menu? [1] SIM ou [2] para NÂO: '))
        if escolha > 1:
            print('Obrigado por usar nosso banco!')
            break
        else:
            menu

# Finalizado v1