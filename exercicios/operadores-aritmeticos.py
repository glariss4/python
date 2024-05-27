# operadores aritméticos

n1 = int(input('um valor: '))
n2 = int(input('outro valor: '))
# print('a soma equivale a {}'.format(n1+n2))
s = n1+n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('a soma equivale a {}, o produto equivale a {} e sua divisão {}'.format(s, m, d), end=' >>>> ')
print('divisão inteira {}, e potência de {}'.format(di, e))
