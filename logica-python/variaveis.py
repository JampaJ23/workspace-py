    # Variáveis, tipos de dados e atribuição
    # Introdução: As variáveis em Python são usadas para armazenar informações que podem ser referenciadas e manipuladas em um programa. Uma variável pode ser vista como um "rótulo" que aponta para um valor ou um objeto na memória.
    # Fonte: (https://hub.asimov.academy/tutorial/entendendo-variaveis-em-python/)

nome = int(input('Digite o dia de seu nascimento: '))
    # Possuem "Tipo", "Nome" e "Conteudo";
    # Deve se formatar corretamente;
    # NÃO pode começar com numeros. Usar _1, _2, _3;
    # NÃO pode contar caracteres especiais ou espaço;
    # NÃO pode haver DOIS iguais;
    # Python é case sensitive.

idade = int(input('Digite sua idade: '))
altura = float(input('Qual a sua altura: '))
nome = input('Digite seu nome: ')
print(f'Confirme as seguintes informações: Seu nome é {nome}, você tem {idade} anos, e sua altura é de aproximadamente {altura} metros. Correto?')

