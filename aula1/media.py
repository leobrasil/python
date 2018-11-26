#!/usr/bin/python3
'''
Programa que vai pedir 2   notas pro usuarioo
calcular a media e se a media for maior ou igual 
'''

qteNotas = int(input('quantas notas serao digitadas: '))
notas = [None] * qteNotas
for i in range(len(notas)):
    notas[i] = float (input('Digite a nota: '))


soma = 0

for i in (notas):
    soma+=i

media = soma / len(notas)

if media >= 7:
    print('aprovado - media: {}'.format(media))
elif media>=3:
    print('recuperacao - media: {}'.format(media))
else:
    print('reprovado - media: {}'.format(media))