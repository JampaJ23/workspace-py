# Entrada de dados com input()
# Introdução: Em Python, a função input() é usada para receber dados do usuário durante a execução de um programa. Esta função pausa a execução do programa e espera que o usuário digite algum texto no console, que então é retornado como uma string. É uma ferramenta essencial para criar programas interativos.
# Fonte: (https://hub.asimov.academy/tutorial/entendendo-a-funcao-input-em-python/)

print('O perimetro em metros é: ', input('Qual é o perimetro em metros?'))

print('Confirme sua idade: ', input('Qual a sua idade?'))

print('Confirme se a data esta correta, por favor: ', input('Qual a data da proxima reuniao?'))
# Aqui temos exemplos de INPUT dentro do print;
# Importante: Desta forma o dado do input NÃO é salvo, apenas, informado no print.

mts = input('Qual é o perimetro em metros? ')
print(f'O perimetro são: {mts} metros. Correto?')
# Desta maneira, os dados do input são devidamente SALVOS;
# Importante: Desta forma, PRECISAM ser formatados os f-strings corretamente;

nome = input('Insira seu nome: ')
tel = input('Insira seu telefone: ')
rgn = input('Insira seu RG: ')
print(f'Nome de usuario: {nome}, telefone: {tel}, RG {rgn}')

