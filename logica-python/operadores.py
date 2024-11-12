    # Operadores e expressões aritméticas
    # Introdução: Em Python, operadores e expressões aritméticas são fundamentais para realizar cálculos e manipulações numéricas.
    # Fonte: (https://www.bosontreinamentos.com.br/programacao-em-python/7-python-operadores-e-expressoes-aritmeticas/)

'''
~> Numericos
    + Adição	
    - Subtração	
    / Divisão	
    * Multiplicação	
    ** Potenciação	
    % Módulo
~> Strings
    + Concatenar	
    * Repetir	
~> Lists, Tuples
    + Concatenar	
    * Gerar	
'''

numero_1 = float(input('Digite um numero: ')) 
numero_2 = float(input('Digite o segundo numero: ')) 
    # Float foi chamado, pois, os valores podem ser decimais;
soma = numero_1 + numero_2
subt = numero_1 - numero_2
mult = numero_1 * numero_2
div = numero_1 / numero_2 # Valor mais proximo, a ser dividido (QUOCIENTE).
div = numero_1 // numero_2 # Divisão inteira.
divr = numero_1 % numero_2 # Resultado do restante da divisão.

print(f'A soma dos valores é: {soma}')
print(f'A subtração dos valores é: {subt}')
print(f'A multiplicação dos valores é: {mult}')
print(f'A divisão dos valores é: {div}')
print(f'O resto da divisão dos valores é: {divr}')

dado = 10
print(f'Conteudo da varialvel dado: {dado}')
dado += 1 # equivalente à  -> dado = dado + 1
print('Conteudo da variavel dado, apos incremento: {dado}')
dado -= 1 # equivalente à -> dado = - 1
print('Conteudo da variavel dado, apos decremento: {dado}')

dado = 10
print(f'Conteudo da varialvel dado: {dado}')
dado *= 2 # equivalente à  -> x2
print(f'Conteudo da variavel dado em multiplicação: {dado}')
dado /= 2 # equivalente à -> metade
print(f'Conteudo da variavel dado em divisao: {dado}')

n1 = float(input('Digite um numero: '))
n2 = float(input('Digite o segundo numero: '))
n3 = float(input('Digite o terceiro numero: '))
nt = n1 + n2 + n3
print(f'O resultado da media, dos tres valores digitados anteriormente é: {nt / 3: .2f}')
    # o formatação do valor numerico, é feita apos (:), separando o valor ao formato;
    # ex: { xxx: <formatação>}

#---------- Comparação de Atribuição (True ou False)
saldo = 1000
saque = 100
print(saldo > saque) # > Maior
print(saldo >= saque) # > = Maior ou igual
print(saldo < saque) # < Menor
print(saldo <= saque) # < = Menos ou igual
print(saldo == saque) # = = Igual
print(saldo != saque) # ! = Diferente

#---------- Comparação Lógicos (and ou or / not)
saldo = 1000
saque = 200
limite = 100
condicao_1 = (saldo >= saque) and (saque <= limite) # False
print(condicao_1)

saldo = 1000
saque = 200
limite = 100
condicao_2 = (saldo >= saque) or (saque <= limite) # True
print(condicao_2)

#---------- Comparação de Negação (not)
not limite > saldo # True, pois inverte a lógica.

#---------- Identidade (is)
curso = "Curso ode Python"
nome_curso = curso # Recebe a variavel curso.
aula = curso is nome_curso # True
print(aula)

saldo, limite = 200, 200
saldo is limite # True
saldo is not limite # False

saldo = 200
limite = 200
saldo is limite # 
print(saldo is limite) # True, pois apontam para o mesmo objeto.
print(saldo is not limite) # False, pois NOT inverte a condição.

#---------- Associação (in)
curso = "Curso de Python"
frutas = ["laranja", "uva", "limão"]
saques = [1500, 100]

"Python" in curso # True, Python está na variavel.
"maçã" not in frutas # True, realmente não está na variavel.
200 in saques # False, pois nao ha 200 na varialvel 'saques'
    # Case sensitive: o valor NECESSARIAMENTE, precisa ser igual.