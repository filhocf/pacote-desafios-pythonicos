"""
13. wordcount

Este desafio é um programa que conta palavras de um arquivo qualquer de duas
formas diferentes.

A. Lista todas as palavras por ordem alfabética indicando suas ocorrências.

Ou seja...

Dado um arquivo letras.txt contendo as palavras: A a C c c B b b B
Quando você executa o programa: python wordcount.py --count letras.txt
Ele deve imprimir todas as palavras em ordem alfabética seguidas
do número de ocorrências.

Por exemplo:

$ python wordcount.py --count letras.txt
a 2
b 4
c 3

B. Lista as 20 palavras mais frequêntes indicando suas ocorrências.

Ou seja...

Dado um arquivo letras.txt contendo as palavras: A a C c c B b b B
Quando você executa o programa: python wordcount.py --topcount letras.txt
Ele deve imprimir as 20 palavras mais frequêntes seguidas
do número de ocorrências, em ordem crescente de ocorrências.

Por exemplo:

$ python wordcount.py --topcount letras.txt
b 4
c 3
a 2

Abaixo já existe um esqueleto do programa para você preencher.

Você encontrará a função main() chama as funções print_words() e
print_top() de acordo com o parâmetro --count ou --topcount.

Seu trabalho é implementar as funções print_words() e depois print_top().

Dicas:
* Armazene todas as palavras em caixa baixa, assim, as palavras 'A' e 'a'
  contam como a mesma palavra.
* Use str.split() (sem parêmatros) para fazer separar as palavras.
* Não construa todo o programa de uma vez. Faça por partes executando
e conferindo cada etapa do seu progresso.
"""

import sys


# +++ SUA SOLUÇÃO +++
# Defina as funções print_words(filename) e print_top(filename).
def print_words(filename):
    arquivo = open(filename)
    resposta = {}

    for linha in arquivo:
        palavras = linha.split()
        
        for palavra in palavras:

            limpo = remove_trash(palavra)
            #print(palavra, limpo)

            if limpo in resposta:
                resposta[limpo.lower()] += 1
            else:
                resposta[limpo.lower()] = 1
    
    respostas = {}
    
    for i in sorted(resposta.keys()):
        respostas[i] = resposta[i]
    
    option = sys.argv[1]
    if option == '--count':
        for key in respostas:
            print(key, ' :: ', respostas[key])

    return respostas

def remove_trash(word):
    to_clean = word
    trash = ('\'s', '\'ll', '\'re','\'ve','!','.','?',',', ':', '\'', ';', ')', '(', '"')


    for x in range(len(trash)):
        if trash[x] in to_clean.lower():
            to_clean = to_clean.replace(trash[x], '')

    return to_clean

def print_top(filename):
    listagem = print_words(filename)
    listagem_ordenada = sorted(listagem.items(), key=lambda x: x[1], reverse=True)
    x = 0
    if len(listagem_ordenada) > 20:
        print('20')
        x = 20
    else:
        print(len(listagem_ordenada))
        x = len(listagem_ordenada)

    for i in range(0, x):
        print(i+1, ' :: ', listagem_ordenada[i])
    
    return

# A função abaixo chama print_words() ou print_top() de acordo com os
# parêtros do programa.
def main():
    if len(sys.argv) != 3:
        print('Utilização: ./13_wordcount.py {--count | --topcount} file')
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    else:
        print('unknown option: ' + option)
        sys.exit(1)


if __name__ == '__main__':
    main()
