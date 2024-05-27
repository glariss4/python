# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
# todo numero par por 2 da zero e todo numer impar por 2 é igual a 1

número = int(input('Me diga um número qualquer:  '))
resultado = número % 2
if resultado == 0:
    print('o número {} é PAR'.format(número))
else:
    print('o número {} é IMPAR'.format(número))