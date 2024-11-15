    # Loops em Python
    # Estruturas de repetição for e while em Python. Esses loops são fundamentais para a programação, pois permitem que você execute um bloco de código várias vezes com base em certas condições.
    # Fontes: (https://blog.rocketseat.com.br/python-dominando-loops/)

i = 1
while i <= 10:
    print(i, " ", end="")
    i += 1
print()
    # Enquanto 'i' ser inferior ou igual a '10' continua o loop
    # variavel 'i' + 1 até que o loop, encontre seu limitador. (10)

h = 10
while h >= 1:
    print(h, " ", end="")
    h -= 1
print()
     # Enquanto 'h' ser maior ou igual a 1, continua se o loop.
     # Loop ira subtraira varialvel 'h' até que chege a 'seu' limite. (1)
     # Quando o loop atingir a 1, ira checar seu limitador e parar.
     
while True: # Loot continuo, ate que encontra um porem. (if,elif/else)
    usuario = int(input("Digite um número: "))
    if usuario == 0: # 'if' o numero seja (=) a 0, para. (break)
        print()
        break

