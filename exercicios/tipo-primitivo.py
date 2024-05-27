# faça um programa que leia algo pelo teclado e mostre na tela o seu
# tipo primitivo e  todas as informações possiveis sobre ele.

a = input('Digite algo: ')
print('o tipo primitivo desse valor é:', type(a))
print('só tem espaços? ', a.isspace())
print('é um número?', a.isnumeric())
print('é alfabético? ', a.isalpha())
print('é alfanumérico? ', a.isalnum())
print('está em maíusculas? ', a.isupper())
print('está em minúsculas? ', a.islower())
print('está capitalizada? ', a.istitle())
