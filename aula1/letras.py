#!/usr/bin/python3

'''
cria uma lista de letras de a-z  com loop
'''
letras = [] 
for i in range(97,123):
    letras.append( chr(i) )

print(letras)

letras = [chr(x) for x in range(97,123)]
print (letras)