    # Biblioteca Python (também conhecida como "Standard Library")
    # Introdução: A biblioteca padrão do Python é uma coleção robusta de módulos e pacotes que vêm integrados com a instalação padrão do Python. Esses módulos fornecem uma ampla gama de funcionalidades, desde manipulação de arquivos e processamento de texto até operações matemáticas avançadas e criação de servidores web.
    # Fontes: (https://docs.python.org/pt-br/3/library/index.html)
'''
~> Manipulação de Arquivos e Diretórios
    os: Fornece funções para interagir com o sistema operacional.
    shutil: Oferece operações de alto nível em arquivos e coleções de arquivos.

~> Operações Matemáticas
    math: Fornece funções matemáticas básicas, como sqrt(), sin(), cos().
    random: Gera números aleatórios.

~> Manipulação de Datas e Horas
    datetime: Fornece classes para manipular datas e horas.
    time: Oferece funções relacionadas ao tempo.

~> Estruturas de Dados
    collections: Fornece implementações alternativas de tipos de dados comuns, como deque, Counter, etc.
    array: Oferece suporte para matrizes de valores básicos.

~> Expressões Regulares
    re: Fornece suporte para expressões regulares.

~> Manipulação de Texto
    string: Fornece constantes e classes para manipulação de strings.
    textwrap: Oferece funções para manipulação de texto.

~> Entrada e Saída de Dados
    io: Oferece ferramentas para manipulação de fluxos de entrada e saída.
    csv: Permite leitura e escrita de arquivos CSV.

~> Trabalhando com Internet e Redes
    urllib: Fornece funções para manipular URLs e fazer requisições HTTP.
    http: Oferece classes para manipulação de requisições HTTP.

~> Serialização de Dados
    json: Oferece suporte para leitura e escrita de dados em formato JSON.
    pickle: Permite serializar e desserializar objetos Python.

~> Módulos Utilitários
    functools: Fornece funções de ordem superior que operam em outras funções, como reduce e partial.
    itertools: Fornece funções para criar geradores de iteração complexos.

~> Tratamento de Exceções
    logging: Oferece uma maneira flexível de gerar logs.
    traceback: Fornece utilitários para formatar e imprimir rastreamentos de pilha.
'''

import math
x = 16
raiz_quadrada = math.sqrt(x)
print(f'Raiz quadrada de {x} é igual a {raiz_quadrada}')

import os
diretorio_atual = os.getcwd() # (get current working directory)
print(f'O diretório atual é {diretorio_atual}')
     # import chama a biblioteca Python;
     # Sempre chamar import com a biblioteca antes;
     # Fechar parênteses, não basta apenas chamar o comando; Ex: math, getcwd, system.
 