# 07-nov
# Operadores e expressões aritméticas
# Exemplos: (+) (-) (*) (/) (%)

n1 = float(input('Digite um numero: ')) 
n2 = float(input('Digite o segundo numero: '))
# Float foi chamado, pois, os valores poder ser decimais; (33.3, 9.5, 0.33)
soma = n1 + n2
subt = n1 - n2
mult = n1 * n2
div = n1 / n2 # Valor mais proximo, a ser dividido; (QUOCIENTE)
divr = n1 % n2 # Resultado do restante da divisão.

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
