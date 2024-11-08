# Funções nativas (built-in functions)
# Introdução: Em Python, funções nativas (ou built-in functions) são aquelas que estão sempre disponíveis, sem a necessidade de importar módulos ou bibliotecas adicionais. Elas fazem parte da linguagem Python e são amplamente utilizadas devido à sua eficiência e simplicidade.
# Fontes: (https://docs.python.org/pt-br/3/library/functions.html)
'''
~> Funções de Manipulação de Strings
len(): Retorna o comprimento de uma string.
upper(): Converte uma string para letras maiúsculas.
lower(): Converte uma string para letras minúsculas.

~> Funções Matemáticas
abs(): Retorna o valor absoluto de um número.
max(): Retorna o maior valor entre dois ou mais números.
min(): Retorna o menor valor entre dois ou mais números.
sum(): Retorna a somatoria dos valores.

~> Funções de Manipulação de Listas
append(): Adiciona um elemento ao final de uma lista.
sort(): Ordena os elementos de uma lista.
reverse(): Inverte a ordem dos elementos de uma lista.

~> Funções de Gerenciamento de Arquivos
open(): Abre um arquivo no modo especificado.
read(): Lê o conteúdo de um arquivo.
write(): Escreve dados em um arquivo.

~> Funções de Condição e Iteração
all(): Retorna True se todos os elementos de um iterável são verdadeiros.
any(): Retorna True se algum elemento de um iterável for verdadeiro.
enumerate(): Cria um iterador que produz pares de índice/valor a partir de um iterável.
'''

lista = [10, 20, 30, 40, 50] # os [ ] apareceram na print
tamanho = len(lista) # len é uma função nativa
print(f'Na lista {lista} à {tamanho} valores.')

lista = [10, 20, 30, 40, 50]
tamanho = len(lista)
soma = sum(lista) # funções nativas, podem trabalhar em conjunto.
print(f'A lista {lista} tem um somatorio igual a {soma}.')

texto = input("Digite uma palavra ou frase: ")
tamanho = len(texto)
print(f"A palavra ou frase '{texto}' contém {tamanho} caracteres.")

