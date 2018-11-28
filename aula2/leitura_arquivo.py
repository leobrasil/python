#!/usr/bin/python3

conteudo = 5 * ['novo\n']

try:
    with open('teste1.txt','x') as arquivo:
        for x in conteudo:
            arquivo.write(x)
except FileExistsError:
    print('arquivo ja existe')