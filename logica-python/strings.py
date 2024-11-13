    # Saída de dados com print() e f-strings {}
    # Introdução: As f-strings (formatted string literals) foram introduzidas no Python 3.6 e fornecem uma maneira prática e eficiente de formatar strings. Elas permitem a inclusão de expressões dentro de uma string, que são avaliadas no momento da execução, tornando o código mais legível e conciso.
    # Fonte: (https://pythonacademy.com.br/blog/f-strings-no-python)

a = 5 
b = 10 
print(f"A soma de {a} e {b} é {a + b}.")
    # A soma de 5 e 10 é 15;
    # {} abre e fecha os formatadores;
    # Boas praticas: usar os valores mais claros possiveis, para os input().

print(f"Preço: R$ {25.12345: .2f}")
    # f vem antes das (""), as quais carregam a informação;
    # Dentro de {}, vamos agregar o valor a sem formatado, juntamente com a forma de formatação;
    # o (.) esta informando a partir de qual infrmação sera feita a formatação.

print(f"O valor inteiro é: {10: d}") # d formata p/ decimal
print(f"O valor em binario é: {23: b}") # binario 
print(f"Pi: {3.14159265: f}")
print(f"Pi: {3.14159265: .2f}")

numero_1 = 23
numero_2 = 10
numero_3 = 1993
print(numero_1, numero_2, numero_3)
print(numero_1, numero_2, numero_3, end="...\n")
    # Saida: 23 10 1993...
    # end= foi chamado para usar strings, logo apos os input, sem quebra de linha
    # \n significa "new line"

print("Início", end="-->")
print("Meio", end="-->")
print("Fim")
    # Saida: Início-->Meio-->Fim
    # Ou seja, pode trazer varias "print" na mesma line; sem quebra de linha

print("Olá, mundo!", end=" ")
print("Como você está?")
    # Foi usado ESPAÇO apenas para separar os 'print' na saida;
    # Saida: Olá, mundo! Como você está?

print("Olá", "mundo", "!", sep="-")
    # Saida: Olá-mundo-!
print("Olá", "mundo", "!", sep="_")
    # Saida: Olá_mundo_! 
    # ou seja, permite controlar como os itens passados para a função print() são separados.

