#13) Faça um algoritmo que leia o salário de um funcionário, calcule e mostre o 
#seu novo salário, com 15% de aumento.

sal = float(input('Salario '))

aum = sal + (15 * sal /100)

print('O salário do funcionário com aumento é {}'.format(aum))
