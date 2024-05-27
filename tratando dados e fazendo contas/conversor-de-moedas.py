# crie um programa que leia quanto dinheiro uma pessoa tem na
# carteira e mostre quantos dólares ela pode comprar.


# considere U$ 1 = R$4,92

real = float(input('Quanto de dinheiro você tem na carteira? R$'))
dolar = real / 4.92
print('Com R${:.2f} você pode comprar U${:.2f}'.format(real, dolar))
