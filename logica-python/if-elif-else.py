    # Estruturas condicionais e de repetição
    # Introdução: As estruturas condicionais permitem que seu programa execute diferentes blocos de código com base em determinadas condições. Em Python, usamos if, elif e else.
    # Fonte: (https://blog.betrybe.com/python/if-else/#2)

#---------- if
saldo = 2000.0
saque = float(input('Informe o valor do saque: '))
if saldo >= saque:
    print('Realizando saque!')
    print('Obrigado por ser nosso cliente!')
if saldo < saque:
    print('Saldo insuficiente!')
    print('Por favor, confira seu saldo e tente novamente.')

#---------- else
if saldo >= saque:
    print('Realizando saque!')
    print('Obrigado por ser nosso cliente!')
else:
    print('Saldo insuficiente!')
    print('Por favor, confira seu saldo e tente novamente.')
    # Perceba, que não ha necessidade de reformular o 'if'
    # Utilizamos quando apenas DOIS cenarios sao possiveis.

#---------- elif
IDADE_ENTRADA = 15
IDADE_LIMITE = 16
idade = int(input('Informe sua idade: '))
if idade <= IDADE_ENTRADA:
    print('Parabéns, você acaba de entrar para equipe sub 16!')
elif idade == IDADE_LIMITE:
    print('Você é um sub 16. Porém, este é seu ultimo ano na categoria Infanto-juvenil. Aproveite!')
else:
    print('Você não pode entrar na categoria Infanto-juvenil, pois sua idade excede o limite da categoria.')

#---------- if Aninhado
conta_normal = True
conta_universitaria = False
    # Valores setados, apenas para sumilação; (True,False)
    # Em uma situação real, estas variaveis podem mudar.
saldo = 2000
saque = 2500
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print('Saque realizado com sucesso!')
    elif saque <= (saldo + cheque_especial):
        print('Saque realizado com uso do cheque especial!')
    else:
        print('Desculpe, saldo insuficiente! Confira os valores.')
        
elif conta_universitaria:
    if saldo >= saque:
        print('Saque realizado com sucesso!')
    else:
        print('Saldo insuficiente!')

#---------- if Ternario
saldo = 2000
saque = 500

status = "Sucesso" if saldo >= saque else "Falha"
print(f'{status} ao realizar o saque!')