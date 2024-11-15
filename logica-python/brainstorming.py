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
SAQUE_LIMITE = 1500
SAQUE_CAIXA = 500
SAQUE_DIA = 3

while True:

    opcao = (input(menu))

    if opcao == 1:
        deposito = float(input('Digite o valor a ser depositado em sua conta: '))
        saldo += deposito
        print(f'Seu novo saldo é de: {saldo}')
        escolha = int(input('Deseja voltar ao menu? [1] SIM ou [2] para NÂO: '))
        if escolha > 1:
            print('Obrigado por usar nosso banco!')
            break
        else:
            menu
    if opcao == 2:
        sacar = float(input('Digite, o valor a ser sacado: '))
        if saldo < sacar:
            print(f'Valor insuficiente para saque, pois seu saldo é de {saldo: .2f}.')
            escolha = int(input('Deseja voltar ao menu? [1] SIM ou [2] para NÂO: '))
            if escolha > 1:
                print('Obrigado por usar nosso banco!')
                break
            else:
                print(f'Seu no saldo é de: R$ {saldo: .2f} - {sacar}')
    if opcao == 3:
        print(f'Seu saldo atual é de: R$ {saldo: .2f}')
        escolha = int(input('Deseja voltar ao menu? [1] SIM ou [2] para NÂO: '))
        if escolha > 1:
            print('Obrigado por usar nosso banco!')
            break
        else:
            menu