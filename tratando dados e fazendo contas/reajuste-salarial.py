# faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input(' Valor do salário do funcionário: R$'))
ajuste = salario + (salario * 15 / 100)

print('O funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(salario, ajuste))
