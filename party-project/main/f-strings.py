# 06-nov 
# Saída de dados com print() e f-strings {}
# exemplo:
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

