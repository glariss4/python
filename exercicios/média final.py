# programa para somar 4 notas de avaliações e receber a média final.

n1 = int(input('nota 1: '))
n2 = int(input('nota 2: '))
n3 = int(input('nota 3: '))
n4 = int(input('nota 4: '))
s = n1+n2+n3+n4
resultado = s / 4

# print ('a soma total equivale a: ' , s)
# print ('a soma entre ' , n1 , 'e' , n2 , ' equivale a :' , s)


# print (f'a soma entre {}, {}, {} e {} equivale a:  {}'.format(n1 , n2 , n3 , n4 , s))

print(f'a soma entre {n1}, {n2}, {n3} e {n4} equivale a: {s}')
print(f'média final: {resultado}')
