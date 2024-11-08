# Saída de dados com print() e f-strings {}
# Introdução: As f-strings (formatted string literals) foram introduzidas no Python 3.6 e fornecem uma maneira prática e eficiente de formatar strings. Elas permitem a inclusão de expressões dentro de uma string, que são avaliadas no momento da execução, tornando o código mais legível e conciso.
# Fonte: (https://pythonacademy.com.br/blog/f-strings-no-python)

a = 5 
b = 10 
print(f"A soma de {a} e {b} é {a + b}.")
# A soma de 5 e 10 é 15.
# {} abre e fecha os formatadores.

print(f"Preço: R$ {25.12345: .2f}")
# f vem antes das (""), as quais carregam a informação;
# Dentro de {}, vamos agregar o valor a sem formatado, juntamente com a forma de formatação;
# o (.) esta informando a partir de qual infrmação sera feita a formatação.

print(f"O valor inteiro é: {10: d}") # d formata p/ decimal
print(f"O valor em binario é: {23: b}") # binario 
print(f"Pi: {3.14159265: f}")
print(f"Pi: {3.14159265: .2f}")

