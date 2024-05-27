# crie um programa que leia um número Real qualquer pelo teclado
# e  mostre na tela a sua porção Inteira.

# ex: digite um número: 6.127
#     o numero 6.127 tem a parte inteira de 6.

# from math import trunc
# num = float(input('Digite um valor: '))
# print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, trunc(num)))

num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, int(num)))
