#!/usr/bin/python3

matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

soma = 0
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if i==j:
            soma+=matriz[i][j]

print (soma)

soma = 0
count =0
for i in matriz:
    soma += i[count] + i[-(count+1)]
    count += 1

print (soma)
