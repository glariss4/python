# crie um programa que leia dois numero e dê o resultado entre eles.

n1 = int(input('valor: '))
n2 = int(input('outro valor: '))
s = n1+n2

# print('a soma total equivale a: ' , s)
# print ('a soma entre ' , n1 , 'e' , n2 , ' equivale a :' , s)

print('a soma entre {} e {} equivale a:  {}'.format(n1, n2, s))
