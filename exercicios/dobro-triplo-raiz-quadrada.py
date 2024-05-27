# crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

from math import sqrt
number = int(input("numero: "))
multip = number*2
triplo = number*3
raiz = sqrt(number)
print(f'seu numero foi {number} e o dobro é {multip} e o triplo {triplo} enquanto a raiz quadrada é {raiz}')
