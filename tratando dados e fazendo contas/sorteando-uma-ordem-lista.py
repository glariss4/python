# o professor quer sortear a ordem de apresentação de trabalhos dos alunos.
# faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random

aluno1 = str(input('Primeiro aluno: '))
aluno2 = str(input('Segundo aluno: '))
aluno3 = str(input('Terceiro aluno: '))
aluno4 = str(input('Quarto aluno: '))
lista = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(lista)
print('A ordem de apresentação será: ')
print(lista)
