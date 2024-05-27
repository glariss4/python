# Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.
# operador in

nome = str(input('Qual é o seu nome completo?: ')).strip()
print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))
# print('Seu nome tem Silva? {}'.format('SILVA' in nome.upper))
